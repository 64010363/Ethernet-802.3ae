import numpy as np
import matplotlib.pyplot as plt

# Encoded data
encoded_data = np.array([1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0], dtype=np.int8)

# Define modulation parameters
bit_duration = 1.0  # Time duration of each bit
carrier_frequency = 10.0  # Carrier frequency (e.g., 10 Hz)
amplitude_low = 0.0  # Low amplitude
amplitude_high = 1.0  # High amplitude

# Time vector
t = np.linspace(0, bit_duration * len(encoded_data), len(encoded_data) * 10)

# Modulated signal
modulated_signal = np.zeros(len(t))
for i, bit in enumerate(encoded_data):
    amplitude = amplitude_high if bit == 1 else amplitude_low
    modulated_signal[i * 10: (i + 1) * 10] = amplitude * np.sin(2 * np.pi * carrier_frequency * t[i * 10: (i + 1) * 10])

# Plot the modulated signal
plt.figure(figsize=(10, 4))
plt.plot(t, modulated_signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('ASK Modulated Signal')
plt.grid(True)
plt.show()
