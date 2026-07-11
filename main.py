def leer_opcion():
    opcion_valida = False
    opcion = None
    while not opcion_valida:
        entrada = input("Ingrese opcion: ")
        try:
            opcion = int(entrada)
            if 1 <= opcion <= 6:
                opcion_valida = True
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")
    return opcion


def unidades_categoria(categoria, productos, stock):
    total = 0
    categoria_buscada = categoria.lower()
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria_buscada:
            total += stock[codigo][1]
    print(f"El total de unidades disponibles es: {total}")


def busqueda_precio(p_min, p_max, productos, stock):
    encontrados = []
    for codigo, datos in stock.items():
        precio = datos[0]
        unidades = datos[1]
        if p_min <= precio <= p_max and unidades != 0:
            nombre = productos[codigo][0]
            encontrados.append(f"{nombre}--{codigo}")

    if len(encontrados) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        encontrados.sort()
        print(f"Los productos encontrados son: {encontrados}")


def main():
    productos = {
        'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
        'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
        'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
        'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
        'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
        'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
    }

    stock = {
        'M001': [32990, 12],
        'M002': [9990, 0],
        'M003': [5490, 25],
        'M004': [7990, 5],
        'M005': [11990, 7],
        'M006': [24990, 3],
    }

    continuar = True
    while continuar:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de productos por rango de precio")
        print("3. Actualizar precio de producto")
        print("4. Agregar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        print("=====================================")

        opcion = leer_opcion()

        if opcion == 1:
    	    categoria = input("Ingrese categoría a consultar: ")
    	    unidades_categoria(categoria, productos, stock)        
        
        elif opcion == 2:
            datos_validos = False
            p_min = 0
            p_max = 0
            while not datos_validos:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min < 0 or p_max < 0 or p_min > p_max:
                        print("Debe ingresar valores enteros")
                    else:
                        datos_validos = True
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, productos, stock)

        if opcion == 6:
            print("Programa finalizado.")
            continuar = False


if __name__ == "__main__":
    main()