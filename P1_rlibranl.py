def string_function():

    string = input(f"\tIntroduce una cadena:\t")
    print(f"\t--> Los 2 primeros caracteres son: {string[0:2]}")
    print(f"\t--> Los 3 últimos caracteres son: {string[-3:]}")
    print(f"\t--> Cada 2 caracteres: {string[::2]}")
    print(f"\t--> Sentido normal y sentido inverso: {string[:]}{string[::-1]}")

string_function()