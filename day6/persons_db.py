import csv

with open("persons.csv", mode="w+") as db_file:
    # writer = csv.writer(db_file)
    writer = csv.DictWriter(db_file, fieldnames=["name", "age"])
    writer.writeheader()

    # writer.writerow(["Victor", 10])
    # writer.writerow(["Kiki", 20])
    writer.writerow({ "name": "Victor", "age": 23 })
    writer.writerow({ "name": "Kiki", "age": 17 })
    writer.writerow({ "name": "Damian", "age": 21 })
    writer.writerow({ "name": "Karina", "age": 22 })


with open("persons.csv", mode="r") as db_file:
    reader = csv.DictReader(db_file, fieldnames=["name", "age"])
    next(reader, None)

    sum_ages = 0
    count = 0
    for row in reader:
        age = row.get("age")
        sum_ages += int(age)
        count += 1
    
    average = sum_ages / count
    print("Average age is " + str(average))