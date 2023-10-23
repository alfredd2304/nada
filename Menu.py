print("Bienvenido al Restaurante, que deseas hacer?")

compra = []
i=0

while i==0:
    print("1. Ver Menu")
    print("2. Resumen del pedido")
    print("3. Eliminar productos")
    print("4. salir")
    opcion = int(input())
    if opcion==1:
        while True:
            print("Ha entrado al Menu, seleccione su pedido")
            print("1. Hamburguesa   ==> 20000$")
            print("2. Papas fritas  ==>  5000$")
            print("3. CocaCola Zero ==>  4000$") 
            print("4. Nuggets Combo ==> 22000$")
            print("5. Helado grande ==>  7000$") 
            print("6. Volver al menu anterior")     
            opcion2 = int(input()) 
            if opcion2==6:
                break
    if opcion==4:
        print("Hasta luego")
        i=1
                