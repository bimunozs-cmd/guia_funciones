
def menu():

    print("MENU\n1. iniciar programa \n2. verificar si son par o impar  \n3. salir ")

def p_imp ():
     
     numero == 2%
     

numeros = []

par = []
impar = []

while True :

    menu()

    try:

        op = int(input("ingrese una opcion (1/2) ="))
    
    except ValueError:
        print("ingrese un numero entero como opcion")
        continue 
    if op == 1:

        cant_n = int(input("ingrese la cantidad de numero que desea comprobar ="))

        for i in range(cant_n):
             
             numero = int(input(f"ingrese el numero ({i+1}) ="))

             numeros.append(numero)

        print(numeros)
        print("desea continuar si lo desea ingrese una opcion si o no ")
        s_n = str(input("ingrese la opcion ="))

        if s_n == "si":
             continue
        elif s_n == "no":
             break
        
    elif op == 2:
         
         print("armando las listas\n")

    elif op == 3:
        break

    elif op <= 0:
         print("ingrese una opcion mayo a 0")
         continue

        

    else:

        
    

            break


