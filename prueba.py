import pandas as pd
def registro_programa(programa, indice):
    ruta_programa = f"programas/{programa}.csv"
    df = pd.read_csv(ruta_programa, encoding="utf-8")
        # Verificar si el número de filas actuales excede el límite
    if len(df) >= 6:
        print(f"LO SENTIMOS NO PUEDE REGISTRARSE EN EL PROGRAMA DE {programa} PORQUE HA ALCANZADO EL LIMITE DE REGISTROS POSIBLES")
        return False
    
    nombre = input("Por favor inserte su nombre: ")
    apellido = input("Por favor inserte su apellido: ")
    
    datos = [{"nombre": nombre, "apellido": apellido}]
    
    df_nuevo = pd.DataFrame(datos)
    
    # debemos concatenar los nuevos datos
    
    df = pd.concat([df, df_nuevo], ignore_index=True)
    df.to_csv(ruta_programa, encoding='utf-8', index=False)
    print(f"SU REGISTRO FUE COMPLETADO CON EXITO USTED SE HA REGISTRADO EN EL PROGRAMA DE {programa}")
    cuestion = input(f"¿DESEA VOLVER A CREAR OTRA CUENTA EN EL PROGRAMA DE {programa}(si/no)?: ").lower()
    if cuestion == "si":
        return registro_programa(programa)
    else:
        print("VOLVIENDO AL MENU PRINCIPAL...")
    return programa
registro_programa("informatica", 0)