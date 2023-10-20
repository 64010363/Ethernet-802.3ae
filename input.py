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

# def plot_data(data):
#     t = np.arange(0, data.size, 1/10)
#     sig = np.array([])
#     for bit in data:
#         if bit == 0:
#             sig = np.append(sig, np.array([0] * 10))
#         else:
#             sig = np.append(sig, np.array([1] * 10))
#     plt.plot(t[0:320], sig[0:320])
#     plt.xlabel("Time (x100 ps)")
#     plt.ylabel("Amplitude (V)")
#     plt.title("Data 32-bits")
#     plt.show()

# def plot_encode(code):
#     t = np.arange(0, code.size, 1/10)
#     sig = np.array([])
#     for bit in code:
#         if bit == 0:
#             sig = np.append(sig, np.array([0] * 10))
#         else:
#             sig = np.append(sig, np.array([1] * 10))
#     plt.plot(t[0:320], sig[0:320])
#     plt.xlabel("Time (x100 ps)")
#     plt.ylabel("Amplitude (V)")
#     plt.title("64/66B Encoded Data 32-bits")
#     plt.show()

# def plot_signal(signal):
#     t = np.arange(0, signal.size / (10 ** 6), 10 ** -6)
#     plt.plot(t[0:-1], signal)
#     plt.xlabel("Time (us)")
#     plt.ylabel("Amplitude (V)")
#     plt.title("Ethernet Signal")
#     plt.show()


def transmitter(raw_data:np.ndarray, dest:np.ndarray, src:np.ndarray, divide:int, SNRdB:int) -> (np.ndarray, int, int):
    rev = np.array([], dtype=np.int8)
    recieve_pkg = 0

    for i in range(0, raw_data.size, divide):
        data = raw_data[i:i+divide]
        frame = framing(data, dest, src)

        code = encoder(frame)
        size = code.size

        # xt = ASK(code)
        xt = ASK(code, amplitude=1, frequency=1, sample_rate=10000, duration=1)
        rt = noise.noise(xt, SNRdB)

        a_hat = demodulation(rt, size)
        frame2 = decoder(a_hat)

        data2, val = deframing(frame2)
        recieve_pkg += val
        err_bit = sum(data != data2[0:data.size])
        
        rev = np.append(rev, data2[0:data.size])
    # plot_data(data)
    plt.plot(rt)
    plt.show()
    # plot_encode(code)
    # plot_signal(xt)
    # print(xt)
    # plt.plot(xt)
    
    # plt.plot(a_hat)
    # plt.show()
    BER = err_bit / raw_data.size
    return rev, BER, recieve_pkg

def BER_calculate(SNRdB:int) -> np.ndarray:
    np.random.seed(11)
    dest = np.random.randint(0, 2, 48, dtype=np.int8)
    src = np.random.randint(0, 2, 48, dtype=np.int8)
    raw = np.random.randint(0, 2, 8 * 46, dtype=np.int8)
    res, BER, recive = transmitter(raw, dest, src, 184, SNRdB)
    print("BER = ", BER)
    print("package recieve = ", recive)
def main():
    BER_calculate(0)
    # np.random.seed(69)
    # dest = np.random.randint(0, 2, 48, dtype=np.int8)
    # src = np.random.randint(0, 2, 48, dtype=np.int8)
    # raw = np.random.randint(0, 2, 8 * 500, dtype=np.int8)
    # res, BER, recive = transmitter(raw, dest, src, 512, -50)
    # print("BER = ", BER)
    # print("package receive = ", recive)

    # # Plot the decoder's output
    # plt.figure()
    # plt.subplot(2, 1, 1)
    # plt.plot(raw[:320], label="Original Data")
    # plt.legend()
    # plt.title("Original Data vs. Decoded Data")

    # plt.subplot(2, 1, 2)
    # plt.plot(res[:320], label="Decoded Data")
    # plt.legend()

    # plt.show()
if __name__ == "__main__":
    main()
