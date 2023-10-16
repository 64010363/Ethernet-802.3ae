import numpy as np
import math
import utils

def check_idle(block:np.ndarray, start:int) -> bool:
    if block.size <= start:
        return True
    for i in range(start, block.size, 8):
        val = utils.read_byte(block, i, i+7)
        if val != utils.IDLE:
            return False
    return True

def XGMII_to_bit_field(block:np.ndarray) -> (np.ndarray, bool):
    if block.size > 64:
        raise ValueError(f"XMGII_to_bit_field error (more than 64) -> ({block.size})")
    
    if check_idle(block, 0) == True:
        type = utils.create_bits(0x1e, 8)
        term = utils.create_bits(0, 56)
        return np.append(type, term), False
    
    output = np.array([], dtype=np.int8)
    for i in range(0, block.size, 8):
        val = utils.read_byte(block, i, i+7)
        if val == utils.TERM:
            if check_idle(block, i+8) == True:
                match i:
                    case 0:
                        type = utils.create_bits(0x87, 8)
                        term = utils.create_bits(0, 56)
                        return np.append(type, term), False
                    case 8:
                        type = utils.create_bits(0x99, 8)
                        type = np.append(type, block[0:8])
                        term = utils.create_bits(0, 48)
                        return np.append(type, term), False
                    case 16:
                        type = utils.create_bits(0xaa, 8)
                        type = np.append(type, block[0:16])
                        term = utils.create_bits(0, 40)
                        return np.append(type, term), False
                    case 24:
                        type = utils.create_bits(0xb4, 8)
                        type = np.append(type, block[0:24])
                        term = utils.create_bits(0, 32)
                        return np.append(type, term), False
                    case 32:
                        type = utils.create_bits(0xcc, 8)
                        type = np.append(type, block[0:32])
                        term = utils.create_bits(0, 24)
                        return np.append(type, term), False
                    case 40:
                        type = utils.create_bits(0xd2, 8)
                        type = np.append(type, block[0:40])
                        term = utils.create_bits(0, 16)
                        return np.append(type, term), False
                    case 48:
                        type = utils.create_bits(0xe1, 8)
                        type = np.append(type, block[0:48])
                        term = utils.create_bits(0, 8)
                        return np.append(type, term), False
                    case 56:
                        type = utils.create_bits(0xff, 8)
                        return np.append(type, block[0:56]), False
                    case _:
                        raise ValueError(f"XMGII_to_bit_field error :({i})")
    return np.append(output, block), True


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
        block, isHeader = XGMII_to_bit_field(package[i:i+64])
        scrambler(block)
        if isHeader:
            header = np.array([0, 1])
        else:
            header = np.array([1, 0])
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