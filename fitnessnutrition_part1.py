import os
times = 3
max_comb = 600
form = 1
DCI = 0
PATH = "Readme.txt"
recipes = []
days = []
allergy_free = []
height = 150
weight = 50
gender = 'female'
age = 25
physical_activity = 2
not_food = 'Fish,;;;:   miLK'
chosen_option = 1

def less(a, b):
    global days
    global allergy_free
    DCI_a = 0
    for i in range(0, len(days[a])):
        DCI_a += int(allergy_free[days[a][i]][1])
    DCI_b = 0
    for i in range(0, len(days[b])):
        DCI_b += int(allergy_free[days[b][i]][1])

    if abs(DCI_a - DCI) < abs(DCI_b - DCI):
        return True
    else:
        return False

def init():
    global PATH
    try:
        f = open(PATH, "r")
    except:
        print("No input/output file is found")
        print("please open the program and change the PATH")
        exit()

    global recipes

    m = int(f.readline())
    recipes = [0] * m
    for i in range(0, m):
        recipes[i] = [0, 0, 0, 0]

    for i in range(0, m):
        s = f.readline().split()
        recipes[i][0] = s[0]
        recipes[i][1] = s[1]
        recipes[i][2] = [0] * int(s[2])
        recipes[i][3] = int(s[3])

        for j in range(0, int(s[2])):
            recipes[i][2][j] = f.readline().split()[0]


    f.close()

def create_days():
    global allergy_free
    global max_comb
    days_local = []
    for i in range(0, len(allergy_free)):
        if allergy_free[i][3] == 0:
            continue
        for j in range(i + 1, len(allergy_free)):
            for k in range(j + 1, len(allergy_free)):
                days_local.append([i, j, k])
                if len(days_local) >= max_comb:
                    break
                for k2 in range(k + 1, len(allergy_free)):
                    days_local.append([i, j, k, k2])
                    if len(days_local) >= max_comb:
                        break
                    # if len(days_local) < max_comb:
                    # for g in range(k2 + 1, len(allergy_free)):
                    # days_local.append([i, j, k, k2, g])
                    # if len(days_local) >= max_comb:
                    # break
    return days_local

def my_sort(data):
    for i in range(0, len(data)):
        for j in range(0, len(data) - 1):
            if less(j, j + 1) == False:
                a = data[j + 1]
                data[j + 1] = data[j]
                data[j] = a

    return data

