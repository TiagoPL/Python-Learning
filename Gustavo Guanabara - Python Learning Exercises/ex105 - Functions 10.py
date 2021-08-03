def grades(*n, sit=True):
    my_dict = {}
    my_dict["Number of Grades"] = len(n)
    my_dict["Highest Grade"] = 0
    my_dict["Minor Grade"] = 999

    for n1 in n:
        if n1 > my_dict["Highest Grade"]:
            my_dict["Highest Grade"] = n1

    for n1 in n:
        if n1 < my_dict["Minor Grade"]:
            my_dict["Minor Grade"] = n1

    my_sum = 0
    for n2 in n:
        my_sum = my_sum + n2
    media = my_sum / len(n)
    my_dict["Media"] = float(f'{media:.2f}')

    if sit == True:
        if my_dict["Media"] >= 5:
            my_dict["SITUATION"] = 'SITUATION GOOD'
        else:
            my_dict["SITUATION"] = 'BAD SITUATION'

    print(my_dict)


grades(4, 5, 6, 7, 1, 9, sit=False)
