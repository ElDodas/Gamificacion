n = int(input(f"\n\tIntroduce un número entre 1 y 10:\t"))
tabla = f"tabla-{str(n)}.txt"
fichero = open(tabla, "w")
for i in range(1, 11):
    fichero.write(f"\t{str(n)} x {str(i)} = {str(n * i)}\n")
fichero.close()