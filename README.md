# A hipótese de Riemann: uma representação gráfica

Proposta pelo matemático alemão Bernhard Riemann em 1859, a hipótese de Riemann é provavelmente uma das mais famosas e instigantes conjecturas matemáticas do mundo. Ela é uma dos sete problemas do milênio cuja resolução seria premiada pelo Instituto Clay com cerca de um milhão de dólares.

Caso a teoria seja comprovada, muita coisa sobre o que sabemos sobre os números primos seria reescrita, o que afetaria diretamente inúmeras aplicações que os utilizam. Dentre elas, estão as criptografias desenvolvidas com base no modelo RSA, que empregam os números primos para gerar suas chaves públicas e privadas.

O seu enunciado é relativamente simples: Riemann afirmou que a distribuição de números primos não é aleatória, podendo seguir um padrão quando descrita pela função zeta de Riemann:

$$\zeta(s) = \dfrac{2^{iy}}{2^{iy}-2^{1-x}}\cdot\sum_{n=1}^\infty \dfrac{(-1)^{n-1}}{n^x}\left[\cos(y\log(n))-i\sin(y\log(n))\right]$$

Além disso, os seus zeros resultantes, com exceção dos chamados “zeros triviais” (−2, −4, −6...), possuem parte real ½ e uma grande quantidade deles estão localizados na chamada linha crítica (que estará visível no gráfico como uma linha vertical verde).

$$\zeta(\dfrac{1}{2}+it)$$

Nesse programa feito em Python, você conseguirá observar toda a distribuição dos zeros de Riemann em um gráfico desenvolvido através da biblioteca Matplotlib. Basta inserir um valor máximo inteiro para “t” que o backend já começará a realizar todos os cálculos necessários para plotar a representação. Quem sabe você até encontre no meio dos dados algum padrão que ajude outros estudiosos a confirmar a hipótese?
