from cmath import cos, sin, tan
from math import radians


ang = float(input("Digite o valor do ângulo: "))
radAng = radians(ang)

seno = sin(radAng)
coss = cos(radAng)
tg = tan(radAng)

print(f"O seno é {seno:.2f};\nO cosseno é {coss:.2f};\ne a tangente é {tg:.2f}.")