import numpy as np
import math
import utils
from framing import framing
from encoder import encoder
from modulation import gaussian_beam
import matplotlib.pyplot as plt

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
    # raw = np.random.randint(0, 2, 1920 * 1080 * 8 * 4, dtype=np.int8)
    # wtf = np.random.randint(0, 2, 1920 * 1080 * 8 * 4, dtype=np.int8)
    # utils.copy_bits(raw, 0, wtf.size-1, wtf)
    # print(raw)
    # raw = np.array([], dtype=np.int8)
    # wtf2 = np.append(raw, wtf)
    # print(wtf2)
    raw = np.random.randint(0, 2, 48, dtype=np.int8)
    res = transmitter(raw, 1280)
    # print(transmitter(raw, 128).size)
    # samp = np.array([])
    # for i in range(0, res.size):
    #     if res[i] == 1:
    #         q = np.array([1] * 50)
    #     else:
    #         q = np.array([0] * 50)
    #     samp = np.append(samp, q)
    # plt.plot(samp)
    # plt.show()
    # raw = np.array([])
    # for i in range(0, 1000):
    #     raw = np.append(raw, np.array([0] * 1280))

if __name__ == "__main__":
    main()
