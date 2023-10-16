import numpy as np
import math
import utils

def XGMII_terminate(block:np.ndarray) -> np.ndarray:
    output = np.zeros(64, dtype=np.int8)
    
    def put_terminate(blk:np.ndarray, start_byte:int) -> None:
        utils.write_byte(blk, utils.TERM, 8 * start_byte, 8 * start_byte + 7)
        for i in range(start_byte + 1, 8):
            utils.write_byte(blk, utils.IDLE, 8 * i, 8 * i + 7)
    
    match block.size:
        case 8:
            utils.write_byte(output, 0x99, 0, 7)
            utils.copy_bits(output, 8, 15, block)
            put_terminate(output, 2)
        case 16:
            utils.write_byte(output, 0xaa, 0, 7)
            utils.copy_bits(output, 8, 23, block)
            put_terminate(output, 3)
        case 24:
            utils.write_byte(output, 0xb4, 0, 7)
            utils.copy_bits(output, 8, 31, block)
            put_terminate(output, 4)
        case 32:
            utils.write_byte(output, 0xcc, 0, 7)
            utils.copy_bits(output, 8, 39, block)
            put_terminate(output, 5)
        case 40:
            utils.write_byte(output, 0xd2, 0, 7)
            utils.copy_bits(output, 8, 47, block)
            put_terminate(output, 6)
        case 48:
            utils.write_byte(output, 0xe1, 0, 7)
            utils.copy_bits(output, 8, 55, block)
            put_terminate(output, 7)
        case 56:
            utils.write_byte(output, 0xff, 0, 7)
            utils.copy_bits(output, 8, 63, block)
        case _:
            raise ValueError(f"XGMII bit error {block.size}")
    return output

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
    n = math.ceil(package.size / 64)

    for i in range(0, n):
        block = package[64 * i: 64 * (i + 1)]
        if block.size < 64:
            header = np.array([1,0], dtype=np.int8)
            block = XGMII_terminate(block)
        else:
            header = np.array([1,0], dtype=np.int8)
        scrambler(block)
        block = np.append(header, block)
        code = np.append(code, block)
    return code

def main():
    byte = np.array([0] * 8 * 1)
    output = encoder(byte)
    print(output)
    # print(XGMII_terminate(byte))
    # scrambler(byte)
    # print(byte)
    # byte = np.array([0] * 16)
    # print(XGMII_terminate(byte))
    # byte = np.array([0] * 24)
    # print(XGMII_terminate(byte))
    # byte = np.array([0] * 32)
    # print(XGMII_terminate(byte))
    # byte = np.array([0] * 40)
    # print(XGMII_terminate(byte))
    # byte = np.array([0] * 48)
    # print(XGMII_terminate(byte))
    # byte = np.array([0] * 56)
    # print(XGMII_terminate(byte))

if __name__ == "__main__":
    main()