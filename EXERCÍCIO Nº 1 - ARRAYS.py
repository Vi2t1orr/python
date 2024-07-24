#exercicio1. . . . . . . . . . . . . . . 

import numpy as np

N = 10
x = np.zeros(N)

for i in range(N):
  x[i] = float(input(f'Informe um valor para V[{i}]: '))
print("\n")
print(x)

#exercicio2. . . . . . . . . . . . . . . 

import numpy as np

N = 5
x = np.zeros(N)
sum = 0

for i in range(N):
  x[i] = float(input(f'Informe um valor para V[{i}]: '))

for i in range(N):
  sum += x[i]
print("\n")
print(f"\nA soma dos valores de V é: {sum}")

#exercicio3. . . . . . . . . . . . . . . 

import numpy as np

N = 5
v = np.zeros(N)
sum = 0

for i in range(N):
  v[i] = float(input(f'Informe um valor para V[{i}]: '))

for i in range(N):
  sum += v[i]
  
med = sum/N  

print("\n")
print(f"\nA média dos valores presentes no vetor v é: {med}")

#interpretei que seria a média da soma de todos os valores

#exercicio4. . . . . . . . . . . . . . . 
