import numpy as np
import math
import utils

def scrambler(block:np.ndarray) -> None:
    seed = np.ones(58, dtype=np.int8)

    for i in range(0, block.size):
        s38 = int(seed[38])
        s57 = int(seed[57])
        res = s38 ^ s57
        block[i] = res ^ int(block[i])
        utils.shift_left_bits(seed, block[i])

def encoder(package:np.ndarray) -> np.ndarray:
    code = np.array([], dtype=np.int8)

    for i in range(0, package.size, 64):
        block = np.array(package[i:i+64])
        scrambler(block)
        header = np.array([0, 1])
        block = np.append(header, block)
        code = np.append(code, block)
    return code



def main():
    _term = [1, 1, 1, 1, 1, 1, 0, 1]
    _idle = [0, 0, 0, 0, 0, 1, 1, 1]
    byte1 = np.array([0, 0, 0, 0, 0, 0, 0, 1] * 14 + 1 * _term + _idle * 1)
    res = encoder(byte1)
    print(res)

if __name__ == "__main__":
    main()