import numpy as np
import utils

def data_length(data:np.ndarray) -> np.ndarray:
    digit = 15
    size = data.size
    length = np.zeros(16, dtype=np.int8)
    
    while size != 0:
        length[digit] = size & 1
        digit -= 1
        size = size >> 1
    return length
        
def crc_system(frame:np.ndarray, start:int, end:int) -> np.ndarray:
    checksum = np.zeros(48, dtype=np.int8)
    return checksum

def framing(data:np.ndarray, dest:np.ndarray, src:np.ndarray) -> np.ndarray:
    premable = np.array([1,0,1,0,1,0,1,0] * 7, dtype=np.int8)
    sfd = np.array([1,0,1,0,1,0,1,1], dtype=np.int8)
    length = data_length(data)
    frame = np.zeros(56 + 8 + 48 + 48 + 16 + data.size + 24, dtype=np.int8)
    
    utils.copy_bits(frame, 0, 55, premable)
    utils.copy_bits(frame, 56, 63, sfd)
    utils.copy_bits(frame, 64, 111, dest)
    utils.copy_bits(frame, 112, 159, src)
    utils.copy_bits(frame, 160, 161, length)
    utils.copy_bits(frame, 162, 162 + data.size - 1, data)
    
    crc = crc_system(frame, 162 + data.size, 162 + data.size + 48)
    return frame

def main():
    byte = np.array([0] * 255)
    print(framing(byte, np.array([1, 1] * 24), np.array([0, 1] * 24)))
    pass

if __name__ == "__main__":
    main()
