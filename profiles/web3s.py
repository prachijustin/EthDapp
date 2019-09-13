from web3 import Web3
import json
from web3.auto import w3
from eth_account.messages import encode_defunct

#LOCALHOST-------------
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))


print(web3.isConnected())
print(web3.eth.blockNumber)

balance = web3.eth.getBalance(web3.eth.accounts[0])
print(balance)

abi = json.loads('[{"constant":false,"inputs":[{"name":"secondary","type":"string"},{"name":"primary","type":"address"}],"name":"mapAddress","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"primary","type":"address"},{"indexed":false,"name":"secondary","type":"string"}],"name":"AddressMapped","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"code","type":"uint256"},{"indexed":false,"name":"sender","type":"address"}],"name":"Error","type":"event"},{"constant":true,"inputs":[{"name":"secondary","type":"string"}],"name":"checkAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"primaryToSecondary","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')

address = web3.toChecksumAddress('0xf6B65DF051154ca83B603F826faAcd29856dC8aE')

contract = web3.eth.contract(address=address, abi=abi)



print(web3.geth.admin.datadir())


#RINKBEY-------------------------------

# web3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/2456d9f27cfd4dc5966e1650bd54af95"))

# print(web3.isConnected())

# print(web3.eth.blockNumber)

# balance = web3.eth.getBalance('0xb837845fFeBdd710A30d7d803Fd3a017aF6FdeCA')


# print(balance)
# abi = json.loads('[{"constant":false,"inputs":[{"name":"secondary","type":"string"},{"name":"primary","type":"address"}],"name":"mapAddress","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"primary","type":"address"},{"indexed":false,"name":"secondary","type":"string"}],"name":"AddressMapped","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"code","type":"uint256"},{"indexed":false,"name":"sender","type":"address"}],"name":"Error","type":"event"},{"constant":true,"inputs":[{"name":"secondary","type":"string"}],"name":"checkAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"primaryToSecondary","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"}]')

# address = web3.toChecksumAddress('0x7efe60e1cad16a8754d524d55b2f8166abde97a5')

# contract = web3.eth.contract(address=address, abi=abi)

