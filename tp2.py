##tarea 2
num1=100
num2=100
suma = num1+num2
print (num1+num2)

num1 = input ("Ingrese un numero: ")
num2 = input ("Ingrese otro numero: ")
num1n = int (num1)
num2n = int (num2)
suma=num1n + num2n
print("La suma es " , suma)

##tarea 3

num1=12
num2=13
num1 = input("Ingrese num1: ")
num2 = input("Ingrese num2: ")
num1n= int (num1)
num2n= int (num2)
multiplicacion = num1n*num2n
print ("La multiplicacion es " , multiplicacion)

##tarea 4

num1=321
num2=213
num1 = input("Ingrese num1: ")
num2 = input("Ingrese num2: ")
num1n= int (num1)
num2n= int (num2)
resta = num1n-num2n
print ("La resta es " , resta)

##tarea 5
print ((20+5)%6)

##tarea 6 crea un programa que calcule el producto De los números 12 y 102

num1=12
num2=102
num1 = input("Ingrese num1: ")
num2 = input("Ingrese num2: ")
num1n= int (num1)
num2n= int (num2)
multiplicacion = num1n*num2n
print ("La multiplicacion es " , multiplicacion)

##tarea 7 Crea un programa que calcule la suma de 200 y 1111, usando variables
num1 =200
num2 = 1111

num1 = input ("Ingrese un numero: ")
num2 = input ("Ingrese otro numero: ")
num1n = int (num1)
num2n = int (num2)
suma=num1n + num2n
print("La suma es " , suma)


##tarea 8 crea un programa que calcule el producto de los números 10 y 25, usando variables llamadas “numero 1” y “numero 2”
numero1=10
numero2=25
num1 = input("Ingrese num1: ")
num2 = input("Ingrese num2: ")
num1n= int (num1)
num2n= int (num2)
multiplicacion = num1n*num2n
print ("La multiplicacion es " , multiplicacion)

##tarea 9  Crea un programa que calcule el producto de dos números introducidos por usuario
num = 0 

num1 = input("Ingrese num1: ")
num2 = input("Ingrese num2: ")
num1n= int (num1)
num2n= int (num2)
multiplicacion = num1n*num2n
print ("La multiplicacion es " , multiplicacion)


##tarea 10 crea un programa que pida al usuario un número entero y diga si es par
number = 0

while True:
  try:
     number=int(input("Ingrese un numero: ")) 
  except ValueError:
     print("Not an integer! Try again!") 
     continue
  else:
     if number%2 == 0:   
         print("El numero", number, "Es par") 
     else:
         print("El número", number, " no es par! Entonces, es impar!") 
         break 

##tarea 11  Crea un programa que pida usuario dos números enteros y diga cuál es el mayor de ellos

def main():
    print("NÚMERO MAYOR")
    primero = int(input("Escriba un número: "))
    segundo = int(input(f"Escriba un número mayor que {primero}: "))

    while segundo <= primero:
        segundo = int(
            input(f"{segundo} no es mayor que {primero}. Inténtelo de nuevo: "))

    print()
    print(f"Los números que ha escrito son {primero} y {segundo}.")

##tarea 12 Crea un programa que pida al usuario dos números enteros.
##Si el segundo no es cero, mostrará el resultado de dividir ente el primero 
##Y el segundo. Por el contrario si el segundo número es cero, escribirá
##“Error: No se puede dividir entre cero”.
def main():
    print("DIVISOR DE NÚMEROS")
    dividendo = int(input("Escriba el dividendo: "))
    divisor = int(input("Escriba el divisor: "))

    if dividendo % divisor == 0:
        print(f"La división es exacta. Cociente: {dividendo // divisor}")
    else:
        print(
            f"La división no es exacta. Cociente: {dividendo // divisor} "
            f"Resto: {dividendo % divisor}"
        )

##tarea13


##tarea 14
i = 0 
while i <=9:
    i +=1     
    print (i)

##tarea 15 do while
x=1
while True:
    
     print (x)
     x=x+1
     if >=11:
         break

print("fin while")

##tarea 16 Crea un programa que escriba en pantalla números del 10 al 20 usando for
for x in range (10, 21):
    print (x)
