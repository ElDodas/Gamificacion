def atravesando_el_umbral():
    nums = [1,2,3,4,5,6,7,8,9,10]
    lista = []
    
    for i in nums:
        if i == 4 or i == 7 or i == 9:
            lista.append(nums[i] * 2)
        
    for i in lista:
        print(f"\t{i}")

atravesando_el_umbral()