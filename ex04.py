# (Name sth with "=" signs)
cars=100
space_in_a_Car=4.0
drivers=30
passengers=90
cars_not_Driven=cars-drivers
cars_Driven=drivers
carpool_Capacity=cars_Driven * space_in_a_Car
average_Passengers_per_Car = passengers / cars_Driven

#(Capital and Small letters MATTER for "name")

print("there are", cars, "Cars available")
print("there are only", drivers, "drivers available.")
print("there will be", cars_not_Driven, "enpty cars today.")
print("we can transport", carpool_Capacity, "perople today.")
print("We have", passengers, "to carpool today.")
print("we need to put about", average_Passengers_per_Car, "in each car")
