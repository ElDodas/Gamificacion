def get_code(file, code):
    
    try: 
        f = open(file, "r")
    except FileNotFoundError:
        print(f"\t¡El fichero {file} no existe!\n")
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(",")) for line in directory])
        if code in directory:
            print(f"\t---> {directory[code]}")
        else:
            print(f"¡El código {code} no existe!\n")


def add_code(file, code, codigo):
    
    try: 
        f = open(file, "a")
    except FileNotFoundError:
        print(f"\t¡El fichero {file} no existe!\n")
    else:
        f.write(code + "," + codigo + "\n")
        f.close()
        print("\tEl código se ha añadido.\n")

def remove_code(file, code):
    
    try: 
        f = open(file, "r")
    except FileNotFoundError:
        return(f"\t¡El fichero  {file} no existe!\n")
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(",")) for line in directory])
        if code in directory:
            del directory[code]
            f = open(file, "w")
            for name, codigo in directory.items():
                f.write(name + "," + codigo)
            f.close()
            print(f"\t¡El cliente se ha borrado!\n")
        else:
            print(f"\t¡El cliente {code} no existe!\n")


def create_directory(file):
    
    import os
    if os.path.isfile(file):
        answer = input(f"\tEl fichero {file} ya existe. ¿Desea vaciarlo (S/N)?:\t")
        if answer == "N": 
            return f"\tNo se ha creado el fichero porque ya existe.\n"
    f = open(file, "w")
    f.close()
    print("\tSe ha creado el fichero\n")

def menu():
    
    print(f"\tGestión de códigos")
    print(f"\t============================")
    print(f"\t1 - Consultar código de identificación")
    print(f"\t2 - Añadir código de un sistema nuevo")
    print(f"\t3 - Eliminar código")
    print(f"\t4 - Crear el gestor de códigos")
    print(f"\t0 - Terminar")
    option = input("\n\tIntroduce una opción:\t")
    return option


def directory():
    
    file = "listin.txt" 
    while True:
        option = menu()
        if option == "1":
            name = input("\tIntroduce el nombre del sistema:\t")
            print(get_code(file, name))
        elif option == "2":
            name = input("\tIntroduce el nombre del sistema:\t")
            codigo = input("\tIntroduce el código del sistema:\t")
            print(add_code(file, name, codigo))
        elif option == "3":
            name = input("\tIntroduce el nombre del sistema:\t")
            print(remove_code(file, name))
        elif option == "4":
            print(create_directory(file))
        else:
            break

directory()