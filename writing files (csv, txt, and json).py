import csv
import json
employees = [["Name", "Age", "Job"],
             ["Ted Bundy", 30, "Secret Model"],
             ["Trump", 68, "Pres"],
             ["Scott", 90, "Unemployed"]]

file_path = "/Users/marcusandriano/Desktop/Desktop cleanup/output.csv"

cooldudes = "I like pizza"
file_path_1 = "/Users/marcusandriano/Desktop/Desktop cleanup/output.txt"

cool = {
    "dude" : "carrot",
    "carrot" : "dude"
}
file_path_2 = "/Users/marcusandriano/Desktop/Desktop cleanup/output.json"

try:
    with open(file=file_path, mode= "w") as file:
        write = csv.writer(file)
        for row in employees:
            write.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print("That file already exists!")


try:
    with open(file=file_path_2, mode= "w") as file2:
        json.dump(cool, file2, indent = 4)
        print(f"json file was created")
except FileExistsError:
    print("That file already exists!")


try:
    with open(file=file_path_1, mode= "w") as file1:
        file1.write(cooldudes)
        print(f"txt file was created")
except FileExistsError:
    print("That file already exists!")