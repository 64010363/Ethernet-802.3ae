import numpy as np
import utils
import crc

def remove_first_64_bits(frame: np.ndarray) -> np.ndarray:
    if frame.size <= 64:
        raise ValueError("Input array size should be greater than 64 bits")
    
    return frame[64:]

# def Check_CRC(Check)
#     checksum1 = Check[-32:]
#     checksum2 = crc.crc_gen(Check)
    
def remove_dest_src_length(frame: np.ndarray) -> np.ndarray:
    if frame.size < 112:
        raise ValueError("Input array size should be at least 112 bits")

    return frame[112:] 
def main():
    frame = np.array([1, 0, 1, 0, 1, 0, 1, 0] * 7)
    frame2 = np.array([1, 0, 1, 0, 1, 0, 1, 1])
    frame3 = np.random.randint(0, 2, 96)
    data = np.ones(64)
    crc = np.zeros(32)
    frame = np.append(frame, frame2)
    frame = np.append(frame, frame3)
    frame = np.append(frame, data)
    frame = np.append(frame, crc)
    print(frame, frame.size)
    frame_without_first_64_bits = remove_first_64_bits(frame)
    print(frame_without_first_64_bits, frame_without_first_64_bits.size)
    pass

if __name__ == "__main__":
    main()
