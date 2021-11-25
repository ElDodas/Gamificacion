def mapa_de_calor():

    string = input(f"\t --> Introduce una palabra:\t")


    for i in range(len(string)):

        if i == len(string)-1:
            print(f"{string[i]}")
        elif i == 0:
            print(f"\t Tu cadena es => {string[i]}", end=", ")
        else:
            print(f"{string[i]}", end=", ")

mapa_de_calor()