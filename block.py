import hashlib
import time
from transaction import Transaction
from key import verify_signature


class Block:
    def __init__(self, blockNumber:int, lastHash:str, timestamp=0) -> None:
        self.transactionList : list[Transaction] = []
        self.blockNumber = blockNumber
        self.minerName = ""
        self.timestamp = timestamp
        self.last_hash = lastHash
        self.hashval = ""
        self.nonce = 0

    def __repr__(self) -> str:
        string = "Block id: " + str(self.blockNumber) + "\n" + \
            "prev hash: " + self.last_hash + "\n" + \
            "hash: " + self.hashval + "\n" + \
            "Miner: " + self.minerName + "\n" +\
            "Nonce: " + str(self.nonce) + "\n"
        return string

    def add_transaction(self,transaction:Transaction) -> None:
        self.transactionList.append(transaction)

    def hash_func(self):

        sha = hashlib.sha256()
        data = ""
        data  = str(self.blockNumber) + str(self.nonce) + str(self.last_hash)
        for elem in self.transactionList:
            data+= str(elem.sender) + str(elem.receiver) + str(elem.amount)
        sha.update(data.encode())

        return sha.hexdigest()

    def check_hash(self, hash:str, difficulty = 0):
        return hash.startswith("0" * difficulty)

    def verify(self):
        return self.hashval == self.hash_func()       
    

    def mine(self, difficulty:int):
        
        self.timestamp = time.time()

        while not self.check_hash(self.hash_func(),difficulty):
            self.nonce += 1
        
        self.minerName = "Antoine"
        self.hashval = self.hash_func()   
        

