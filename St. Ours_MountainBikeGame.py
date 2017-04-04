#Andrew St. Ours
#3/28/17
#Mountain bike game

#welcome

print("Welcome to Whistler Mountain Bike Park. \nToday you are going to"
      "have a choice of three trails to ride on. \nA green circle trail, a blue"
      " square trail and a black diamond trail.")

print("\nMake sure you pick the trail that applies best to your level of riding.")

#lists

x= ["bike", "helmet", "pair of gloves", "backpack", "water"]

y= ["bike", "helmet", "pair of gloves", "backpack", "water"]

z= ["bike", "helmet", "pair of gloves", "backpack", "water"]

print("\n\nOn your trip you have a",x,".")

print("\n\nAre you ready?")

input("\n\nPress [Enter] to continue up to the top of the mountain.")

#adding elemnets to the list

print("\n\nYou are now at the top and it is time to choose your trail.")


trail= input("\nWould you like the green, blue or black trail?\n")

#if statements

if trail == "green" or trail == "Green":
    print("Ah we have a beginner I see. \nYou have recieve a nice"
          " Whistler Mountain Bike t-shirt. \nIt will be added to"
          " your things.")
    
    x.append("t-shirt")
    print(x)

if trail == "blue" or trail == "Blue":
    print("Ooo we have a decent rider here. \nYou have recieved a pair"
          " of riding shoes. \nThey will be added to your things.")

    y.append("riding shoes")
    print(y)


if trail == "black" or trail == "Black":
    print("Mad respect for being an expert dude. \nYou have recieved a"
          "check for $10000 to buy a new bike. \nThe check will be added"
          " to your things.")

    z.append("check")
    print(z)


#Exit

print("\n\nI hope you had fun today and keep shredding!")

input("\n\nPress [Enter] to exit the park.")


    
        
      



