#!/usr/bin/python3

from web3 import Web3, Account
from mnemonic import Mnemonic
from substrateinterface import Keypair
import json
import os

# Enable this feature to use the mnemonic functionality of the Account object
Account.enable_unaudited_hdwallet_features()

def create_eth_wallets(number_of_wallets):
    mnemo = Mnemonic("english")
    eth_wallets = []
    eth_mnemonics = []
    for _ in range(number_of_wallets):
        mnemonic_words = mnemo.generate(strength=128)
        acct = Web3().eth.account.from_mnemonic(mnemonic=mnemonic_words)
        wallet_info = {
            'address': acct.address,
            'private_key': acct.key.hex(),
            'mnemonic': mnemonic_words
        }
        eth_wallets.append(wallet_info)
        eth_mnemonics.append(mnemonic_words)
    return eth_wallets, eth_mnemonics

def create_dot_wallets(number_of_wallets):
    dot_wallets = []
    dot_mnemonics = []
    for _ in range(number_of_wallets):
        keypair = Keypair.create_from_mnemonic(Keypair.generate_mnemonic())
        wallet_info = {
            'address': keypair.ss58_address,
            'mnemonic': keypair.mnemonic
        }
        dot_wallets.append(wallet_info)
        dot_mnemonics.append(keypair.mnemonic)
    return dot_wallets, dot_mnemonics

def main():
    wallet_type = input("Which type of wallets do you want to create? Enter ETH for Ethereum or DOT for Polkadot: ").upper()
    number_of_wallets = int(input("Enter the number of wallets to create (0-999): "))
    
    if 0 <= number_of_wallets <= 999:
        os.makedirs('wallets', exist_ok=True)
        if wallet_type == "ETH":
            eth_wallets, eth_mnemonics = create_eth_wallets(number_of_wallets)
            with open(os.path.join('wallets', 'eth_wallets_info.json'), 'w') as file:
                json.dump(eth_wallets, file, indent=4)
            with open(os.path.join('wallets', 'eth_mnemonics.txt'), 'w') as file:
                for mnemonic in eth_mnemonics:
                    file.write(mnemonic + '\n')
            print(f"{number_of_wallets} ETH wallets have been created and saved to wallets/eth_wallets_info.json and wallets/eth_mnemonics.txt")
        elif wallet_type == "DOT":
            dot_wallets, dot_mnemonics = create_dot_wallets(number_of_wallets)
            with open(os.path.join('wallets', 'dot_wallets_info.json'), 'w') as file:
                json.dump(dot_wallets, file, indent=4)
            with open(os.path.join('wallets', 'dot_mnemonics.txt'), 'w') as file:
                for mnemonic in dot_mnemonics:
                    file.write(mnemonic + '\n')
            print(f"{number_of_wallets} DOT wallets have been created and saved to wallets/dot_wallets_info.json and wallets/dot_mnemonics.txt")
        else:
            print("Invalid wallet type selected. Please enter either ETH for Ethereum or DOT for Polkadot.")
    else:
        print("Invalid number of wallets. Please enter a number between 0 and 999.")

if __name__ == "__main__":
    main()

