def stark_normalizar_datos(lista_personajes:list) -> bool: #1
    '''Normaliza los datos de los personajes de la lista proporcionada

    Esta función toma una lista de personajes y verifica si los valores de peso, altura
    y fuerza están en los tipos de datos correctos (float para peso y altura, int para fuerza).
    Si algún valor no tiene el tipo de dato correcto, lo convierte al tipo correcto y retorna True.

    Args:
        lista_personajes (list): Una lista de diccionarios, donde cada diccionario representa un personaje
                                 y debe tener claves 'peso', 'altura' y 'fuerza'.

    Returns:
        bool: True si se raliza por lo menos un cambio en los datos (es decir, se realizaron conversiones),
              False si los datos ya estaban en el formato correcto o la lista se encuentre vacia.
    '''

    estado = False

    for personajes in lista_personajes:
        if type(personajes['peso']) != float or type(personajes['altura']) != float or type(personajes['fuerza']) != int:
            personajes['peso'] = float(personajes['peso'])
            personajes['altura'] = float(personajes['altura'])
            personajes['fuerza'] = int(personajes['fuerza'])
            estado = True 

    return estado

#----------------------
def obtener_dato(personaje:dict, caracteristica:str) -> str | bool: #TODO 
    '''devuelve la caracteristica especificada de un diccionario
    
    Args:
        personajes(dict): diccionario que representa un personaje en especifico
        caracteristica(str): clave del diccionario donde obtener el valor

    Return:
        str: en caso de que la caracteristica ingresados pertenezcan a un diccionario.
        bool: si el diccionario esta vacio o la caracteristica no pertenezca al diccionario.
    
    ejemplo:
        obtener_dato(personaje, 'altura')
    '''
    
    if not personaje or not 'nombre' in personaje or not caracteristica in personaje:
        return False
    
    return f"{caracteristica.capitalize()}: {personaje[caracteristica]}"


def obtener_nombre(personaje:dict) -> str | bool: 
    '''devuelve la clave nombre de un diccionario

    Args:
        personajes(dict): diccionario que representa un personaje en especifico
    
    Return:
        str: en caso de que la clave 'nombre' pertenezcan a un diccionario.
        bool: si el diccionario esta vacio o la caracteristica no pertenezca al diccionario.
        
    '''
    if not personaje or not 'nombre' in personaje:
        return False
    
    return obtener_dato(personaje, 'nombre')


def obtener_nombre_y_dato(personaje:dict, caracteristica:str) -> str | bool: #2
    '''devuelve un mensaje concatenado de la clave 'nombre' y la clave ingresada como parametro
    
    Args:
        personaje(dict): diccionario que representa un personaje en especifico.
    
    Return:
        str: nombre y caracteristica concatenada en un mesaje
        bool: si el diccionario se encuentra vacio o no se encuentran las claves dentro de la lista
    '''
    mensaje_dato = obtener_dato(personaje, caracteristica)
    mensaje_nombre = obtener_nombre(personaje)

    if mensaje_dato == False or mensaje_nombre == False:
        return False
    
    return mensaje_nombre + " | " + mensaje_dato

#---------------------
def obtener_maximo(lista_personajes:list, caracteristica:str) -> int | float | bool: # 3 4
    ''' devuelve un numero maximo de una caracteristica espeficada por parametro
    Args:
        lista_personajes(list): lista de diccionarios que representa los personajes 
        caracteristica(str): clave del diccionario de personajes que representa el valor a obtener el maximo
                            el valor de la clave debe ser un int(entero) o float(flotante)
    
    Return: 
        int/float: valor maximo obtenido
        false: si los valores de la claves no son str(cadena de caracteres)
    '''

    if not lista_personajes:
        return False
    
    bandera_primera_entrada = True
    maximo = None

    for superheroe in lista_personajes:

        if type(superheroe[caracteristica]) != int and type(superheroe[caracteristica]) != float:
            return False

        if bandera_primera_entrada or superheroe[caracteristica] > maximo:
            maximo = superheroe[caracteristica]
            bandera_primera_entrada = False

    return maximo
  

def obtener_minimo(lista_personajes:list, caracteristica:str) -> int | float | bool: # 5 6
    ''' devuelve un numero minimo de una caracteristica espeficada por parametro
    Args:
        lista_personajes(list): lista de diccionarios que representa los personajes 
        caracteristica(str): clave del diccionario de personajes que representa el valor a obtener el minimo
                            el valor de la clave debe ser un int(entero) o float(flotante)
    
    Return: 
        int/float: valor minimo obtenido
        false: si los valores de la claves no son str(cadena de caracteres)
    '''
    if not lista_personajes:
        return False
    
    bandera_primera_entrada = True
    minimo = None

    for superheroe in lista_personajes:

        if type(superheroe[caracteristica]) != int and type(superheroe[caracteristica]) != float:
            return False

        if bandera_primera_entrada or superheroe[caracteristica] < minimo:
            minimo = superheroe[caracteristica]
            bandera_primera_entrada = False

            
    return minimo


