liste = [30,15,19,50,0,1]

def pair_dans_liste (arr):
    list_even = []
    list_odd = []

    for num in arr:
        if (num % 2) == 0:
            list_even.append(num)
        else:
            list_odd.append(num)

    return list_even

print(pair_dans_liste(liste))