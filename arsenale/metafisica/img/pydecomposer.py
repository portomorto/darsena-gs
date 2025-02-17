import numpy as np
import matplotlib.pyplot as plt

# Parametri
fs = 44100  # Frequenza di campionamento
duration = 0.1  # Durata in secondi
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Funzioni d'onda
wave1 = (np.sin(2 * np.pi * 500 * t) + 1) / 2
wave2 = (np.sin(2 * np.pi * 1000 * t) + 1) / 2
wave3 = (np.sin(2 * np.pi * 1500 * t) + 1) / 2

# Unità decomposta
decomposed_unit = 1 - wave1 - wave2 - wave3

# Plotta i segnali
fig, axs = plt.subplots(4, 1, sharex=True, figsize=(8, 6))

axs[0].plot(t, decomposed_unit)
axs[0].set_ylabel('Unità decomposta')
axs[0].grid(True)

axs[1].plot(t, wave1)
axs[1].set_ylabel('Onda 1 (500 Hz)')
axs[1].grid(True)

axs[2].plot(t, wave2)
axs[2].set_ylabel('Onda 2 (1000 Hz)')
axs[2].grid(True)

axs[3].plot(t, wave3)
axs[3].set_ylabel('Onda 3 (1500 Hz)')
axs[3].set_xlabel('Tempo (s)')
axs[3].grid(True)

plt.tight_layout()
plt.savefig('decomposed_unit.svg')
