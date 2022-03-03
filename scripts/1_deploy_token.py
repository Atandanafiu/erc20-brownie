from brownie import MyToken, network, accounts, web3
from scripts import helpfu_scripts
from web3 import Web3

initial_supply = web3.toWei(4000000000000, "ether")


def main():
    account = helpfu_scripts.get_account()
    my_token = MyToken.deploy(initial_supply, {"from": account})
    print(my_token.name())
