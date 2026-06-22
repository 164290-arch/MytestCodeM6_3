print("Area Calculator Program")

print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = int(input("Choose a shape (1-3): "))

if choice == 1:
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))
    area = width * length
    print("Rectangle Area =", area)

elif choice == 2:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Triangle Area =", area)

elif choice == 3:
    radius = float(input("Enter radius: "))
    area = math.pi * (radius ** 2)
    print("Circle Area =", round(area, 2))

else:
    print("Please choose a number between 1 and 3.")
