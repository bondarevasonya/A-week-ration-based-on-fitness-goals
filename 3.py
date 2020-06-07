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
    print('Now you need to choose your goal!')
    print("Print 1 if you want to lose weight")
    print("Print 2 if you want to maintain your body weight")
    print("Print 3 if you want to gain weight")
    chosen_option_local = int(input())
    return [height_local, weight_local, gender_local, age_local, physical_activity_local, not_food_local,
            chosen_option_local]


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

BM = 10 * weight + 6.25 * height + 5 * age + 5
if gender == 'female':
    BM -= 156
DCI = BM * 1.2
if physical_activity == 1:
    DCI = BM * 1.2
elif physical_activity == 2:
    DCI = BM * 1.375
elif physical_activity == 3:
    DCI = BM * 1.55

if chosen_option == 1:
    DCI = DCI - 200
elif chosen_option == 3:
    DCI = DCI + 200
DCI = int(DCI)

init()

for i in range(0, len(recipes)):
    cnt = 0
    for j in range(0, len(recipes[i][2])):
        if recipes[i][2][j] in not_food:
            cnt = 1
    if cnt == 0:
        allergy_free.append(recipes[i])

days = create_days()

print('Please wait, sorting in progress')
days = my_sort(days)
print('Sorting finished')
chosen_days = create_chosen_days(days)
print('Chosen days finished')

while True:
    print('Print 1 for all available recipes')
    print('Print 2 for allergy free recipes')
    print('Print 3 for recommended daily calorie input')
    print("Print 4 for recommended nutrition program for a week")
    print("Print 5 for exit")
    option = int(input())

    if option == 1:
        for i in range(0, len(recipes)):
            print(recipes[i][0], recipes[i][1])
            for j in range(0, len(recipes[i][2])):
                print(recipes[i][2][j], end=" ")
            print()
            print()

    elif option == 2:
        for i in range(0, len(allergy_free)):
            print(allergy_free[i][0], allergy_free[i][1])
            for j in range(0, len(allergy_free[i][2])):
                print(allergy_free[i][2][j], end=" ")
            print()
            print()

    elif option == 3:
        print(DCI)
        print()

    elif option == 4:
        x = len(chosen_days)
        if x == 0:
            print('Unfortunately, no such foods available')
            continue
        for i in range(0, 7):
            i0 = chosen_days[i % x][0]
            i1 = chosen_days[i % x][1]
            i2 = chosen_days[i % x][2]
            print('Day', i + 1)
            print()
            print('Breakfast:', end=" ")
            print(allergy_free[i0][0], allergy_free[i0][1])
            if len(chosen_days[i % x]) > 3:
                print('Brunch:', end=" ")
                print(allergy_free[chosen_days[i % x][3]][0], allergy_free[chosen_days[i % x][3]][1])
            print('Lunch:', end=" ")
            print(allergy_free[i1][0], allergy_free[i1][1])
            print('Diner:', end=" ")
            print(allergy_free[i2][0], allergy_free[i2][1])
            if len(chosen_days[i % x]) > 4:
                print('Second dinner:', end=" ")
                print(allergy_free[chosen_days[i % x][4]][0], allergy_free[chosen_days[i % x][4]][1])
            print()

    elif option == 5:
        break
