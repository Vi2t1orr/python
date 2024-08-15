#questao1

x = []
for i in range(10): 
  x.append(input("Digite um valor: "))
print(x)

#..........................................

#questao2

x = []
for i in range(10): 
  x.append(int(input("Digite um valor: ")))
print(x)

for i in range(10): 
  if isinstance(x[i], str):
    x[i] = 'erro'
  
  elif x[i] % 2 == 0:
    x[i] = x[i] * i

  else:
    x[i] = i

print(x)

A = [1,2,3,4,5]
B = [6,7,8,9,10]
C = A + B

#..........................................

#questao3

l1 = []
l2 = []

for i in range(5):
  l1.append(int(input("Digite um valor inteiro para a lista 1: ")))

print("\n===========================\n")
for i in range(5):
  l2.append(int(input("Digite um valor inteiro para a lista 2: ")))

soma = sum(l1) + sum(l2)

print(soma)

#..........................................

#questao4

l1 = []
l2 = []
l3 = []

for i in range(5):
  l1.append(int(input("Digite um valor inteiro para a lista 1: ")))

print("\n===========================\n")
for i in range(5):
  l2.append(int(input("Digite um valor inteiro para a lista 2: ")))
c = 4
for i in range(5):
  l3.append(l1[i] * l2[c])
  c-=1

print(l3)

#..........................................

#questao5

print(C)
