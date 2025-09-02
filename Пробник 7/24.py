f = open("Задание 24.txt").readline()
k = "FSWY"
while k+"FSWY" in f:
    k+="FSWY"
k = "SWY"+k+"FSW"
print(len(k))