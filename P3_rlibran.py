def tercer_ataque():

    gadgets = ["Batería", "Portátil", 100, "Ordenador central", 310.28,"Altavoces", 27.00, "Pantalla", 1000, "Maletín electrónico", "Lente de cámara"]
    numbers = []
    strings = []

    for i in gadgets:
        if type(i) == float or type(i) == int:
            numbers.append(i)
        else:
            strings.append(i)

    print(f"\n\tStrings ordenadas en ascenso:\t {sorted(strings)}")
    print(f"\tStrings ordenadas en ascenso:\t {sorted(strings, reverse = True)}")
    print(f"\tNúmeros ordenados de menor a mayor: {sorted(numbers, reverse = True)}")
    print(f"\tNúmeros ordenados de mayor a menor: {sorted(numbers)}\n")

tercer_ataque()
