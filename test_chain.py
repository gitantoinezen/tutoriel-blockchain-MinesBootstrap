from chain import Blockchain
from key import BitcoinAccount

wallet = BitcoinAccount()
address = wallet.to_address()
difficulty = 4

blockchain = Blockchain(difficulty)
blockchain.create_genesis_block()

print("blockchain: ")
print(blockchain.to_dict())
print("\n\n\n")

first_block = blockchain.chain[-1]

print("First block: ")
print(first_block)

blockchain.add_transaction(address, "colas", 10)
blockchain.add_transaction(address, "salim", 30)
blockchain.mine_block()

print("blockchain: ")
print(blockchain.to_dict())
print("\n\n\n")
second_block = blockchain.chain[-1]

blockchain.add_transaction(address, "coco", 10)
blockchain.add_transaction(address, "emilie", 30)
blockchain.mine_block()
print("blockchain: ")
print(blockchain.to_dict())

print("Second block: ")
print(second_block)
