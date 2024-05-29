# Simple Blockchain Block Miner

This project demonstrates a simple implementation of a blockchain block miner using Python and the SHA-256 hashing algorithm. The goal is to find a nonce that, when combined with the block's data and the previous hash, produces a hash that starts with a specific number of leading zeros, defined by the `difficulty` level.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/block-miner.git
    cd block-miner
    ```

2. **Install dependencies:**

    This script uses only standard Python libraries, so no additional dependencies are required.

3. **Run the script:**

    ```bash
    python miner.py
    ```

## Code Explanation

### `sha256_hash`

This function computes the SHA-256 hash of a given text.

```python
def sha256_hash(text):
    """Compute SHA-256 hash of the given text."""
    return sha256(text.encode("ascii")).hexdigest()

**Mine Block**
This function attempts to mine a new block by finding a nonce such that the SHA-256 hash of the block's content starts with a specific number of leading zeros (difficulty).

```def mine_block(block_number, transactions, previous_hash, difficulty):
    """Mine a new block with the specified parameters."""
    prefix_zeros = '0' * difficulty
    nonce = 0

    while True:
        text = f"{block_number}{transactions}{previous_hash}{nonce}"
        new_hash = sha256_hash(text)
        
        if new_hash.startswith(prefix_zeros):
            logger.info(f"Successfully mined block {block_number} with nonce value: {nonce}")
            return new_hash, nonce

        nonce += 1
        if nonce % 100000 == 0:
            logger.debug(f"Current nonce: {nonce}")
