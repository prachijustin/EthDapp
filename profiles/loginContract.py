import json
from profiles.web3s import web3


abi = json.loads('[{"constant":false,"inputs":[{"name":"secondary","type":"string"},{"name":"primary","type":"address"}],"name":"mapAddress","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"secondary","type":"string"}],"name":"checkAddress","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"primaryToSecondary","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"primary","type":"address"},{"indexed":false,"name":"secondary","type":"string"}],"name":"AddressMapped","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"code","type":"uint256"},{"indexed":false,"name":"sender","type":"address"}],"name":"Error","type":"event"}]')

address = '0xEeA53F8a6F800012F3f09AfB0bBedEa554641F91'

contract = web3.eth.contract(address=address, abi=abi)


	# mapped = contract.functions.mapAddress().call()
