import hikari
import opensimplex
opensimplex.seed(1234)
for i in range(10):
    n = opensimplex.noise2(x=i, y=i) * 100
    n = int(n)
    print(n)