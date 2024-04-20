# primero un login y contraseña osea ya tenemos cierta base de datos, y olvidamos usar values jajajaajjajaajaj

import pandas as pd
ruta_datos = "base/cuentas.csv"

def iniciar_sesion():
    # iniciaremos sesion
    df = pd.read_csv(ruta_datos, encoding="utf-8")
    preguntar_usuario = input("Por favor inserte su nombre de usuario: ")
    if preguntar_usuario in df["usuario"].values:
        indice = df[df["usuario"] == preguntar_usuario].index[0]
        comprobar_password(indice, df)
    else:
        print("SU USUARIO NO FUE ENCONTRADO POR FAVOR VUELVA A INTENTARLO")
        iniciar_sesion()
        
        
def comprobar_password(index, dataframe, conteo_intentos=0):
    df = pd.read_csv(ruta_datos, encoding="utf-8")
    password = input("Su usuario fue encontrado ahora inserte su contraseña: ")
    if df.loc[index, "password"] == password:
        print("INICIO DE SESION EXITOSO")
        programa(index)
        return 0  # No hay intentos fallidos, por lo que se reinicia el contador
    else:
        conteo_intentos += 1 # sumamos uno
        print("INICIO DE SESION FALLIDO INTENTE DE NUEVO") # si llega a fallar
        
        if conteo_intentos > 2: # ignorado hasta tener el valor nuevo
            conteo_intentos = 0
            bloquear_usuario(index)
            
        else:
            conteo_intentos = comprobar_password(index, dataframe, conteo_intentos) # tambien se ejecuta en este caso
    return conteo_intentos
        
def bloquear_usuario(index):
    # Suponiendo que tienes la variable ruta_datos definida anteriormente
    
    # Cargar los datos originales y la lista de cuentas bloqueadas
    df = pd.read_csv(ruta_datos, encoding="utf-8")
    df_block = pd.read_csv("base/cuentas_block.csv", encoding="utf-8")
    
    # Copiar los datos de la cuenta bloqueada
    cuenta = df.iloc[index].copy()
    
    # Formatear los datos para crear un nuevo DataFrame
    cuenta_format = {"usuario": [cuenta["usuario"]], "password": [cuenta["password"]]}
    df_nuevo = pd.DataFrame(cuenta_format)
    
    # Concatenar los datos de la cuenta bloqueada al DataFrame de cuentas bloqueadas
    df_block = pd.concat([df_block, df_nuevo], ignore_index=True) # basicamente buscamos que cuando se concatene se use correctamente concat especificando la base correctamente y no otra variables ah
    
    # Guardar el DataFrame actualizado de cuentas bloqueadas
    df_block.to_csv("base/cuentas_block.csv", encoding='utf-8', index=False)
    
    # Eliminar la cuenta bloqueada del DataFrame original
    df_cuenta_eliminada = df.drop(index)
    df_cuenta_eliminada.to_csv(ruta_datos, encoding='utf-8', index=False)
    
    print("CUENTA BLOQUEADA POR MUCHOS INTENTOS")
    print("SALIENDO DEL SISTEMA...")

def programa(index):
    print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
    print("                          ¡BIENVENID@ AL MENU PRINCIPAL!")
    print("｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
    print("1. Informática")
    print("2. Medicina")
    print("3. Marketing")
    print("4. Artes")
    print("5. Salir")
    seleccion = int(input("SELECCIONE UNO DE LOS PROGRAMAS: "))
    if seleccion == 1:
        confirmacion = input("¿DESEA REGISTRARSE EN EL PROGRAMA DE INFORMATICA? (si/no)?: ").lower()
        if confirmacion == "si":
            registro_programa("informatica", index)
        else:
            print("REGRESANDO A LA SELECCION...")
            programa = programa(index)
            return programa
    elif seleccion == 2:
        confirmacion = input("¿DESEA REGISTRARSE EN EL PROGRAMA DE MEDICINA? (si/no)?: ").lower()
        if confirmacion == "si":
            registro_programa("medicina", index)
        else:
            print("REGRESANDO A LA SELECCION...")
            programa = programa(index)
            return programa
    elif seleccion == 3:
        confirmacion = input("¿DESEA REGISTRARSE EN EL PROGRAMA DE MARKETING? (si/no)?: ").lower()
        if confirmacion == "si":
            registro_programa("marketing", index)
        else:
            print("REGRESANDO A LA SELECCION...")
            programa = programa(index)
            return programa
    elif seleccion == 4:
        confirmacion = input("¿DESEA REGISTRARSE EN EL PROGRAMA DE ARTES? (si/no)?: ").lower()
        if confirmacion == "si":
            registro_programa("artes", index)
        else:
            print("REGRESANDO A LA SELECCION...")
            programa = programa(index)
            return programa
    else:
        print("SALIENDO DEL PROGRAMA...")
    return True

def registro_programa(nombre_programa, indice):
    ruta_programa = f"programas/{nombre_programa}.csv"
    df = pd.read_csv(ruta_programa, encoding="utf-8")
        # Verificar si el número de filas actuales excede el límite
    if len(df) >= 6:
        print(f"LO SENTIMOS NO PUEDE REGISTRARSE EN EL PROGRAMA DE {nombre_programa} PORQUE HA ALCANZADO EL LIMITE DE REGISTROS POSIBLES")
        return False
    
    nombre = input("Por favor inserte su nombre: ")
    apellido = input("Por favor inserte su apellido: ")
    
    datos = [{"nombre": nombre, "apellido": apellido}]
    
    df_nuevo = pd.DataFrame(datos)
    
    # debemos concatenar los nuevos datos
    
    df = pd.concat([df, df_nuevo], ignore_index=True)
    df.to_csv(ruta_programa, encoding='utf-8', index=False)
    print(f"SU REGISTRO FUE COMPLETADO CON EXITO USTED SE HA REGISTRADO EN EL PROGRAMA DE {nombre_programa}")
    cuestion = input(f"¿DESEA VOLVER A CREAR OTRA CUENTA EN EL PROGRAMA DE {nombre_programa} (si/no)?: ").lower()
    if cuestion == "si":
        registro_programa = registro_programa(nombre_programa, indice)
        return registro_programa
    else:
        print("VOLVIENDO AL MENÚ PRINCIPAL...")
        programa(indice)  # Llamada correcta a la función programa

iniciar_sesion()