def obtener_dato_cantidad(lista_personajes:list, valor_buscado: str | int, caracteristica:str) -> list | bool: # 3 4 5 6
    ''' devuelve una lista de diccionarios representando los personajes con una clave(caracteristica) y valor(valor_buscado) espeficifico

    Args:
        lista_personajes(list): lista de diccionarios que representan los personajes
        valor_buscado(int/str/float): valor buscado en los valores de los diccionarios
        caracteristica(str): clave de los diccionarios donde se busca el valor

    Return:
        list: devuelve una lista de diccionarios que representa los personajes que cumplen con las condiciones especificadas
        False: en caso de que UNA de las caracteristicas no se encuentre en los diccionarios de lista_personajes
    '''
    resultado = []

    for personajes in lista_personajes:

        if caracteristica not in personajes:
            resultado =  False
        
        if personajes[caracteristica] == valor_buscado:
            resultado.append(personajes)
    
    return resultado

#----------------------
def stark_imprimir_heroes(lista_personajes: list[dict], titulo:str) -> None | bool: # 3 4 5 6
    """
    devuelve un mensaje estructurado de los diccionarios que representa los personajes

    args:
        lista_personajes(list): lista de diccionarios que representan a los personajes

    Retunr:
        str: datos completos de los diccionarios de una lista
    """
    if type(lista_personajes) == list and lista_personajes:
        mensaje = titulo.upper()
        for personaje in lista_personajes:
            for clave, valor in personaje.items():
                if clave == 'nombre':
                    mensaje += f"\n\n\t{valor.upper()}"
                    continue

                mensaje += f"\n{clave:14} : {valor}"
        print(mensaje)
    else:
        return False


def stark_imprimir_caracteristicas_heroes(dict_caracteristica: dict[list], titulo:str) -> None | bool: # 8 9 10 11
    """
    devuelve un mensaje estructurado de los diccionarios que representa los personajes

    args:
        lista_personajes(list): lista de diccionarios que representan a los personajes

    Return:
        str: datos completos de los diccionarios de una lista
    """
    if type(dict_caracteristica) == dict and dict_caracteristica:
        mensaje = titulo.upper() + "\n"
        for caracteristica, lista_nombre_personajes in dict_caracteristica.items():
            mensaje += f"{caracteristica}: {' - '.join(lista_nombre_personajes)}\n"
        print(mensaje)
    else:
        return False


def stark_imprimir_cantidad_heroes(dict_caracteristica: dict, titulo:str) -> None:
    """
    Imprime la cantidad de héroes por característica.

    Parameters:
        dict_caracteristica (dict): Un diccionario que contiene las características y la cantidad de héroes asociados.
        titulo (str): El título que se imprimirá antes de la lista de héroes.

    Returns:
        None
    """

    mensaje = titulo.upper() + "\n"
    for caracteristica, cantidad in dict_caracteristica.items():
        mensaje += f"{caracteristica:15} : {cantidad} heroes\n"
    print(mensaje)

#----------------------
def sumar_datos_heroes(lista_personajes:list, caracteristica:str) -> int | bool:
    '''
    devuelve la suma de todos los valores que posean una caracteristica

    Args:
        lista_personajes(list): lista de diccionarios que representa los personajes
        caracteristica(str): clave de los diccionarios que representa los personajes (altura, peso, fuerza)
    
    Return:
        int/float: representa la suma total de los valores que estan asociados a las caracteristicas
        False: si la lista esta vacia o si la caracteristica buscada no es un int(entero) o float(flotante)
    '''
    suma_total = 0
    for personaje in lista_personajes:

        if type(personaje) != dict or not personaje or (type(personaje[caracteristica]) != int and type(personaje[caracteristica]) != float):
            return False
        
        suma_total += personaje[caracteristica]

    return suma_total


def dividir(dividendo:float, divisor:float) -> float | bool:
    ''' devuelve la division entre un dividendo y un divisor

    Args:
        dividendo(float): valor el cual se va a dividir 
        divisor(float): valor numerico distinto de 0

    Return:
        float: numero que representa la division entre los argumentos
        false: en caso de que el divisor sea 0
    '''
    if divisor == 0:
        return False
    
    return dividendo / divisor
    

