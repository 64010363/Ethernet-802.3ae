# System Module
import numpy as np
import matplotlib.pyplot as plt

def BER_graph():
    SNRdB = np.arange(-120, 10, 10)
    BER = np.array([0.2587890625, 0.2587890625, 0.259765625, 0.259765625, 0.255859375, 0.255859375, 0.24609375, 0.220703125, 0.08203125, 0, 0, 0, 0])
    plt.semilogy(SNRdB[0:8], BER[0:8])
    plt.xlabel("SNR (dB)")
    plt.ylabel("BER")
    plt.title("BER (Eb/N0) Ethernet802.03ae")
    plt.grid()
    plt.show()

# SNRdb = -120 Ber = 0.2587890625
# SNRdb = -110 Ber = 0.2587890625
# SNRdb = -100 Ber = 0.259765625
# SNRdb = -90 Ber = 0.259765625
# SNRdb = -80 Ber = 0.255859375
# SNRdb = -70 Ber = 0.255859375
# SNRdb = -60 Ber = 0.24609375
# SNRdb = -50 Ber = 0.220703125
# SNRdb = -40 Ber = 0.08203125
# SNRdb = -30 Ber =  0
# SNRdb = -20 Ber =  0
# SNRdb = -10 Ber = 0 
# SNRdb = 0 Ber = 0

def main():
    BER_graph()

if __name__ == "__main__":
    main()