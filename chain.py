import time
import copy
from block import Block
from transaction import Transaction


class Blockchain:
    def __init__(self, difficulty, blocks_list=[], block_reward=50):
        self.chain = []
        for elem in blocks_list:
            block = Block(elem["index"],
                          elem["previous_hash"],
                          elem["nonce"],
                          elem["timestamp"],
                          elem["transactions"],
                          elem["hashval"],
                          elem["miner"])
            self.chain.append(block)
        self.tx_pool = []
        self.difficulty = difficulty
        self.block_reward = block_reward

    def create_genesis_block(self):
        # Manually construct the first block
        block = Block(0, "")
        new_tx = Transaction("network",
                             "me",
                             self.block_reward,
                             time.time())
        block.add_transaction(new_tx)
        nonce = block.mine(self.difficulty)
        self.chain.append(block)

    def mine_block(self):
        last_block = self.chain[-1]
        index = last_block.index + 1
        previous_hash = last_block.hashval
        block = Block(index, previous_hash)
        for elem in self.tx_pool:
            block.add_transaction(elem)
        self.tx_pool.clear()
        new_tx = Transaction("network",
                             "me",
                             self.block_reward,
                             time.time())
        block.add_transaction(new_tx)
        nonce = block.mine(self.difficulty)
        self.chain.append(block)

    def add_block(self, block):
        last_block = self.chain[-1]
        if(block.timestamp < last_block.timestamp):
            print("Timestamp received"+str(block.timestamp))
            print("Timestamp last block"+str(last_block.timestamp))
            raise ValueError(
                "Error timestamp is before timestamp of last block")
        if(block.index != last_block.index+1):
            print("index received"+str(block.index))
            print("index expected"+str(last_block.index+1))
            raise ValueError("Error in indexing")
        if(block.previous_hash != last_block.hashval):
            print("Previous hash received"+str(block.previous_hash))
            print("Previous hash expected"+str(last_block.hashval))
            raise ValueError("block not aligned in the chain")
        if(block.verify(block.nonce) != True):
            raise ValueError("block not valid")
        self.chain.append(block)

    def add_transaction(self, sender, receiver, amount):
        transaction = Transaction(sender,
                                  receiver,
                                  amount,
                                  time.time())
        self.tx_pool.append(transaction)

    def verify(self):
        for elem in self.chain:
            if(elem.verify() == False):
                return False
        return True

    def to_dict(self):
        chain_dict = []
        for elem in self.chain:
            chain_dict.append(elem.to_dict())
        return chain_dict