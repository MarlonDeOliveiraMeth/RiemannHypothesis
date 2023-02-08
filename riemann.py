# Importação das bibliotecas numpy e matplotlib.
import numpy as np
import matplotlib.pyplot as plt

# Cálculos da função zeta de Riemann.
def zeta(x, y):
    eq1 = (2**(y*1j))/((2**(y*1j))-(2**(1-x))) 
    eq2 = 0
    
    for n in range(1, 9999):
        eq2 += (((-1)**(n-1))/(n**x))*(np.cos(y*np.log(n))-1j*np.sin(y*np.log(n)))

    res = eq1*eq2

    return res.real, res.imag

# Input do usuário e configurações do gráfico.
def chart(x):
    try:
        value = int(input('Sendo a função zeta de Riemann definida como ζ(1/2 + it), insira um valor máximo para "t": '))
        print("Calculando e gerando gráfico...")

        reals = []
        imags = []

        for t in range(0, value):
            y = t
            z = zeta(x, y)
            reals.append(z[0])
            imags.append(z[1])

        plt.figure().add_subplot(1,1,1).set_aspect(1)
        plt.plot(reals, imags, color="blue", marker=".", mec = "red", mfc = "red")
        plt.title('Função zeta de Riemann calculada com "t" sendo cada número inteiro entre 0 e ' + str(value))
        plt.xlabel("Reais")
        plt.ylabel("Imaginários")
        plt.axhline(y=0, color="black")
        plt.axvline(x=0, color="black")
        plt.axvline(x=0.5, color="green")
        plt.grid(True)
        plt.show()

    except:
        print("Por favor, insira valor válido.")

# Execução do script, passando o valor padrão de "x".
if __name__ == "__main__":
    chart(1/2)
