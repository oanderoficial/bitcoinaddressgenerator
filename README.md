# Bitcoin Address Generator
 Script em Python com o pacote bitcoinaddress, que gera um endereço de carteira Bitcoin. Ele gera uma chave privada em diferentes formatos (hex, wif e wif compactado) e endereços públicos correspondentes, brutos, endereços P2WPKH começando com o prefixo 1, endereços P2SH começando com prefixo 3 como parte de Segwit soft fork e endereços Bech32 com prefixo bc1 P2WPKH e P2WSH.

## Installation

```
pip install bitcoinaddress
pip install colored
pip install clint
```

## code 

```
from bitcoinaddress import Wallet
from clint.textui import colored

print(colored.yellow("""

  ____  _ _            _          ____                           _             
 | __ )(_) |_ ___ ___ (_)_ __    / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  _ \| | __/ __/ _ \| | '_ \  | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |_) | | || (_| (_) | | | | | | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
 |____/|_|\__\___\___/|_|_| |_|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                                                                       
       Por: @bitcoinander | Bitcoin Address Generator | 2021
        """))

carteira = Wallet()
print(carteira)
print(carteira.key.__dict__['mainnet'].__dict__)
print(carteira.key.__dict__['testnet'].__dict__)

```
<img src="https://raw.githubusercontent.com/bitcoinander/bitcoinaddressgenerator/main/img/img.jpg">
