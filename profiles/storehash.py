from profiles.web3s import web3
import json

address = web3.toChecksumAddress('0xc694905424ed58226af07d309a1f53b7fdff89bc')

abi = json.loads('[{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"enrollToIPFS","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"enroll","type":"uint256"}],"name":"getHash","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"enroll","type":"uint256"},{"name":"x","type":"string"}],"name":"sendHash","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
ipfsContract = web3.eth.contract(address= address, abi=abi)
