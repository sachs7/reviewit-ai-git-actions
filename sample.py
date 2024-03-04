def func_x(breeds, pet):
    for breed in breeds:
        if breed == pet:
            print("I have a dog.")
    else:
        print("I don't have a dog")


func_x(["chihuahua", "jack russell"], "chihuahua")

# => I have a dog.
# => I don't have a dog
