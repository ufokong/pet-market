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


def buscar_codigo(codigo, stock):
    codigo_buscado = codigo.upper()
    for clave in stock:
        if clave.upper() == codigo_buscado:
            return True
    return False


def actualizar_precio(codigo, nuevo_precio, stock):
    if buscar_codigo(codigo, stock):
        for clave in stock:
            if clave.upper() == codigo.upper():
                stock[clave][0] = nuevo_precio
                return True
    return False


def validar_texto(valor):
    return valor.strip() != ""


def validar_codigo_nuevo(codigo, stock):
    if not validar_texto(codigo):
        return False
    return not buscar_codigo(codigo, stock)


def validar_peso(valor):
    try:
        peso = float(valor)
        return peso > 0
    except ValueError:
        return False


def validar_si_no(valor):
    return valor.lower() in ("s", "n")


def validar_precio(valor):
    try:
        precio = int(valor)
        return precio > 0
    except ValueError:
        return False


def validar_unidades(valor):
    try:
        unidades = int(valor)
        return unidades >= 0
    except ValueError:
        return False


def agregar_producto(codigo, nombre, categoria, marca, peso_kg,
                      es_importado, es_para_cachorro, precio, unidades,
                      productos, stock):
    if buscar_codigo(codigo, stock):
        return False
    productos[codigo] = [nombre, categoria, marca, peso_kg,
                          es_importado, es_para_cachorro]
    stock[codigo] = [precio, unidades]
    return True


def eliminar_producto(codigo, productos, stock):
    if buscar_codigo(codigo, stock):
        clave_real = None
        for clave in stock:
            if clave.upper() == codigo.upper():
                clave_real = clave
        del stock[clave_real]
        del productos[clave_real]
        return True
    return False


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

        elif opcion == 3:
            seguir = "s"
            while seguir == "s":
                codigo = input("Ingrese código del producto: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                except ValueError:
                    print("El código no existe")
                    seguir = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                    continue

                if actualizar_precio(codigo, nuevo_precio, stock):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                seguir = input("¿Desea actualizar otro precio (s/n)?: ").lower()

        elif opcion == 4:
            codigo = input("Ingrese código del producto: ")
            nombre = input("Ingrese nombre: ")
            categoria = input("Ingrese categoría: ")
            marca = input("Ingrese marca: ")
            peso = input("Ingrese peso (kg): ")
            importado = input("¿Es importado? (s/n): ")
            cachorro = input("¿Es para cachorro? (s/n): ")
            precio = input("Ingrese precio: ")
            unidades = input("Ingrese unidades: ")

            if not validar_codigo_nuevo(codigo, stock):
                print("El código ya existe")
            elif not validar_texto(nombre):
                print("El nombre no es válido")
            elif not validar_texto(categoria):
                print("La categoría no es válida")
            elif not validar_texto(marca):
                print("La marca no es válida")
            elif not validar_peso(peso):
                print("El peso no es válido")
            elif not validar_si_no(importado):
                print("El valor de importado no es válido")
            elif not validar_si_no(cachorro):
                print("El valor de para cachorro no es válido")
            elif not validar_precio(precio):
                print("El precio no es válido")
            elif not validar_unidades(unidades):
                print("Las unidades no son válidas")
            else:
                agregado = agregar_producto(
                    codigo, nombre, categoria, marca, float(peso),
                    importado.lower() == "s", cachorro.lower() == "s",
                    int(precio), int(unidades), productos, stock)
                print("Producto agregado" if agregado else "El código ya existe")

        elif opcion == 5:
            codigo = input("Ingrese código del producto: ")
            if eliminar_producto(codigo, productos, stock):
                print("Producto eliminado")
            else:
                print("El código no existe")

        elif opcion == 6:
            print("Programa finalizado.")
            continuar = False


if __name__ == "__main__":
    main()
