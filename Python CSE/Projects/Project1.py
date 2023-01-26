###########################################################
#Project 1 
#In this prject I write code that convert rods into the following:
#Meters, Feet, Miles, Furlongs, and ,minutes to walk the given rods
#The first line is for the user input I also make it so the number is a float
#The second line states what the user inputted 
#The Third line just states Conversions on a new line
###########################################################
user = float(input("Input rods: "))
print("\nYou input",user,"rods.")
print("\nConversions")
Meters = user * 5.0292 #this multiples the rods and converts it into meters 
print("Meters:", round(Meters, 3));
Feet = Meters / 0.3048 #this divides meters and converts it into feet
print("Feet:", round(Feet, 2))
Miles = Meters / 1609.34 #this divides meters and converts it into miles
print("Miles:", round(Miles, 3))
Furlongs = user * 0.025 #this multiples the rods and converts it into Furlongs
print("Furlongs:", round(Furlongs, 3))
a = (Miles / 3.1) * 60 #This divides miles by the provide units than multiples it by minutes
print("Minutes to walk", user, "rods:", round(a, 3))