def calcular_promedio(lista_personajes:list, caracteristica:str) -> float | bool:
    '''devuelve el promedio entre el acumulado de una caracteristica especificada y su cantidad

    Args:
        lista_personajes(list): lista de diccionarios que representa los personajes
        caracteristica(str): clave de los diccionarios que representa los personajes (altura, peso, fuerza)

    Return:
        float: promedio de los valores pasados como parametro
    '''

    sumatoria = sumar_datos_heroes(lista_personajes, caracteristica)
    contador = 0

    if sumatoria == False:
        return False
    
    for personaje in lista_personajes:
        if type(personaje) != dict or not personaje:
            return False
        
        contador += 1

    return dividir(sumatoria, contador)


def mostrar_promedio_dato(lista_personajes:list, caracteristica:str)-> float | bool: # 7
    '''imprime en terminal el promedio de la caracteristica pasada por parametro
    
    Args:
        lista_personajes(list): lista de diccionarios que representa los personajes
        caracteristica(str): clave de los diccionarios que representa los personajes (altura, peso, fuerza)
    
    Return:
        False: si la lista se encuentra vacia o si la caracteristica de los diccionarios dentro de la lista no sea un int(entero) o float(flotante) 
    '''
    if not lista_personajes:
        return False
    
    for personajes in lista_personajes:
        if type(personajes[caracteristica]) != int and type(personajes[caracteristica]) != float:
            return False
        
    print(f"promedio de la lista: {calcular_promedio(lista_personajes, caracteristica):.2f}")

#---------------------
def imprimir_menu() -> None:
    '''imprime terminal el menu de opciones del programa'''

    menu = '''DESAFIO STARK
    1. Normalizar datos (No se debe poder acceder a los otros puntos)
    2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
    3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    5. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
    6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
    7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
    8. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    9. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    10. Listar todos los superhéroes agrupados por color de ojos.
    11. Listar todos los superhéroes agrupados por tipo de inteligencia
    '''
    print(menu)


def validar_entero(numero:str) -> bool:
    '''devuelve un valor booleano que indica si es correcto el valor ingresado por terminal

    Args:
        numero(str): cadena de caracteres que debe contener valores enteros no negativos

    Return:
        True: si numero representa un entero positivo o cero.
        False: caso contrario
    '''
    if not numero.isdigit():
        return False
    
    return True
    

def stark_menu_principal() -> int | bool:
    '''imprime en pantalla el menu y valida la entrada de datos por input
    
    Args:
        None

    Return:
        int: devuelve un numero entero
        false: en caso de que el numero ingresado no sea entero positivo
    '''
    imprimir_menu()
    entrada = input("ingrese una opcion: ")

    if entrada == 'x':
        return entrada

    if not validar_entero(entrada):
        return False

    return int(entrada)


#PERSONAL
def obtener_dato_contador(lista_personajes:list, caracteristica:str) -> dict | bool: # 8 9
    '''devuelve un diccionario donde la clave indica la caracteristica y el valor la cantidad de personajes que tienen dicha caracteristica

    args:
        lista_personajes(list): lista de diccionarios que representa los personajes
        caracteristica(str): clave de los diccionarios que representa los personajes ('empresa', 'genero', 'color_ojos', 'color_pelo', 'inteligencia')
    
    Return: 
        dict: diccionario de caracteristicas 
        false: si por lo menos una caracteristica especificada no se encuentra en el diccionario
    '''
    dict_salida = {}

    for personajes in lista_personajes:
        caracteristica_normalizada = str(personajes[caracteristica]).capitalize()
        
        if caracteristica not in personajes:
            return False

        if caracteristica_normalizada not in dict_salida:
            if caracteristica_normalizada == "":
                continue
            dict_salida[caracteristica_normalizada] = 1
        else:
            dict_salida[caracteristica_normalizada] += 1

            
        
    return dict_salida


def obtener_personaje_caracteristica(lista_personajes:list, caracteristica:str) -> dict: #10 11
    '''devuelve un diccionario cuya clave son las caracteristica especificada y sus valores un diccionario de personajes

    Args:
        lista_personajes(list): lista de diccionarios que representa los personajes
        caracteristica(str): clave de los diccionarios que representa los personajes

    Return:
        dict: diccionario de caracteristicas
        false: si por lo menos una de las caracteristicas no se encuentra en los diccionarios
    '''

    dict_salida = {}

    for personajes in lista_personajes:

        caracteristica_normalizada = str(personajes[caracteristica]).capitalize()
        if caracteristica not in personajes:
            return False

        if caracteristica_normalizada not in dict_salida:
            if caracteristica_normalizada == "":
                continue
            dict_salida[caracteristica_normalizada] = []
        dict_salida[caracteristica_normalizada].append(personajes['nombre'])

    return dict_salida

