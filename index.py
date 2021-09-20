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
