import numpy as np

TERM = 0xfd
IDLE = 0x07

def copy_bits(frame:np.ndarray, start:int, end:int, src:np.ndarray) -> None:
    j = 0
    for i in range(start, end+1):
        frame[i] = src[j]
        j += 1

def write_byte(block:np.ndarray, val:int, start:int, end:int) -> None:
    j = 1
    for i in reversed(range(start, end+1)):
        block[i] = (val & j != 0)
        j = j << 1
        
def dec(x, y):
    def test(func):
        def inner(*args, **kwargs):
            print("HEE")
            func(*args, **kwargs)
        return inner
    return test