
# Crea un bucle que te de la siguiente resultado:
# "1 , -2, 3, -1, 2, -3,..."

# Primera forma:

n = 12 #cantidad de terminos
j= 1 #el numero que iterara entre 1,2,3
lista=[] #lista vacia
for i in range(1,n+1): 
  res = (-1)**(i+1)  # codigo para cambiar de signo saltandose un paso
  num= j*res # Resultado que se guarda en la lista
  lista.append(num) #Agregamos el valor al final de la lista con append
  j=1+j
  j=abs(j) #Regresamos a j a su valor absoluto
  if j==4: # SI el valor de j llega a ser 4, lo igualas a 1 para que reinicie
      j=1
print(lista) # imprmir el resultado 

