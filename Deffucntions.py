def describe_car(brand="Tesla", model="Model S"):
    print(f"Your car is a {brand} {model}.")
describe_car()
brand = input("What is the brand of your car? : ")
model = input("What is the model of your car? : ")
fuel_type = input("What is the fuel type of your car? : ")
describe_car(brand, model)