import numpy as np
import matplotlib.pyplot as plt

demodulated_data = [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0,
 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0]

# Modify the following parameters as needed
Nbits = len(demodulated_data)  # Number of bits in the demodulated signal
f = 1  # Bit rate (bit duration = 1/f)
Nsamp = int(len(demodulated_data) / Nbits)  # Number of samples per bit

# Create a cosine waveform for correlation
t = np.linspace(0, Nbits / f, Nbits, endpoint=False)  # Time vector
cos_t = np.cos(2 * np.pi * f * t)

# Correlator
z = []
z_tt = []

for i in range(Nbits):
    z_t = np.multiply(demodulated_data[i * Nsamp:(i + 1) * Nsamp], cos_t)
    z_t_out = np.sum(z_t)
    z_tt.extend(z_t)
    z.append(z_t_out)

# Plot the results
plt.figure(1)
plt.plot(z_tt)  # r(t) * cos for all time
plt.stem(z)  # Correlation output
plt.title('Correlation Output')
plt.grid(True)

# Make a decision (bit detection)
a_hat = []
for zdata in z:
    if zdata > 0:
        a_hat.append(1)
    else:
        a_hat.append(0)

# Plot the detected bits
plt.figure(2)
plt.stem(a_hat)
plt.title('Detected Bits (1/0)')
plt.grid(True)

plt.show()
