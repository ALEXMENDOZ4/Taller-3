from numpy.random import randint
import numpy as np


def ejercicio1():
    n = int(input("digite la cantidad de autos\n"))
    i = 1
    amarillo = 0
    rosa = 0
    rojo = 0
    verde = 0
    azul = 0
    print("***Digito del automovil***")
    print("1 o 2 amarillo")
    print("3 o 4 rosa")
    print("5 o 6 rojo")
    print("7 o 8 verde")
    print("9 o 0 azul")
    while i <= n:
        digito = int(input("escriba el ultimo digito de la placa de su auto\n"))
        if(digito == 1 ) | (digito == 2):
            amarillo = amarillo + 1
        elif(digito == 3) | (digito == 4):
            rosa = rosa + 1
        elif(digito == 5) | (digito == 6):
            rojo = rojo + 1
        elif(digito == 7) | (digito == 8):
                verde = verde + 1
        elif(digito == 9) | (digito == 0):
                azul = azul + 1
        i+=1

    print("total de automoviles con calcomania amarillo", amarillo)
    print("total de automoviles con calcomania rosa", rosa)
    print("total de automoviles con calcomania rojo", rojo)
    print("total de automoviles con calcomania verde", verde)
    print("total de automoviles con calcomania azul", azul)
            

ejercicio1()


def ejercicio2():
    i = 1
    n = 0
    total = 0
    edad = 0
    categoria1 = 0
    categoria2 = 0
    categoria3 = 0
    animal = ""

    print("selecciona un animal")
    print("1 = elefante\n")
    print("2 = jirafas\n")
    print("3 = chimpances\n")
    n = int(input("escoga una opcion\n"))

    if(n > 1 and n < 4):
        if(n == 1):
            animal = "elefante"
            total = 20
        elif(n == 2):
               animal = "jirafas"
               total = 15
        elif(n == 3):
               animal = "chimpances"
               total = 40        

    for i in range(0,total):
        
      edad = int(input(f"{i+1}. ingresa la edad: "))
      

      if(edad >= 0 and edad <= 1):
       categoria1+=1
      elif(edad < 3):
       categoria2+=1
      elif(edad >= 3):
       categoria3+=1             

    print("porcentaje de edades de ", animal)
    print((categoria1/total)*100,"% de 0 a 1 año")
    print((categoria2/total)*100,"% de mas de 1 año y menos de 3")
    print((categoria3/total)*100,"% de 3 años o mas")


ejercicio2()



def ejercicio3(): 
   t = int(input("Escribe el numero de trabajadores\n"))
   x = 1
   salario = 0
   horas_extra = 0

   while x <= t:
      h = int(input("escribe el numero de horas trabajadas\n"))

      
      if(h <= 40):
          salario = h * 20
          print("el salario del trabajador ",x," es:", salario)
      else:
        horas_extra = h - 40
        salario = (40 * 20) + (horas_extra * 25)
        print("el salario del trabajador ",x," es:", salario)

      x+=1     

ejercicio3()


def ejercicio4():
    n = int(input("ingrese el numero de alumnos de todo el grupo\n"))
    x = 1
    mujeres = 0
    hombres = 0
    edadMujer = 0
    edadHombre = 0

    while(x <= n):
        print("Escribe un numero de acuerdo a su sexo:")
        print("1 = mujer")
        print("2 = hombre")
        sexo = int(input("escoga una opcion: "))
        edad = int(input("escribe tu edad: "))

        if(sexo == 1):
            edadMujer = edadMujer + edad
            mujeres+=1
            promedioM = edadMujer / mujeres
        else:
            edadHombre = edadHombre + edad
            hombres+=1
            promedioH = edadHombre / hombres    

        x+=1
    print("el promedio de todo el grupo es:", (edadMujer + edadHombre) / n ,"años")
    print("el promedio de edades de mujeres de todo el grupo es: ",promedioM ,"años")
    print("el promedio de edades de hombres de todo el grupo es: ",promedioH ,"años")


ejercicio4()


def ejercicio5():
    n = int(input("escribe el total de numeros a calcular\n"))
    x = 1
    while(x <= n):
       numero = int(input("escriba un numero\n"))
       if(x == 1):
           menor = numero
       else:
           if(numero < menor):
               menor = numero
       x+=1
    print("el numero menor es: ", menor)    


