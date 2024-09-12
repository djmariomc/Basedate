import csv

FILENAME = "users.csv"

print("Name 'Nickname' - Age")
users = [
    ["DjMarioMc 'the Oldman'", 37],
    ["Bon-Bon 'la Chica'", 20],
    ["Helen 'the Blond'", 21]
]

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, "a", newline="") as file:
    user = ["Sancho 'Egghead'", 25]
    writer = csv.writer(file)
    writer.writerow(user)

FILENAME = "users.csv"

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])

