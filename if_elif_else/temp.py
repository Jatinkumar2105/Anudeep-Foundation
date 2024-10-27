# 3. Check if a temperature is hot, warm, or cold.
temperature = float(input("Enter temperature in Celsius: "))
if temperature > 35:
    print("It's hot.")
elif 10 <= temperature <= 35:
    print("It's warm.")
else:
    print("It's cold.")