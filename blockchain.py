import datetime
import hashlib
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash):  # FIXED: __init__
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # FIXED: use __dict__ instead of _dict_
        block_string = json.dumps(self.__dict__, sort_keys=True, default=str)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):  # FIXED: __init__
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        block = Block(len(self.chain), datetime.datetime.now(), data, previous_hash)
        self.chain.append(block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash() or curr.previous_hash != prev.hash:
                return False
        return True
