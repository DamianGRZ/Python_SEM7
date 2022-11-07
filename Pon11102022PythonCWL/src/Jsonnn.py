from pathlib import Path
import json

def Json():
    ContinueFile = True
    while ContinueFile:
        fileName = input("Enter name of the file you want to change: ")
        try:
            with open(fileName, "r") as json_file:
                json_object = json.load(json_file)
        except:
            print("File with that name does not exist")  
            break

        print(json.dumps(json_object, indent=1))  # print existing file

        # Make a choice
        data = input("Do you want to add or remove record? [a or r]: ")

        if data == "a" or data == "A":
            Add_record()
        elif data == "r" or data == "R":
            Delete_record(json_object)
        else:
            print("Incorrect input")
            continue  # In the case of incorrect input continue the program

        print("Do you want to continue [y or n]: ")
        cont = input()
        if cont == "y" or cont == "Y":
            ContinueFile = True
        elif cont == "n" or cont == "N":
            ContinueFile = False
        else:
            print("Incorrect input")
            continue  # In the case of incorrect input continue the program


def Delete_record(json_object):
    data = input("What record to delete {enter car name}: ")
    for i in range(0, len(json_object["cars"])):
        if json_object["cars"][i]["Car Name"] == data:
            json_object["cars"].pop(i)
            print(json.dumps(json_object, indent=1))
            break
    Write_to_file_del("Cars.json",json_object)

def Add_record():
    carName = input("Car Name: ")
    carModel = input("Car Model: ")
    carMaker = input("Car Maker: ")
    carPrice = input("Car Price: ")
    entry = {"Car Name" : carName, "Car Model" : carModel, 
             "Car Maker" : carMaker, "Car Price" : carPrice}
    Write_to_file_add("Cars.json", entry)

def Write_to_file_add(filename, newData):
    with open(filename, "r+") as json_file:
        json_object = json.load(json_file)
        json_object["cars"].append(newData)
        json_file.seek(0)
        json.dump(json_object, json_file, indent=1)
        
def Write_to_file_del(filename, Data):
    with open(filename, "w") as json_file:
        json.dump(Data, json_file, indent=1)
# EX6
if __name__ == "__main__":
    Json()
