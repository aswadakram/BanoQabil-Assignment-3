print("===================")
print("Temperature Converter")
print("===================")
print("                    ")

print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
choose=input("Choose conversion (1 or 2): ")

if choose == "1":
    celsius = int(input("Enter temperature in Celsius: "))
    fahrenheit = 59*celsius+32
    print(celsius,"°C is equal to", fahrenheit,"°F")
    
elif choose == "2":
    fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    celsius = 95*(fahrenheit-32)
    print(fahrenheit,"°F is equal to", celsius,"°C")
    
else:
    print("Invalid choice. Please select 1 or 2.")
