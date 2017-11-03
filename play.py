from blottogame import BlottoGame
import numpy as np

me = [18, 18, 16, 6, 8, 8, 2, 10, 8, 6]

enemy = [16, 24, 12, 6, 2, 17, 5, 3, 11, 4]
#enemy = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]


print(BlottoGame(enemy, me, 10))
