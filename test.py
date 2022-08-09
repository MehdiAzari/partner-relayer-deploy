from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider('http://localhost:8080'))
print ("Latest Ethereum block number by bitex relayer" , w3.eth.blockNumber)

pw3 = Web3(HTTPProvider('https://testnet.aurora.dev'))
print ("Latest Ethereum block number by public testnet" , pw3.eth.blockNumber)
diff = pw3.eth.blockNumber - w3.eth.blockNumber 
print("Our relaye is", diff ," blocks behind")
delay = 1.0526 * diff
print("Considering avg time 1.0526s we are", delay, "behind",delay/60,'m', delay/360,"h",delay/(360*24),"day")
