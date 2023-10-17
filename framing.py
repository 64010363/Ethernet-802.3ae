import numpy as np
from crc import crc_gen
import utils

def framing(data:np.ndarray, dest:np.ndarray, src:np.ndarray) -> np.ndarray:
    # Error Handling
    size = data.size
    if (size < 64 * 8):
        data = np.append(data, np.zeros(64 * 8 - size))
    
    # Generate Frame's Bits
    premable = np.array([1,0,1,0,1,0,1,0] * 7, dtype=np.int8)
    sfd = np.array([1,0,1,0,1,0,1,1], dtype=np.int8)
    length = utils.create_bits(size // 8, 16)
    # frame = np.array([], dtype=np.int8)
    frame = np.zeros(56 + 8 + 48 + 48 + 16 + data.size + 32, dtype=np.int8)

    # Put bit here
    # frame = np.append(premable, sfd)
    # frame = np.append(frame, dest)
    # frame = np.append(frame, src)
    # frame = np.append(frame, length)
    # frame = np.append(frame, data)

    # Put Bits here
    utils.copy_bits(frame, 0, 55, premable)
    utils.copy_bits(frame, 56, 63, sfd)
    utils.copy_bits(frame, 64, 111, dest)
    utils.copy_bits(frame, 112, 159, src)
    utils.copy_bits(frame, 160, 175, length)
    utils.copy_bits(frame, 176, 176 + data.size - 1, data)
    
    # Calculate CRC
    crc = crc_gen(frame, 64, 176 + data.size - 1)
    utils.copy_bits(frame, 176 + data.size, 176 + data.size + 31, crc)
    return frame

def main():
    byte = np.array([0] * 30)
    print(framing(byte, np.array([1, 1] * 24), np.array([0, 1] * 24)))
    pass

if __name__ == "__main__":
    main()