ejercicio5()


def ejercicio6():
    x = 0
    n = 0
    pesoA = 0
    peso = 0
    suma = 0

    for n in range(n,5):
        print("\npersona", n+1)
        pesoA = int(input("ingresa tu peso anterior\n"))

        for x in range(x,10):
            peso = int(input(f'ingresa el peso {x+1} : ' ))
            suma = suma + peso
        if(suma / 10 == pesoA):
            print("la personas",x, "se mantiene en el peso")
        elif(suma / 10 > pesoA):
            print("la persona",n+1,"subio")
        else:            
            print("la persona",n+1,"bajo") 
        x = 0       

ejercicio6()


def ejercicio7():
    cantidad = 0
    total = 0
    precio = 0
    res = 0

    while(True):
      cantidad = int(input("ingresa la cantidad de articulos\n"))
      precio = int(input("ingrese el precio del articulo\n"))
      total = total + (cantidad * precio)
      res = int(input("desea seguir comprando (1.si 2.no)\n"))

      if(res != 1):
          break
      
    print("el total a pagar por los articulos es: ", total)    
        

ejercicio7()


def ejercicio8():
    edad = 0
    res = 0
    categoria1 = 0
    categoria2 = 0
    categoria3 = 0
    categoria4 = 0
    categoria5 = 0
    total = 0

    precio = int(input("ingresa el precio del boleto: "))

    while(True):

        edad = int(input("ingresa la edad: "))

        if(edad < 5):
            print("no se permiten menores de 5 años")
        elif(edad <= 14):
            descuento = (precio * 0.35)
            categoria1 = categoria1 + descuento
        elif(edad <= 19):
            descuento = (precio * 0.25)
            categoria2 = categoria2 + descuento
        elif(edad <= 45):
            descuento = (precio * 0.10)
            categoria3 = categoria3 + descuento
        elif(edad <= 65):
            descuento = (precio * 0.25)
            categoria4 = categoria4 + descuento
        else:
            descuento = (precio * 0.35)
            categoria5 = categoria5 + descuento
        
        total = total + descuento

        print("el descuento aplicado es: ", descuento)

        res = int(input("desea continuar? 1.si 2.no: "))                        

        if(res != 1):
          break 

    print("el descuento total en la categoria 1 es:", categoria1)
    print("el descuento total en la categoria 2 es:", categoria2)
    print("el descuento total en la categoria 3 es:", categoria3)
    print("el descuento total en la categoria 4 es:", categoria4)
    print("el descuento total en la categoria 5 es:", categoria5)

    print("el descuento total es: $", total)      


ejercicio8()



def ejercicio9():
    vendedor = []
    comision_venta = []
    i = 1
    n = int(input("ingrese numero de vendedores\n"))
    while(i <= n):
       nombre = input("Ingrese nombre vendedor\n")
       vendedor.append(nombre) 
       venta = int(input("ingrese importe total venta\n"))
       if(venta <= 20000000):
          comision = venta * 0.10
       elif(venta > 20000000 and venta < 40000000):
          comision = venta * 0.15
       elif(venta >= 40000000 and venta < 80000000):       
          comision = venta * 0.20    
       elif(venta >= 80000000 and venta <= 1600000000):
          comision = venta * 0.25
       elif(venta >= 1600000000):
          comision = venta * 0.30
       i+=1
       comision_venta.append(comision) 
       
       print("Comisiones vendedores")
       print("nombre vendedor:",vendedor, "comision:",comision_venta)


ejercicio9()



def ejercicio10():
  values = randint(0, 3, 50000)
  count_arr = np.bincount(values)
  can1 = (count_arr[0])
  can2 = (count_arr[1])
  can3 = (count_arr[2])
  
  if can1 > can2 and can1 > can3 : winname ="Canditato #1"
  if can2 > can1 and can2 > can3 : winname ="Candidato #2"
  if can3 > can1 and can3 > can2 : winname ="Candidato #3"
  
  winnum=max(can1, can2, can3)
  
  print(can1)
  print(can2)
  print(can3)
  print(f"el ganador es "+winname+" con "+str(winnum)+" votos")



ejercicio10()