def add_pet_to_list(pet, pets=[]):
    pets.append(pet)
    return pets


list_w_cat = add_pet_to_list("cat1")
list_w_dog = add_pet_to_list("dog1")

print(list_w_cat)
print(list_w_dog)
