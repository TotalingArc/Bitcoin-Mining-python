import logging
import time
from hashlib import sha256

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def sha256_hash(text):
    """Compute SHA-256 hash of the given text."""
    return sha256(text.encode("ascii")).hexdigest()

def mine_block(block_number, transactions, previous_hash, difficulty):
    """Mine a new block with the specified parameters."""
    prefix_str = '0' * difficulty
    prefix_zeros = '0' * difficulty
    nonce = 0

    while True:
        text = str(block_number) + str(transactions) + previous_hash + str(nonce)
        new_hash = sha256_hash(text)
        
        if new_hash.startswith(prefix_str):
            logger.info(f"Successfully mined block {block_number} with nonce value: {nonce}")
            return new_hash, nonce

        nonce += 1
        if nonce % 100000 == 0:
            logger.debug(f"Current nonce: {nonce}")

def main():
    transactions = [
        {"from": "Dhaval", "to": "Bhavin", "amount": 20},
        {"from": "Mando", "to": "Cara", "amount": 45}
    ]
    previous_hash = '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7'
    difficulty = 4

    start_time = time.time()
    logger.info("Start mining")
    new_hash, nonce = mine_block(5, transactions, previous_hash, difficulty)
    end_time = time.time()

    total_time = end_time - start_time
    logger.info(f"End mining. Mining took: {total_time} seconds")
    logger.info(f"New block hash: {new_hash}")

if __name__ == '__main__':
    main()
