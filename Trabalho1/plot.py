import matplotlib.pyplot as plt

def plot_sinal(sinal, bits, name):
    tempo = list(range(len(sinal)))
    plt.step(tempo, sinal, where='post')
    plt.ylim(-2, 2)
    plt.grid()
    plt.title(f'Codificação do sinal: {bits}')
    plt.xlabel('Tempo')
    plt.ylabel('Nível de Tensão')
    plt.show() 
    plt.close()
