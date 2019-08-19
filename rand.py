# Gera arquivos randomicos para testes

import random
import time


with open('f1.txt', 'w') as file_out:

    for x in range(10000000):
        line1 = random.randint(1, 100000000)
        line2 = random.randint(1, 100000000)
        line3 = random.randint(1, 100000000)

        file_out.write(str(line1) + ';' + str(line1) + ';' + str(line1) + '\n') # --- Maior probabilidade de miltiplicidades
        #file_out.write(str(line1) + ';' + str(line2) + ';' + str(line3) + '\n') # --- Menor probabilidade de miltiplicidades
