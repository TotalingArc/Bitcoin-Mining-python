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
