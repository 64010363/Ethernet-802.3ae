import numpy as np
from crc import crc_gen
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

def framing(data:np.ndarray, dest:np.ndarray, src:np.ndarray) -> np.ndarray:
    # frame = np.array([])
    premable = np.array([1,0,1,0,1,0,1,0] * 7, dtype=np.int8)
    sfd = np.array([1,0,1,0,1,0,1,1], dtype=np.int8)
    length = data_length(data)
    frame = np.zeros(56 + 8 + 48 + 48 + 16 + data.size + 32, dtype=np.int8)

    # frame = np.append(frame, premable)
    # frame = np.append(frame, sfd)
    # frame = np.append(frame, dest)
    # frame = np.append(frame, src)
    # frame = np.append(frame, length)
    # frame = np.append(frame, data)

    utils.copy_bits(frame, 0, 55, premable)
    utils.copy_bits(frame, 56, 63, sfd)
    utils.copy_bits(frame, 64, 111, dest)
    utils.copy_bits(frame, 112, 159, src)
    utils.copy_bits(frame, 160, 175, length)
    utils.copy_bits(frame, 175, 175 + data.size - 1, data)
    
    crc = crc_gen(frame, 64, 175 + data.size - 1)
    # print(crc.size)
    # frame = np.append(frame, crc)
    utils.copy_bits(frame, 175 + data.size, 175 + data.size + 31, crc)

    return frame

def main():
    byte = np.array([0] * 255)
    print(framing(byte, np.array([1, 1] * 24), np.array([0, 1] * 24)))
    pass

if __name__ == "__main__":
    main()
