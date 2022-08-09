
from web3 import Web3, HTTPProvider
while True:
  w3 = Web3(HTTPProvider('http://localhost:8080'))
  pw3 = Web3(HTTPProvider('https://testnet.aurora.dev'))
  diff = pw3.eth.blockNumber - w3.eth.blockNumber
  delay = 1.0526 * diff
  print("Testnet:",pw3.eth.blockNumber ,"relayer:",w3.eth.blockNumber,"difference:",diff,delay/60,'m', delay/360,"h",delay/(360*24),"day")
