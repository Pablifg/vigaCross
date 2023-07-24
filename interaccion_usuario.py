
import os
import sys
import numpy as np

#VARIABLES

SALIR = "s"
encabezado = []
TITULO = """
------------------------------------------------------------------------------
Rutina que determina los esfuerzos internos de una viga continua con N tramos
y diferentes cargas mediante el metodo de cross.

Unidades:

- Tramos en [m] 
- Cargas unif. [kN/m]  signo (+) direccion gravitacional.
- Rigideces en [kNm2]

(s)alir
------------------------------------------------------------------------------
"""

FIN="""
------------------------------------------------------------------------------
"""

# PRESENTACION EN LA MEDIDA QUE AVANZA LA RUTINA

encabezado.append(TITULO)

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_encabezado(encabezado):
    for texto in encabezado:
        print(texto)


# CONSULTA NUMERO DE TRAMOS
def numero_tramos():
    while True:
        try:
            num_tramos = input("Numero de tramos? ")
            if num_tramos == SALIR:
                break
            else:
                num_tramos = int(num_tramos)
                break
        except:
            print("Debe ingresar un numero entero mayor o igual que 1")
    if num_tramos == SALIR:
        sys.exit()
    else:
        return num_tramos

# CONSULTA APOYO

def tipo_apoyo(lado : str):

    while True:
            apoyo = input(f"Tipo de apoyo {lado} [(e)mpotrado (a)rticulado]? ")
            if apoyo == SALIR:
                break
            elif apoyo == "e":
                apoyo = "empotrado"
                break
            elif apoyo == "a":
                apoyo = "articulado"
                break
            else:
                print("Debe ingresar (e)mpotrado (a)rticulado o", SALIR)
    
    if apoyo == SALIR:
        sys.exit()
    else:
        return apoyo

# CONSULTA LONGITUD DE LOS TRAMOS

def longitud_tramos(nTramos:int):

    contenedor = []
    for tramo in range(nTramos):
        while True:
            try:
                aux1 = input(f"Longitud del tramo {tramo+1} ? ")
                if aux1 == SALIR:
                    break
                elif float(aux1)<= 0:
                    print("Debe ingresar un numero positivo y mayor que cero")
                else:
                    contenedor.append(float(aux1))
                    break
            except:
                    print("Debe ingresar un numero positivo y mayor que cero")
                
        if aux1 == SALIR:
            sys.exit()
    return np.array(contenedor)

# CONSULTA CARGA DISTRIBUIDA EN CADA TRAMO

def carga_distribuida(nTramos:int):

    contenedor = []
    for tramo in range(nTramos):
        while True:
            try:
                aux1 = input(f"Carga dist. aplicada en tramo {tramo+1} ? ")
                if aux1 == SALIR:
                    break
                else:
                    contenedor.append(float(aux1))
                    break
            except:
                    print("Debe ingresar un valor numerico")
                
        if aux1 == SALIR:
            sys.exit()
    return np.array(contenedor)

# CONSULTA RIGIDECES EN CADA TRAMO

def rigideces_tramos(nTramos:int):

    contenedor = []
    for tramo in range(nTramos):
        while True:
            try:
                aux1 = input(f"Rigidez en tramo {tramo+1} ? ")
                if aux1 == SALIR:
                    break
                elif float(aux1)< 0:
                    print("Debe ingresar un numero positivo")
                else:
                    contenedor.append(float(aux1))
                    break
            except:
                    print("Debe ingresar un numero positivo, mayor o igual que cero")
                
        if aux1 == SALIR:
            sys.exit()
    return np.array(contenedor)


# MODULO INPUT

def entrada_datos():

    #Numero de tramos

    limpiar_consola()
    print_encabezado(encabezado)
    nTramos = numero_tramos()
    encabezado.append(f"Numero de tramos : {nTramos}")
    limpiar_consola()

    # Tipo de apoyo lado izquierdo

    print_encabezado(encabezado)
    apoyo_izq = tipo_apoyo("Izquierdo")
    encabezado.append(f"Apoyo lado Izquierdo : {apoyo_izq}")
    limpiar_consola()

    # Tipo de apoyo lado derecho

    print_encabezado(encabezado)
    apoyo_der = tipo_apoyo("Derecho")
    encabezado.append(f"Apoyo lado Derecho : {apoyo_der}")
    limpiar_consola()

    # longitud de tramos
    print_encabezado(encabezado)
    long_tramos = longitud_tramos(nTramos)
    encabezado.append(f"Longitud de tramos : {long_tramos}")
    limpiar_consola()

    # Carga distribuida
    print_encabezado(encabezado)
    q_distribuida = carga_distribuida(nTramos)
    encabezado.append(f"Carga distribuida en cada tramo : {q_distribuida}")
    limpiar_consola()

    # Rigideces en cada tramo
    print_encabezado(encabezado)
    rigidez_por_cada_tramos = rigideces_tramos(nTramos)
    encabezado.append(f"Rigidez en cada tramo : {rigidez_por_cada_tramos}")
    encabezado.append(FIN)
    limpiar_consola()

    # Resumen
    print_encabezado(encabezado)

    diccionario = {"longTramos": long_tramos , 
                   "cargasTramos": q_distribuida, 
                   "rigidecesTramos": rigidez_por_cada_tramos,
                   "apoyoIzq": apoyo_izq,
                   "apoyoDer": apoyo_der,
                   "noTramos": nTramos,
                   }
    return diccionario