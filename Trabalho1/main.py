from codificadores import b8zs, nrz_l, nrz_i, ami, pseudoternary, manchester, manchester_differential, hdb3, mlt_3
from plot import plot_sinal

bits = "01001110"
sinal_b8zs = b8zs(bits)
sinal_nrzl = nrz_l(bits)
sinal_nrzi = nrz_i(bits)
sinal_ami = ami(bits)
sinal_pseudo = pseudoternary(bits)
sinal_man = manchester(bits)
sinal_man_diff = manchester_differential(bits)
sinal_hdb3 = hdb3(bits)
sinal_mlt3 = mlt_3(bits)

plot_sinal(sinal_b8zs, bits, 'B8ZS')
plot_sinal(sinal_nrzl, bits, 'NRZ - L')
plot_sinal(sinal_nrzi, bits, 'NRZ - I')
plot_sinal(sinal_ami, bits, 'AMI')
plot_sinal(sinal_pseudo, bits, 'PSEUDOTERNARY')
plot_sinal(sinal_man, bits, 'MANCHESTER')
plot_sinal(sinal_man_diff, bits, 'MANCHESTER DIFFERENTIAL')
plot_sinal(sinal_hdb3, bits, 'HDB3')
plot_sinal(sinal_mlt3, bits, 'MLT - 3')