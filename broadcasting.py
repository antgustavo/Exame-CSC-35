#!/usr/bin/env python

'Setting the position of nodes and providing circular mobility'

import sys
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.wmediumdConnector import interference
from mininet.term import makeTerm
import random
import time

def make_term(s1,s2,s3,s4):
    makeTerm(s1, cmd = "bash")
    makeTerm(s2, cmd = "bash")
    makeTerm(s3, cmd = "bash")
    makeTerm(s4, cmd = "bash")

def topology(args):
    # Definindo r para usar na probabilidade de erro
    r = random.random()
    
    "Create a network."
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    kwargs = {}
    if '-a' in args:
        kwargs['range'] = 100

    sta1 = net.addStation('sta1', ip6='fe80::1',
                          min_x=100, max_x=200, min_y=100, max_y=200, min_v=10, max_v=15, **kwargs)
    sta2 = net.addStation('sta2', ip6='fe80::2',
                          min_x=200, max_x=300, min_y=100, max_y=200, min_v=10, max_v=15, **kwargs)
    sta3 = net.addStation('sta3', ip6='fe80::3',
                          min_x=100, max_x=200, min_y=200, max_y=300, min_v=10, max_v=15, **kwargs)
    sta4 = net.addStation('sta4', ip6='fe80::4',
                          min_x=200, max_x=300, min_y=200, max_y=300, min_v=10, max_v=15, **kwargs)
    
    espiao = net.addStation('espiao', ip6='fe80::5',
                          min_x=0, max_x=400, min_y=0, max_y=400, min_v=10, max_v=15,
                           **kwargs)

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.2)

    info("*** Configuring nodes\n")
    net.configureNodes()

    if '-p' not in args:
        net.plotGraph(max_x=400, max_y=400, )
    
    info("*** Setting mobility paths\n")
    net.setMobilityModel(time=0, model='RandomDirection',
                         max_x=400, max_y=400, seed=10)

    
    info("*** Creating links\n")
    protocols = ['babel', 'batman_adv', 'batmand', 'olsrd', 'olsrd2']
    kwargs = {}
    for proto in args:
        if proto in protocols:
            kwargs['proto'] = proto

    net.addLink(sta1, cls=adhoc, intf='sta1-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta2, cls=adhoc, intf='sta2-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                **kwargs)
    net.addLink(sta3, cls=adhoc, intf='sta3-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_cap='HT40+', **kwargs)
    net.addLink(sta4, cls=adhoc, intf='sta4-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_Cap='HT40+', **kwargs)
    net.addLink(espiao, cls=adhoc, intf='espiao-wlan0',
                ssid='adhocNet', mode='g', channel=5,
                ht_Cap='HT40+', **kwargs)


    info("*** Starting network\n")
    net.build()

    info("\n*** Addressing...\n")
    if 'proto' not in kwargs:
        sta1.setIP6('2001::1/64', intf="sta1-wlan0")
        sta2.setIP6('2001::2/64', intf="sta2-wlan0")
        sta3.setIP6('2001::3/64', intf="sta3-wlan0")
        sta4.setIP6('2001::4/64', intf="sta4-wlan0")
        espiao.setIP6('2001::5/64', intf="espiao-wlan0")

    info("*** Searching for spy\n")

    for sta in [sta1, sta2, sta3, sta4, espiao]:
        sta.cmd('sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=0')
    
    make_term(sta1,sta2,sta3,sta4)

    CLI(net)
    info("\n*** Stopping network")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology(sys.argv)