def segundo_ataque():
    
    lista_nums = []

    while True:
        
        num = input(f"Introduce un número o letra:\t")

        lista_nums.append(num)
        
        stop = input(f"\tQuieres introducir otro número (y / n):\t").lower()

        if stop.startswith("n"):
            break

    print(f"\n\t{set(lista_nums)}\n")

segundo_ataque()