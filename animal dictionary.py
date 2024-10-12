fObj = open("animalNames.txt")
d = {}
'''
hippo : calf
horse : foal
dog : pup
kangaroo : joey
monkey : infant
owl : owlet
parrot : chick
rabbit : bunny
rat : pup
cow' : calf
skunk : kit
sheep : lamb
cat : kitten
'''

with open("animalNames.txt", 'r') as file:
    for line in file:
        f = line.split(":")
        d.update({f[0].strip(): f[1].strip()})
print(d)


programFunction = int(input("""What would you like this program to do?
1) Find an baby animals name
2) Add another animal's name to the dictionary
3) Delete another animal's name
4) Exit
:"""))

while programFunction != 4:
    if programFunction == 1:
        print("1) Find an baby animals name")
        animal = input("what animal are you looking for?")
        animal = animal.lower()
        if animal in d :
            print ( "The baby name of " + animal + " is", d[animal])
        else:
            print ("Name is not in dictionary")
            newEntry = input("Do you want to add an entry to the dictionary? ")
            if newEntry == "yes":
                print("""What do you want to add to the dictionary?
You must provide a baby name and an animal name.""")

                animalName = input("What is the animal's name: ")
                animalName = animalName.lower()

                babyName = input("What is the baby animal's name: ")
                d[animalName] = babyName

                with open("animalNames.txt", 'a') as file:
                    file.write(animalName)
                    file.write(":")
                    file.write(babyName)
                    file.write('\n')

                print ("You have sucessfully added Animal:" , animalName , "and Baby:" , babyName , "to the list ")
               
            else:
                print("ok")
         
    if programFunction == 2:
        print("2) Add another animal's name to the dictionary")
        print("""What do you want to add to the dictionary?
You must provide a baby name and an animal name.""")

        animalName = input("What is the animal's name: ")
        animalName = animalName.lower()

        babyName = input("What is the baby animal's name: ")
        d[animalName] = babyName

        with open("animalNames.txt", 'a') as file:
            file.write(animalName)
            file.write(":")
            file.write(babyName)
            file.write('\n')

        print ("You have sucessfully added Animal:" , animalName , "and Baby:" , babyName , "to the list ")
               

    if programFunction == 3:
        print("3) Delete another animal's name")
        delName = input("What do you want to delete off the dictionary? ")

        if delName in d:
            del d[delName]
            updatedlist = "\n".join(f"{key} : {value}" for key, value in d.items())

            with open("animalNames.txt", "w") as file:
                file.write(updatedlist + "\n")

            print(updatedlist)
            print("You have successfully deleted", delName, "from the list.")
        else:
            print("The name", delName, "is not in the dictionary.")

    programFunction = int(input("""Is there anything else you would you like this program to do?
1) Find an baby animals name
2) Add another animal's name to the dictionary
3) Delete another animal's name
4) Exit
:"""))

if programFunction == 4:
        print("Thank You! BYE BYE :D")
        print("Your Changes Have Been Updated in the File")
        exit()
