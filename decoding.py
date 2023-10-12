import numpy as np
import math
import utils
import encoder
TERM = 0xfd
IDLE = 0x07

def unscrambler(block: np.ndarray) -> None:
    seed = np.ones(58, dtype=np.int8)

    for i in range(0, block.size):
        s38 = int(seed[38])
        s57 = int(seed[57])
        res = s38 ^ s57
        block[i] = res ^ int(block[i])
        utils.shift_left_bits(seed, block[i])

def XGMII_remove_terminate(block: np.ndarray) -> np.ndarray:
    output = np.zeros(64, dtype=np.int8)

    def is_terminate(blk, start_byte):
        return all(blk[8 * start_byte: 8 * start_byte + 8] == TERM)

    if is_terminate(block, 2):
        output = block[8:16]
    elif is_terminate(block, 3):
        output = block[8:24]
    elif is_terminate(block, 4):
        output = block[8:32]
    elif is_terminate(block, 5):
        output = block[8:40]
    elif is_terminate(block, 6):
        output = block[8:48]
    elif is_terminate(block, 7):
        output = block[8:56]
    elif is_terminate(block, 8):
        output = block[8:64]
    elif is_terminate(block, 9):
        output = block[8:72]    
    else:
        raise ValueError("Invalid XGMII termination")

    return output

def unencoder(encoded_data: np.ndarray) -> np.ndarray:
    decoded_data = np.array([], dtype=np.int8)

    for i in range(0, len(encoded_data), 66):
        block = encoded_data[i:i + 66]
        unscrambler(block)
        block = XGMII_remove_terminate(block)
        decoded_data = np.append(decoded_data, block)

    return decoded_data

def main():
    encoded_data = np.array([1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0])
    decoded_data = unencoder(encoded_data)
    print(decoded_data)

if __name__ == "__main__":
    main()
