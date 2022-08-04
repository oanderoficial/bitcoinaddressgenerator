from bitcoinaddress import Wallet
from clint.textui import colored

print(colored.yellow("""

  ____  _ _            _          ____                           _             
 | __ )(_) |_ ___ ___ (_)_ __    / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  _ \| | __/ __/ _ \| | '_ \  | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |_) | | || (_| (_) | | | | | | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
 |____/|_|\__\___\___/|_|_| |_|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                                                                       
       Por: @oanderoficial | Bitcoin Address Generator | 2021
        """))

carteira = Wallet()
print(carteira)
print(carteira.key.__dict__['mainnet'].__dict__)
print(carteira.key.__dict__['testnet'].__dict__)


