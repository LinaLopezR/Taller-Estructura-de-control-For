archivo = open('paises.txt', 'r',encoding="utf8")
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
 """
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la letra M 
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="M"):
    print(i)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="U"):
    print(i)
 """

#Cuente e imprima cuantos paises que hay en el archivo
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
print(len(lista))
"""
#Busque e imprima la ciudad de Singapur
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
print(lista[163])
"""
#Busque e imprima el pais de Venezuela y su capital
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
print(lista[189])
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="E"):
    print(i)
"""
#Buesque e imprima la Capiltal de Colombia
"""
for i in archivo:
  pais, capital = i.split(': ')
  if pais == "Colombia":
    print(capital)
"""

#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México\n"):
    break
  lista=[]   
print(c)
"""
#cambio de palabra
"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato

lines_list = archivo.readlines()
count = 0
for l in lines_list:
  if 'Madagascar' in l:
    lines_list[count] = "Madagascar: Antananarivo\n"
    break
  
  count+=1

new_archivo = open('paises.txt', 'w',encoding="utf8")
new_archivo.writelines(lines_list)
"""

#Agregue un país que no esté en la lista 
"""
new_archivo = open('paises.txt', 'a',encoding="utf8")
new_archivo.write("\nSeychelles: Victoria")
"""

archivo.close()
