import numpy as np

def dec(x, y):
    def test(func):
        def inner(*args, **kwargs):
            print("HEE")
            func(*args, **kwargs)
        return inner
    return test

def data_length(data:np.ndarray) -> np.ndarray:
    digit = 15
    size = data.size
    length = np.zeros(16, dtype=np.int8)
    
    while size != 0:
        length[digit] = size & 1
        digit -= 1
        size = size >> 1
    return length

def copy_bits(frame:np.ndarray, start:int, end:int, src:np.ndarray) -> None:
    j = 0
    for i in range(start, end+1):
        frame[i] = src[j]
        j += 1
        
def crc(frame:np.ndarray, start:int, end:int) -> np.ndarray:
    checksum = np.zeros(48, dtype=np.int8)
    pass

def framing(data:np.ndarray, dest:np.ndarray, src:np.ndarray) -> np.ndarray:
    premable = np.array([1,0,1,0,1,0,1,0] * 7, dtype=np.int8)
    sfd = np.array([1,0,1,0,1,0,1,1], dtype=np.int8)
    length = data_length(data)
    frame = np.zeros(56 + 8 + 48 + 48 + 16 + data.size + 24, dtype=np.int8)
    
    copy_bits(frame, 0, 55, premable)
    copy_bits(frame, 56, 63, sfd)
    copy_bits(frame, 64, 111, dest)
    copy_bits(frame, 112, 159, src)
    copy_bits(frame, 160, 161, length)
    copy_bits(frame, 162, 162 + data.size - 1, data)
    
    crc = None
    return frame

def main():
    byte = np.array([0] * 255)
    print(framing(byte, np.array([1, 1] * 24), np.array([0, 1] * 24)))
    pass

if __name__ == "__main__":
    main()
