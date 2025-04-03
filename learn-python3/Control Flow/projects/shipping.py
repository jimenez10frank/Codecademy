weight = 1.5

# Ground shipping
if weight <= 2:
    ground_cost = weight * 1.50 + 20
    print("Ground shipping cost is", ground_cost)
elif weight <= 6:
    ground_cost = weight * 3.00 + 20
    print("Ground shipping cost is", ground_cost)
elif weight <= 10:
    ground_cost = weight * 4.00 + 20
    print("Ground shipping cost is", ground_cost)
else:
    ground_cost = weight * 4.75 + 20 
    print("Ground shipping cost is", ground_cost)

premium_ground_cost = 125.00
print("Premium ground shipping cost is", premium_ground_cost)

# drone shipping

if weight <= 2:
    drone_cost = weight * 4.50
    print("Drone shipping cost is: ", drone_cost)
elif weight <= 6:
    drone_cost = weight * 9.00
    print("Drone shipping cost is: ", drone_cost)
elif weight <= 10:
    drone_cost = weight * 12.00
    print("Drone shipping cost is: ", drone_cost)
else:
    drone_cost = weight * 14.25
    print("Drone shipping cost is: ", drone_cost)