#-----------------------------------------------------
def stark_marvel_app(lista_personajes:list) -> None:
    '''inicio de programa Stark Industries
    
    Args:
        lista_personajes: lista de diccionarios que representan a los personajes

    Return:
        None
    '''
    lista_superheroes_M = obtener_dato_cantidad(lista_personajes, 'M', 'genero')
    lista_superheroes_F = obtener_dato_cantidad(lista_personajes, 'F', 'genero')
    lista_superheroes_NB = obtener_dato_cantidad(lista_personajes, 'NB', 'genero')
    
    estado_normalizado_lista = None
    while True:
        opcion = stark_menu_principal()
        match opcion:
            case 'x': #salir del programa
                break
            case 1: #normalizado de datos
                estado_normalizado_lista = stark_normalizar_datos(lista_personajes)
                if estado_normalizado_lista:
                    print("Datos Normalizados")
                else: 
                    print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")
            case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11: #opciones de programa 
                if estado_normalizado_lista is not None:
                    match opcion:
                        case 2: # Nombre de superheroes NB
                            mensaje = ''
                            for personajes in lista_superheroes_NB:
                                if obtener_nombre_y_dato(personajes, 'genero') != False:
                                    mensaje += obtener_nombre_y_dato(personajes, 'genero') + '\n'
                            print(f"nombre de superheroes NB:\n{mensaje}")

                        case 3: # superhéroe más alto de género F
                            lista_superheroes_altos_F = obtener_dato_cantidad(lista_superheroes_F, obtener_maximo(lista_superheroes_F, "altura"), "altura")
                            if lista_superheroes_altos_F != False:
                                stark_imprimir_heroes(lista_superheroes_altos_F, "lista de superheores altos de genero Femenino:")
                            else:
                                print('error. no se ha podido acceder a los datos')

                        case 4: # superhéroe más alto de género M
                            lista_superheroes_altos_M = obtener_dato_cantidad(lista_superheroes_M, obtener_maximo(lista_superheroes_M, "altura"), "altura")
                            if lista_superheroes_altos_M != False:
                                stark_imprimir_heroes(lista_superheroes_altos_M, "lista de los superheroes mas altos de genero masculino:")
                            else:
                                print('error. no se ha podido acceder a los datos')

                        case 5: # superhéroe más débil de género M
                            lista_superheroes_debil_M = obtener_dato_cantidad(lista_superheroes_M, obtener_minimo(lista_superheroes_M, "fuerza"), "fuerza")
                            if lista_superheroes_debil_M != False:
                                stark_imprimir_heroes(lista_superheroes_debil_M, "lista de superheroes mas debiles de genero Masculino:")
                            else:
                                print('error. no se ha podido acceder a los datos')

                        case 6: # superhéroe más débil de género NB
                            lista_superheroes_debil_NB = obtener_dato_cantidad(lista_superheroes_NB, obtener_minimo(lista_superheroes_NB, "fuerza"), "fuerza")
                            if lista_superheroes_debil_NB != False:
                                stark_imprimir_heroes(lista_superheroes_debil_NB, "lista de superheroes de genero NB mas debiles:")
                            else:
                                print('error. no se ha podido acceder a los datos')

                        case 7: # fuerza promedio de los superhéroes de género NB
                            mostrar_promedio_dato(lista_superheroes_NB, 'fuerza')

                        case 8: # superhéroes por tipo de color de ojos.
                            cantidad_por_ojos = obtener_dato_contador(lista_personajes, 'color_ojos')
                            if cantidad_por_ojos != False:
                                stark_imprimir_cantidad_heroes(cantidad_por_ojos, "superheroes por tipo de color de ojos")
                            else:
                                print('error. no se ha podido acceder a los datos')

                        case 9: # superhéroes por tipo de color de pelo.
                            cantidad_por_pelo = obtener_dato_contador(lista_personajes, 'color_pelo')
                            if cantidad_por_pelo != False:
                                stark_imprimir_cantidad_heroes(cantidad_por_pelo, "superhéroes por tipo de color de pelo.")
                            else:
                                print('error. no se ha podido acceder a los datos')

                        case 10: # superhéroes agrupados por color de ojos.
                            heroes_color_ojos = obtener_personaje_caracteristica(lista_personajes, 'color_ojos')
                            if heroes_color_ojos != False:
                                stark_imprimir_caracteristicas_heroes(heroes_color_ojos, "superhéroes agrupados por color de ojos.")
                            else:
                                print('error. no se ha podido acceder a los datos')
                            
                        case 11: # superhéroes agrupados por tipo de inteligencia
                            heroes_inteligencia = obtener_personaje_caracteristica(lista_personajes, 'inteligencia')
                            if heroes_inteligencia != False:
                                stark_imprimir_caracteristicas_heroes(heroes_inteligencia, "superhéroes agrupados por tipo de inteligencia")
                            else:
                                print('error. no se ha podido acceder a los datos')
                else: 
                    print('los datos no han sido normalizados')
            case _:
                print('eleccion fuera de rango')