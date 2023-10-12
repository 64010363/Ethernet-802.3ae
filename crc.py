import numpy as np
import utils

def crc_gen(pkg:np.ndarray, msb:int, lsb:int) -> np.ndarray:
    seed = np.ones(32, dtype=np.int8)
    
    for i in reversed(range(msb, lsb)):
        # Save Bit before shifting
        x32:int = int(seed[31])
        x26:int = int(seed[26])
        x23:int = int(seed[23])
        x22:int = int(seed[22])
        x16:int = int(seed[16])
        x12:int = int(seed[12])
        x11:int = int(seed[11])
        x10:int = int(seed[10])
        x8:int = int(seed[8])
        x7:int = int(seed[7])
        x5:int = int(seed[5])
        x4:int = int(seed[4])
        x2:int = int(seed[2])
        x1:int = int(seed[1])
        x0:int = int(seed[0])

        # Shifting
        utils.shift_left_bits(seed, pkg[i])

        # XOR and put to seed
        seed[27] = x26 ^ x32
        seed[24] = x23 ^ x32
        seed[23] = x22 ^ x32
        seed[17] = x16 ^ x32
        seed[13] = x12 ^ x32
        seed[12] = x11 ^ x32
        seed[11] = x10 ^ x32
        seed[9] = x8 ^ x32
        seed[8] = x7 ^ x32
        seed[6] = x5 ^ x32
        seed[5] = x4 ^ x32
        seed[3] = x2 ^ x32
        seed[2] = x1 ^ x32
        seed[1] = x0 ^ x32

    return seed

def main():
    # y = np.array([1,0,1,1,0,0,1,0])
    # print(y)
    # shift_left_bits(y, 1)
    # print(y)
    # shift_left_bits(y, 0)
    # print(y)
    # shift_left_bits(y, 1)
    # print(y)
    x = np.array([1, 1, 0, 1, 0, 1, 0, 1] * 64)
    print(crc_gen(x, 0, 64 * 8))
    pass

if __name__ == "__main__":
    main()