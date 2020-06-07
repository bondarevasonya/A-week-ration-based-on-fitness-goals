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


def create_chosen_days(days):
    hmt = [0] * len(allergy_free)
    chosen_days = []
    for i in range(0, len(days)):
        cnt = 0
        for j in range(0, len(days[i])):
            i0 = days[i][j]
            if hmt[i0] < times:
                cnt += 1
        if cnt == len(days[i]):
            chosen_days.append(days[i])
            for k in range(0, len(days[i])):
                hmt[days[i][k]] += 1

        if len(chosen_days) == 7:
            break
    return chosen_days

def is_letter(x):
    if ord(x) >= ord('a') and ord(x) <= ord('z'):
        return 1
    elif ord(x) >= ord('A') and ord(x) <= ord('Z'):
        return 2
    else:
        return 3

def capitalize(data):

    data = data.replace('.', ' ')
    data = data.replace(',', ' ')
    data = data.replace(';', ' ')
    data = data.replace(':', ' ')
    data = data.split()
    new_data = []
    for s in data:
        s1 = ""
        if is_letter(s[0]) == 1:
            s1 = s1 + chr(ord(s[0]) - 32)
        else:
            s1 = s1 + s[0]
        for i in range(1, len(s)):
            if is_letter(s[i]) == 2:
                s1 = s1 + chr(ord(s[i]) + 32)
            else:
                s1 = s1 + s[i]
        new_data.append(s1)
    return new_data


def fill_in_the_form():
    print("Firstly, indicate your height, sm")
    height_local = int(input())
    print('Secondly, indicate your current weight, kg')
    weight_local = int(input())
    print("Indicate your gender, female or male")
    gender_local = input()
    if is_letter(gender_local[0]) == 2:
        s = chr(ord(gender_local[0]) + 32)
        s = s + gender_local[1: len(gender_local)]
        gender_local = s
    print("Indicate your age")
    age_local = int(input())
    print("Indicate your activity level")
    print("1 - no physical activity")
    print("2 - limited physical activity")
    print("3 - high physical activity")
    physical_activity_local = int(input())
    print("Then indicate your allergies or foods you do not eat")
    not_food_local = input()
    print('Now you need to chose your goal!')
    print("Print 1 if you want to lose weight")
    print("Print 2 if you want to maintain your body weight")
    print("Print 3 if you want to gain weight")
    chosen_option_local = int(input())
    return [height_local, weight_local, gender_local, age_local, physical_activity_local, not_food_local, chosen_option_local]



finish = False
while form == 1 and finish == False:
    try:
       personal_data = fill_in_the_form()
       finish = True
    except:
        print('Data is incorrect, try again')
        finish = False
if form == 1:
    height = personal_data[0]
    weight = personal_data[1]
    gender = personal_data[2]
    age = personal_data[3]
    physical_activity = personal_data[4]
    not_food = personal_data[5]
    chosen_option = personal_data[6]
not_food = capitalize(not_food)


