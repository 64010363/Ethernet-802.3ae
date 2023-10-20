# System Module
import numpy as np
import matplotlib.pyplot as plt

def BER_graph():
    SNRdB = (31,32,33,34,35,36,37,38,39,40,41,42)
    BER = np.array([0.03282, 0.03188, 0.03182,0.03030,0.02929,0.02777, 0.026515, 0.02525, 0.02525, 0.02277 ,0.02227,0.02129])
    plt.semilogy(SNRdB, BER)
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
    