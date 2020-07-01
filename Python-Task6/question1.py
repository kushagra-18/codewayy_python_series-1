# Question1
def checkSpeed(driverSpeed):
    speedLimit = 70
    if(driverSpeed <= speedLimit):
        print("OK")

    else:
        
        demeritPoint = 1
        # Iterating to find the number of demerit points
        for index in range(speedLimit + 5, driverSpeed):
            if(index %5 == 0):
                demeritPoint += 1
        print("Points:",demeritPoint)
        
        if(demeritPoint > 12):
            print("License suspended")


# Taking user input
driverSpeed = int(input("Enter the speed of the driver:"))

# Calling the function
checkSpeed(driverSpeed)
