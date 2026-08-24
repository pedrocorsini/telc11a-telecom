import matplotlib.pyplot as plt
import numpy as np

# Parâmetros
t = np.linspace(0, 0.01, 1000)

# Sinal modulante
Am = 8
fm = 200
m_t = np.cos(2 * np.pi * fm * t)

# Sinal Portadora
Ac = 1
Fc = 1000
carrier = np.cos(2 * np.pi * Fc * t)

# Índice de Modulação
#m_a = Am/Ac
m_a = 1

# AM-DSB
# s(t) = Ac[1 + m_a*x]*carrier
moduled_signal = Ac * (1 + m_a * m_t) * carrier

# Envoltória para visualização
envoltoria_sup = Ac + m_a*m_t
envoltoria_inf = -envoltoria_sup

# Modulação PM
Kp = 0.5 # arbitrario
carrier_phase = 2 * np.pi * Fc * t
pm = Ac * np.cos(carrier_phase + Kp * Am * m_t)

# Modulação FM
Kf = 500
b = Kf*Am/fm
signal_fm = Ac * np.cos(2*np.pi*Fc*t + b*np.sin(2*np.pi*fm*t))


# Plotagem
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

# AM-DSB
axs[0].plot(t * 1000, moduled_signal, label='Sinal Modulado s(t)', color='blue')
axs[0].plot(t * 1000, envoltoria_sup, 'r--', alpha=0.7, label='Envoltória +[Ac + m(t)]')
axs[0].plot(t * 1000, envoltoria_inf, 'g--', alpha=0.7, label='Envoltória -[Ac + m(t)]')
axs[0].set_xlabel('Tempo (ms)')
axs[0].set_ylabel('Amplitude')
axs[0].set_title(f'Sinal AM-DSB (Fc={Fc}Hz, fm={fm}Hz, μ={m_a})')
axs[0].grid(True)
axs[0].legend(loc='upper right')

# PM
axs[1].plot(t * 1000, pm, label='Sinal PM', color='purple')
axs[1].set_xlabel('Tempo (ms)')
axs[1].set_ylabel('Amplitude')
axs[1].set_title(f'Sinal PM (Fc={Fc}Hz, fm={fm}Hz, Kp={Kp})')
axs[1].grid(True)
axs[1].legend(loc='upper right')

# FM
axs[2].plot(t * 1000, signal_fm, label='Sinal FM', color='green')
axs[2].set_title(f'Sinal FM (Fc={Fc}, fm={fm}Hz, b={b:.2f})')
axs[2].set_xlabel('Tempo (ms)')
axs[2].set_ylabel('Amplitude')
axs[2].grid(True)
axs[2].legend(loc='upper right')

fig.suptitle(
    f'Sinais Modulados — m(t) = {Am}·cos(2π·{fm}t)   |   portadora(t) = {Ac}·cos(2π·{Fc}t)',
    fontsize=14, fontweight='bold'
)
plt.tight_layout()
plt.show()