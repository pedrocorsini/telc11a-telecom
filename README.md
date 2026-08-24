# TELC11A - Lab Telecomunicações 1

Repositório com implementações em Python de técnicas clássicas de modulação analógica, desenvolvidas para a disciplina de TELC11A - Laboratório de Telecomunicações 1 (UNIFEI). Os scripts geram e analisam sinais modulados em **AM-DSB-SC**, **AM-DSB**, **PM** e **FM**, tanto no domínio do tempo quanto no domínio da frequência.

## Estrutura

```
codes/
├── modulacao_tempo.py        # Sinais modulados no domínio do tempo
└── modulacao_frequencia.py   # Espectros dos sinais modulados (via FFT)
```

## Requisitos

```bash
pip install numpy matplotlib
```

## Scripts

### `codes/modulacao_tempo.py`

Plota os sinais modulados no domínio do tempo:

- **AM-DSB** — `s(t) = Ac[1 + μ·x(t)]·cos(ωc t)`, com a envoltória superior/inferior sobreposta ao sinal para visualizar o índice de modulação `μ`.
- **PM** — `s(t) = Ac·cos(ωc t + Kp·m(t))`.
- **FM** — `s(t) = Ac·cos(ωc t + β·sin(ωm t))`, com índice de modulação `β = Kf·Am/fm`.

### `codes/modulacao_frequencia.py`

Calcula e plota o espectro (magnitude via FFT) de quatro sinais modulados a partir do mesmo sinal modulante e portadora:

- **AM-DSB-SC** — `s(t) = m(t)·carrier(t)`
- **AM-DSB** — `s(t) = m(t)·carrier(t) + carrier(t)`
- **PM** — `s(t) = Ac·cos(ωc t + Kp·m(t))`
- **FM** — `s(t) = Ac·cos(ωc t + β·sin(ωm t))`

A função `fourier(signal, fs)` centraliza o espectro em 0 Hz (`fftshift`) e normaliza a magnitude pelo número de amostras.

## Parâmetros padrão

| Parâmetro | Valor | Descrição |
|---|---|---|
| `fs` | 10000 Hz | Frequência de amostragem |
| `Am` | 8 | Amplitude do sinal modulante |
| `fm` | 200 Hz | Frequência do sinal modulante |
| `Ac` | 1 | Amplitude da portadora |
| `Fc` | 1000 Hz | Frequência da portadora |
| `Kp` | 0.5 | Constante de sensibilidade de fase (PM) |
| `Kf` | 500 | Constante de sensibilidade de frequência (FM) |

## Observação técnica

Com `Am=8` e `Ac=1`, o índice de modulação do AM-DSB é `μ = Am/Ac = 8`, caracterizando **sobremodulação severa** — a envoltória do sinal assume valores negativos, o que inviabilizaria a demodulação por detector de envoltória simples, ainda que o espectro (FFT) apresente corretamente as três componentes esperadas (`±(Fc-fm)`, `±Fc`, `±(Fc+fm)`).

## Como executar

```bash
python codes/modulacao_tempo.py
python codes/modulacao_frequencia.py
```