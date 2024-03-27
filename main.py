# def sandwich_toppings(*toppings):
#     for topping in toppings:
#         print(topping)
        
# sandwich_toppings("Tuna", "Olives", "Pepper")

def user_profile(first_name, last_name, location, place, field, subject):
    
    user_dict = {first_name : last_name,
                 location : place,
                 field : subject}
    return(user_dict)
    
myCharacter = user_profile("Wadie", "Benabdouh", "location", "Moscow", "field", "Aviation")
print(myCharacter)