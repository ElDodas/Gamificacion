n = int(input(f"\n\tIntroduce un número entre 1 y 10:\t"))
tabla = f"tabla-{str(n)}.txt"
try: 
    fich = open(tabla, "r")
except FileNotFoundError:
    print(f"\n\tNo existe el archivo con la tabla del {n}")
else:
    print(f"\n{fich.read()}")