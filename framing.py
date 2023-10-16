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

def XGMII_terminate(data:np.ndarray) -> np.ndarray:
    block = np.array(data, dtype=np.int8)
    
    # Make Control bits
    term = utils.create_bits(utils.TERM, 8)
    idle = utils.create_bits(utils.IDLE, 8)
    
    # Put Bits here
    block = np.append(block, term)
    while block.size <= 46:
        block = np.append(block, idle)
    return block

def framing(data:np.ndarray, dest:np.ndarray, src:np.ndarray) -> np.ndarray:
    # Error Handling
    if (data.size < 46):
        data = XGMII_terminate(data)
    
    # Generate Frame's Bits
    premable = np.array([1,0,1,0,1,0,1,0] * 7, dtype=np.int8)
    sfd = np.array([1,0,1,0,1,0,1,1], dtype=np.int8)
    length = data_length(data)
    frame = np.zeros(56 + 8 + 48 + 48 + 16 + data.size + 32, dtype=np.int8)

    # Put bit here
    utils.copy_bits(frame, 0, 55, premable)
    utils.copy_bits(frame, 56, 63, sfd)
    utils.copy_bits(frame, 64, 111, dest)
    utils.copy_bits(frame, 112, 159, src)
    utils.copy_bits(frame, 160, 175, length)
    utils.copy_bits(frame, 175, 175 + data.size - 1, data)
    
    # Calculate CRC
    crc = crc_gen(frame, 64, 175 + data.size - 1)
    utils.copy_bits(frame, 175 + data.size, 175 + data.size + 31, crc)
    return frame

def main():
    byte = np.array([0] * 30)
    print(framing(byte, np.array([1, 1] * 24), np.array([0, 1] * 24)))
    pass

if __name__ == "__main__":
    main()
