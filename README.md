# Simulação de Rede FANET com Detecção de Intrusos

Este repositório contém dois scripts em Python para simulação de uma rede FANET (Flying Ad Hoc Network) utilizando o Mininet-WiFi. O objetivo é detectar intrusos em uma área monitorada por drones e avaliar o impacto de ataques de jamming.

## Funcionalidades

1. **Configuração de Rede FANET**:
   - Criação de quatro drones vigilantes que patrulham uma área delimitada.
   - Um intruso tenta acessar a região protegida (coordenadas entre `(100,100)` e `(300,300)`).

2. **Missão de Detecção**:
   - Os drones utilizam pacotes ICMP (ping) para localizar o intruso.
   - A localização e o tempo de detecção do intruso são registrados.

3. **Simulação de Ataque de Jamming**:
   - Utilizando a flag `-at`, o intruso executa um ataque de jamming, comprometendo o tempo de detecção e gerando mensagens maliciosas no arquivo de saída.

## Requisitos

- **Sistema Operacional**: Linux
- **Mininet-WiFi**: Certifique-se de que o Mininet-WiFi esteja corretamente instalado no sistema. Consulte a [documentação oficial](https://github.com/intrig-unicamp/mininet-wifi) para instruções de instalação.
- **Python 3**: Necessário para executar os scripts.

## Arquivos

1. `mininet-wifi.py`: Configura a rede FANET e simula o cenário básico de detecção de intrusos.
2. `broadcasting.py`: Simula o broadcasting da rede, incluindo a interação entre drones e o intruso.

## Como Rodar

### Etapa 1: Configurar o Ambiente

Certifique-se de estar no ambiente do Mininet-WiFi. Caso contrário, inicie-o com:

```bash
sudo mn -c
sudo mn-wifi
```

### Etapa 2: Executar o Script

#### Cenário Normal (Sem Ataque):
Para rodar a simulação sem ataque:

```bash
sudo python3 mininet-wifi.py
```

#### Cenário com Ataque (Jamming):
Para rodar a simulação com o ataque do intruso:

```bash
sudo python3 mininet-wifi.py -at
```

#### Simulação de Broadcasting:
Para executar o script de broadcasting:

```bash
sudo python3 broadcasting.py
```

### Etapa 3: Analisar os Resultados

- Durante a execução, o console exibira:
  - O tempo de detecção do intruso.
  - A localização do intruso no momento da detecção.

- O arquivo de saída (`arquivo_de_saida`) será gerado contendo as mensagens relacionadas à detecção.

## Parâmetros do Script

- `-at`: Ativa o ataque de jamming pelo intruso, comprometendo o arquivo de saída e aumentando o tempo de detecção.
- Sem flag: O intruso é detectado normalmente, e a missão ocorre sem interferências.

## Notas

- **Performance**: O impacto do ataque pode ser analisado comparando os tempos de detecção com e sem a flag `-at`.
- **Logs**: Certifique-se de verificar os logs para mais detalhes sobre o comportamento da rede durante a simulação.

## Contribuições

Contribuições são bem-vindas! Para reportar problemas ou sugerir melhorias, por favor, envie um pull request ou abra uma issue neste repositório.
