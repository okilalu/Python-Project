import hashlib
import json
import time


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def add_block(self, data):
        index = len(self.chain)
        previous_hash = self.chain[-1].hash
        new_block = Block(index, time.time(), data, previous_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


# Initialize the blockchain
blockchain = Blockchain()

# Add blocks to the blockchain
blockchain.add_block("Sensor data 1")
blockchain.add_block("Sensor data 2")
blockchain.add_block("Sensor data 3")

# Print the contents of the blockchain
for block in blockchain.chain:
    print("Block Index:", block.index)
    print("Block Timestamp:", block.timestamp)
    print("Block Data:", block.data)
    print("Block Hash:", block.hash)
    print("Block Previous Hash:", block.previous_hash)
    print()
