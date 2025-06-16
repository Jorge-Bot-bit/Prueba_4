# EJERCICIO PRUEBA PARCIAL 4

# DATOS INICIALES

stock_concepcion = 500
stock_puente_alto = 1300
stock_valparaiso = 100
stock_vina_mar = 50

entradas_concepcion = []
entradas_puente_alto = []
entradas_valparaiso = []
entradas_vina_mar = []

# Funcion validacion codigo

def codigo_concepcion(codigo):
    return(len(codigo) >= 6 and
           any(c.isupper()for c in codigo)and
           any(c.isdigit()for c in codigo)and
           ' ' not in codigo)


# Funciones Principales

def comprar_concepcion():
    print("--- Comprar de entrada 'Los fortificados' en Concepcion ---")
    global stock_concepcion
    if stock_concepcion == 0:
        print("Lo sentimos, no hay entradas disponibles en Concepcion")
        return
    nombre = input("Ingrese su nombre --> : ")
    if nombre in [entrada['nombre'] for entrada in entradas_concepcion]:
        print(f"Ya existe una registrada a nombre de {nombre}")
        return
    codigo = input("Ingrese codigo verificador (6 caracteres y al menos un numero y una mayuscula) --> : ")
    if not codigo_concepcion(codigo):
        print("Codigo invalido")
        return
    entradas_concepcion.append({'nombre': nombre , 'codigo': codigo})
    stock_concepcion -= 1
    print(f"Entrada registrada para {nombre}, stock restante: {stock_concepcion}")
    
    
def comprar_puente_alto():
    print("--- Compra de entradas 'Los Fortificados' en Puente Alto ---")
    global stock_puente_alto  
    if stock_puente_alto == 0:
        print("Lo sentimos, no hay entradas disponibles en Puente Alto")
        return
    nombre = input("Ingrese su nombre --> : ")
    if nombre in [entrada['nombre'] for entrada in entradas_puente_alto]:
        print(f"Ya existe una entrada registrada a nombre de {nombre}")
        return
    else:
        try:
            cantidad = int(input("Ingrese la cantidad de entradas que desea comprar (max 3) --> :"))
            if cantidad < 1 or cantidad > 3:
                print("Cantidad no valida")
                return
        except ValueError:
            print("Cantidad no valida")
        entradas_puente_alto.append({'nombre': nombre , 'cantidad': cantidad})
        stock_puente_alto -= cantidad
        print(f"Entrada(s) registrada(s) para {nombre}, stock restante: {stock_puente_alto}")


def comprar_valparaiso():
    print("--- Compra de entradas 'Los Fortificados' en Valparaiso ---")
    global stock_valparaiso
    if stock_valparaiso == 0:
        print("Lo sentimos, no hay entradas disponibles en Valparaiso")
        return
    nombre = input("Ingrese su nombre --> : ")
    if nombre in [entrada['nombre'] for entrada in entradas_valparaiso]:
        print(f"Ya existe una entrada registrada a nombre de {nombre}")
        return 
    tipo_entrada = input("Tipo en entrada asignado --> : ").upper()
    if tipo_entrada.upper() != "G":
        print("Tipo de entradas no valido, solo se aceptan entradas generales (G)")
        return
    entradas_valparaiso.append({'nombre': nombre , 'tipo_entrada': tipo_entrada})
    stock_valparaiso -= 1
    print(f"Entrada registrada para {nombre}, stock restante: {stock_valparaiso}")


def comprar_vina_mar():
    print("--- Compra de entradas 'Los Fortificados' en Viña del Mar ---")
    global stock_vina_mar
    if stock_vina_mar == 0:
        print("Lo sentimos, no hay entradas disponibles en Viña del Mar")
        return
    nombre = input("Ingrese su nombre --> : ")
    if nombre in [entrada['nombre'] for entrada in entradas_vina_mar]:
        print(f"Ya existe una entrada registrada a nombre de {nombre}")
        return 
    tipo_entrada = input("Tipo en entrada asignado (Sun=Sunset, Ni=Night) --> : ").upper()
    if tipo_entrada not in ["SUN", "NI"]:
        print("Tipo de entradas no valido, solo se aceptan entradas en el atardecer o en la noche (NI/SUN)")
        return
    entradas_vina_mar.append({'nombre': nombre , 'tipo_entrada': tipo_entrada})
    stock_vina_mar -= 1
    print(f"Entrada registrada para {nombre}, stock restante: {stock_vina_mar}")
    
                   
# Menu        
            
def menu():
    while True:
        print("--- TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE ---")
        print("1.- Comprar entrada a “los Fortificados” en Concepción.")
        print("2.- Comprar entrada a “los Fortificados” en Puente Alto.")
        print("3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.")
        print("4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.")
        print("5.- Salir.")
        opcion = input("\nIngrese una opción: ")
        if opcion == "1":
            comprar_concepcion()
        elif opcion == "2":
            comprar_puente_alto()
        elif opcion == "3":
            comprar_valparaiso()
        elif opcion == "4":
            comprar_vina_mar()
        elif opcion == "5":
            print("Programa terminado...")
            break
        else:
            print("Opcion no valida, intente nuevamente.")   
menu()                             


        