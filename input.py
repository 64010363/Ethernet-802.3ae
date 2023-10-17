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
import matplotlib.pyplot as plt

def transmitter(raw_data:np.ndarray, dest:np.ndarray, src:np.ndarray, divide:int, SNRdB:int) -> (np.ndarray, int, int):
    rev = np.array([], dtype=np.int8)
    recieve_pkg = 0

    for i in range(0, raw_data.size, divide):
        data = raw_data[i:i+divide]
        frame = framing(data, dest, src)

        code = encoder(frame)
        size = code.size

        xt = ASK(code)
        rt = noise.noise(xt, SNRdB)

        a_hat = demodulation(rt, size)
        frame2 = decoder(a_hat)

        data2, val = deframing(frame2)
        recieve_pkg += val
        err_bit = sum(data != data2[0:data.size])
        rev = np.append(rev, data2)
    
    BER = err_bit / raw_data.size
    return rev, BER, recieve_pkg

def BER_calculate(SNRdB:int) -> np.ndarray:
    np.random.seed(69)
    dest = np.random.randint(0, 2, 48, dtype=np.int8)
    src = np.random.randint(0, 2, 48, dtype=np.int8)
    raw = np.random.randint(0, 2, 8 * 100, dtype=np.int8)
    res, BER, recive = transmitter(raw, dest, src, 1280, SNRdB)
    print("BER = ", BER)
    print("package recieve = ", recive)

def main():
    BER_calculate(-45)

if __name__ == "__main__":
    main()
