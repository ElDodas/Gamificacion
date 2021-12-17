def primer_ataque():
    from num2words import num2words

    
    lista_nums = []
    sum_total = 0
    while True:
        
        num = int(input(f"Introduce un número entre 10 y 99:\t"))

        if num > 9 and num < 100:
            lista_nums.append(num)
            sum_total += num
        
        stop = input(f"\tQuieres introducir otro número (y / n):\t").lower()

        if stop.startswith("n"):
            break

    print(f"\tLa suma de los números es {num2words(sum_total)}")
    print(f"\tLa suma de los números multiplicados x 9 es: {num2words(sum_total * 9)}")
    print(f"\tEl mayor número es {num2words(max(lista_nums))} y el menor es {num2words(min(lista_nums))}")
    print(f"\tHas introducido {num2words(len(lista_nums))} números")

primer_ataque()