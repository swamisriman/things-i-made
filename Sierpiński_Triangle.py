import matplotlib.pyplot as plt
import random

mapX = [-1, 0, 1]
mapY = [0, 1, 0]
randomSeed = (0, 0.5)

n = 25000
while n:
    trianglePoint = random.randint(0, 2)
    randomSeed = ( (randomSeed[0]+mapX[trianglePoint])/2, (randomSeed[1]+mapY[trianglePoint])/2 )
    mapX.append(randomSeed[0])
    mapY.append(randomSeed[1])
    n -= 1


plt.scatter(mapX, mapY, c="black", marker='.', s=0.1)
plt.title('Sierpiński Triangle')
plt.savefig('Sierpiński_Triangle.png')
plt.show()