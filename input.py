import numpy as np
import matplotlib.pyplot as plt
import noise
import math
import utils
from framing import framing
from encoder import encoder

def package_divider(raw_data:np.ndarray, divide:int) -> np.ndarray:
    n = math.ceil(raw_data.size / divide)
    dest = np.random.randint(0, 2, 48, dtype=np.int8)
    src = np.random.randint(0, 2, 48, dtype=np.int8)
    send_bits = np.array([], dtype=np.int8)

    for i in range(0, n):
        frame = framing(raw_data[divide * i: divide * (i + 1)], dest, src)
        send_bits = np.append(send_bits, frame)
    return send_bits

def transmitter(raw_data:np.ndarray, divide:int) -> np.ndarray:
    n = math.ceil(raw_data.size / divide)
    dest = np.random.randint(0, 2, 48, dtype=np.int8)
    src = np.random.randint(0, 2, 48, dtype=np.int8)
    recieve = np.zeros(raw_data.size, dtype=np.int8)
    rev = np.array([], dtype=np.int8)

    for i in range(0, n):
        data = raw_data[divide * i:divide * (i + 1)]
        frame = framing(data, dest, src)
        code = encoder(frame)
        # signal = gaussian_beam(code)
        # Demodulate
        rev = np.append(rev, code)
    return rev


def main():
    raw = np.random.randint(0, 2, 48, dtype=np.int8)
    res = transmitter(raw, 1280)

if __name__ == "__main__":
    main()
