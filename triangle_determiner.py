print("===================")
print("Triangle Determiner")
print("===================")
print("                    ")

side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))


if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:

    if side1 == side2 == side3:
        print("The triangle is equilateral.")

    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")

    else:
        print("The triangle is scalene.")

else:
    print("The lengths you provide do not form a valid triangle.")
