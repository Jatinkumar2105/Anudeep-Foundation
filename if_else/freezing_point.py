#Test if a temperature is above or below freezing (0°C)# Input temperature from the user
temperature = float(input("Enter the temperature in degrees Celsius: "))

# Check if the temperature is above freezing
if temperature > 0:
    print("The temperature is above freezing.")
else:
    print("The temperature is at or below freezing.")
