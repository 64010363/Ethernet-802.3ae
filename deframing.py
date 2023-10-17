import numpy as np
import utils
import crc

def remove_sync_header(frame:np.ndarray) -> np.ndarray:
    if frame.size <= 64:
        raise ValueError("Input array size should be greater than 64 bits")
    
    return np.copy(frame[64:])

def check_CRC(package:np.ndarray) -> int:
    checksum1 = package[-32:]
    checksum2 = crc.crc_gen(package, 64, package.size - 33)
    val = sum(checksum1 != checksum2)
    return int(val == 0)
    
def remove_dest_src_mac(frame:np.ndarray) -> np.ndarray:
    if frame.size <= 96:
        raise ValueError("Input array size should be at least 112 bits")

    return np.copy(frame[96:])

def get_length(frame:np.ndarray) -> int:
    return utils.read_byte(frame, 160, 175)

def deframing(frame:np.ndarray) -> (np.ndarray, int):
    val = check_CRC(frame)
    length = utils.read_byte(frame, 160, 175)
    frame = remove_sync_header(frame)
    frame = remove_dest_src_mac(frame)
    frame = frame[16:-32]
    return np.array(frame[0:length * 8]), val

def main():
    pass

if __name__ == "__main__":
    main()
