while True:
    age = input("How old are you? ")
    
    age = int(age)
    if age < 3:
        print("Your enter is free")
    elif age < 12:
        print("Your enter is dh20") 
    else:
        print("Your enter is dh25")