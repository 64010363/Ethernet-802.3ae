import numpy as np
import noise
import math
import utils
from framing import framing
from deframing import deframing
from encoder import encoder
from decoder import decoder
from modulation import ASK
from correlator import demodulation

def transmitter(raw_data:np.ndarray, divide:int) -> np.ndarray:
    dest = np.random.randint(0, 2, 48, dtype=np.int8)
    src = np.random.randint(0, 2, 48, dtype=np.int8)
    rev = np.array([], dtype=np.int8)
    recieve_pkg = 0

    for i in range(0, raw_data.size, divide):
        data = raw_data[i:i+divide]
        frame = framing(data, dest, src)
        code = encoder(frame)
        size = code.size
        xt = ASK(code)
        rt = xt
        a_hat = demodulation(rt, size)
        frame2 = decoder(a_hat)
        data2, val = deframing(frame2)
        print("err = ", sum(data != data2))
        recieve_pkg += val
        rev = np.append(rev, data)
    print("recieve = ", recieve_pkg)
    return rev


def main():
    raw = np.random.randint(0, 2, 48, dtype=np.int8)
    res = transmitter(raw, 1280)

if __name__ == "__main__":
    main()
