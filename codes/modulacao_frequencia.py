import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import hilbert

# Parâmetros    
fs = 50000.0 # 50kHz
T = 1.0/fs
t = np.arange(0, 0.05, T)

# Sinal modulante
Am = 8
fm = 200
m = Am*np.cos(2*np.pi*fm*t)

# Sinal Portadora
Ac = 1
Fc = 1000
carrier = Ac*np.cos(2*np.pi*Fc*t)

# AM-DSB-SC
signal_dsb_sc = m * carrier  

# AM-DSB
signal_dsb = m*carrier + carrier

# Modulação AM-SSB - Transformada de Hilbert
m_hat = np.imag(np.asarray(hilbert(m))) # transformada de Hilbert de m(t)
# USB: m(t)cos(wc t) - m_hat(t)sin(wc t)
signal_ssb = m*carrier - m_hat*Ac*np.sin(2*np.pi*Fc*t)

# Modulação FM
Kf = 50
b = Kf*Am/fm
signal_fm = Ac * np.cos(2*np.pi*Fc*t + b*np.sin(2*np.pi*fm*t))

def fourier(signal, fs):
    N = len(signal)
    S = np.fft.fft(signal)
    S = np.fft.fftshift(S)
    freqs = np.fft.fftfreq(N, d=1/fs)
    freqs = np.fft.fftshift(freqs)
    magnitude = np.abs(S)/N
    return freqs, magnitude              

moduled_am_dsb_sc_freqs, moduled_am_dsb_sc_magnitude = fourier(signal_dsb_sc, fs)
moduled_amdsb_freqs, moduled_amdsb_magnitude = fourier(signal_dsb, fs)
moduled_ssb_freqs, moduled_ssb_magnitude = fourier(signal_ssb, fs)
moduled_fm_freqs, moduled_fm_magnitude = fourier(signal_fm, fs)

# Plotagem
fig, axs = plt.subplots(2, 2, figsize=(15,8), sharex=True)

# AM-DSB-SC
axs[0][0].plot(moduled_am_dsb_sc_freqs, moduled_am_dsb_sc_magnitude, label='Sinal Modulado AM-DSB-SC', color='purple')
axs[0][0].set_title(f'Espectro AM-DSB-SC (Fc={Fc}Hz, fm={fm}Hz)')
axs[0][0].set_xlabel('Frequência (Hz)')
axs[0][0].set_ylabel('Magnitude')
axs[0][0].grid(True)
axs[0][0].legend(loc='upper right')

# AM-DSB
axs[1][0].plot(moduled_amdsb_freqs, moduled_amdsb_magnitude, label='Sinal Modulado AM-DSB', color='blue')
axs[1][0].set_title(f'Espectro AM-DSB (Fc={Fc}Hz, fm={fm}Hz, Am/Ac={Am/Ac})')
axs[1][0].set_xlabel('Frequência (Hz)')
axs[1][0].set_ylabel('Magnitude')
axs[1][0].grid(True)
axs[1][0].legend(loc='upper right')

# AM-SSB
axs[0][1].plot(moduled_ssb_freqs, moduled_ssb_magnitude, label='Sinal Modulado AM-SSB (USB)', color='darkorange')
axs[0][1].set_title(f'Espectro AM-SSB (Fc={Fc}Hz, fm={fm}Hz)')
axs[0][1].set_xlabel('Frequência (Hz)')
axs[0][1].set_ylabel('Magnitude')
axs[0][1].grid(True)
axs[0][1].legend(loc='upper right')

# FM
axs[1][1].plot(moduled_fm_freqs, moduled_fm_magnitude, label='Sinal Modulado FM', color='green')
axs[1][1].set_title(f'Espectro FM (Fc={Fc}Hz, fm={fm}Hz, β={b:.1f})')
axs[1][1].set_xlabel('Frequência (Hz)')
axs[1][1].set_ylabel('Magnitude')
axs[1][1].grid(True)
axs[1][1].legend(loc='upper right')

plt.xlim(-1500, 1500)
fig.suptitle(
    f'Sinais Modulados — m(t) = {Am}·cos(2π·{fm}t)   |   portadora(t) = {Ac}·cos(2π·{Fc}t)',
    fontsize=14, fontweight='bold'
)
plt.tight_layout()
plt.show()