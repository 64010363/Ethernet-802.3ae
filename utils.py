import numpy as np

TERM = 0xfd
IDLE = 0x07
CRC = 0b00000100_11000001_00011101_10110111
CRC_INIT = 0xFFFFFFFF
CRC_MSB = 0x4C11DB7
CRC_LSB = 0xEDB88320

def copy_bits(frame:np.ndarray, start:int, end:int, src:np.ndarray) -> None:
    # frame[start:end+1] = src
    j = 0
    for i in range(start, end+1):
        frame[i] = src[j]
        j += 1

def write_byte(block:np.ndarray, val:int, start:int, end:int) -> None:
    j = 1
    for i in reversed(range(start, end+1)):
        block[i] = (val & j != 0)
        j = j << 1

def shift_left_bits(seed:np.ndarray, msg_bit:int) -> None:
    num = 0
    digit = 0

    for i in reversed(range(0, seed.size)):
        num += int(seed[i]) << digit
        digit += 1
    num <<= 1

    digit = 1
    for i in reversed(range(0, seed.size)):
        seed[i] = int(num & digit != 0)
        digit <<= 1
    seed[-1] = msg_bit
        
def dec(x, y):
    def test(func):
        def inner(*args, **kwargs):
            print("HEE")
            func(*args, **kwargs)
        return inner
    return test

def main():
    raw = np.array([0] * 64)
    src = np.array([1] * 16)
    copy_bits(raw, 5, 20, src)
    print(raw)
    print(bin(69)[0])

if __name__ == "__main__":
    main()