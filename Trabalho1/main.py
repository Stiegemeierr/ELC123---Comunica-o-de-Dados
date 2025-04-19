from codificadores import b8zs
from plot import plot_sinal

bits = "10000000000001"
sinal = b8zs(bits)

plot_sinal(sinal, bits)
