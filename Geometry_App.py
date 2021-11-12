from Geometry import *

print("Welcome to Geometry App!")


def calculator():
    print("\nWhat shape would you like to operate on?")
    option = int(input("1. Rectangle\n2. Circle\n3. Triangle\n4. Equilateral triangle\n5. Isosceles Triangle"
                       "\n6. Scalene triangle\n7. Cylinder\n8. Parallelogram\n9. Trapezium\n"))

    if option == 1:
        length = int(input("Enter the length of the figure(cm): "))
        width = int(input("Enter the width of the figure(cm): "))
        rectangle = Rectangle(length=length, width=width)
        print("What would you like to do?")
        answer = int(input("1. Area\n2. Perimeter\n"))
        if answer == 1:
            print(rectangle.area())
        elif answer == 2:
            print(rectangle.perimeter())
    elif option == 2:
        try:
            radius = int(input("Enter the radius of the figure(cm): "))
            circle = Circle(radius=radius)
            print("What would you like to do?")
            answer = int(input("1. Area\n2. Circumference\n"))
            if answer == 1:
                print(circle.area())
            elif answer == 2:
                print(circle.circumference())
        except Exception as ex:
            print(ex)

    elif option == 3:
        """Triangle"""
        try:
            base_length = int(input("Enter the base length of the figure(cm): "))
            length = int(input("Enter the length of the figure(cm): "))
            height = int(input("Enter the height of the figure(cm): "))
            second_slant = int(input("Enter the second slant length(cm): "))
            triangle = Triangle(base_length=base_length, height=height, length=length, second_slant=second_slant)
            print("What would you like to do?")
            answer = int(input("1. Area\n2. Perimeter\n"))
            if answer == 1:
                print(triangle.area())
            elif answer == 2:
                print(triangle.perimeter())
        except Exception as ex:
            print(ex)

    elif option == 4:
        """Equilateral"""
        try:
            length = int(input("Enter the length of the equilateral triangle(cm): "))
            triangle = EquilateralTriangle(length=length)
            print("What would you like to do?")
            answer = int(input("1. Area\n2. Perimeter\n"))
            if answer == 1:
                print(triangle.area())
            elif answer == 2:
                print(triangle.perimeter())
        except Exception as ex:
            print(ex)

    elif option == 5:
        """Isosceles"""
        try:
            length = int(input("Enter the slant length of the figure(cm): "))
            second_length = int(input("Enter the different second length of the figure(cm): "))
            triangle = IsoscelesTriangle(length=length, second_length=second_length)
            print("What would you like to do?")
            answer = int(input("1. Area\n2. Perimeter\n3. Area with an angle"))
            if answer == 1:
                print(triangle.area())
            elif answer == 2:
                triangle.perimeter()
            elif answer == 3:
                triangle.area_with_one_angle()
        except Exception as ex:
            print(ex)

    elif option == 6:
        """Scalene"""
        try:
            base_length = int(input("Enter the base length of the scalene triangle(cm): "))
            first_slant = int(input("Enter the first slant length of the figure(cm): "))
            second_slant = int(input("Enter the second slant length of the figure(cm): "))
            triangle = Scalene(base_length=base_length, first_slant=first_slant, second_slant=second_slant)
            print("What would you like to do?")
            answer = int(input("1. Area\n2. Perimeter\n"))
            if answer == 1:
                triangle.area()
            elif answer == 2:
                triangle.perimeter()
        except Exception as ex:
            print(ex)

    elif option == 7:
        """Cylinder"""
        try:
            height = int(input("Enter the height of the cylinder(cm): "))
            radius = int(input("Enter the radius of the cylinder(cm): "))
            cylinder = Cylinder(height=height, radius=radius)
            print("What would you like to do?")
            answer = int(input("1. Area\n2. Curved surface area\n3. Total surface area\n4. Volume\n"))
            if answer == 1:
                print(cylinder.area())
            elif answer == 2:
                print(cylinder.curved_surface_area())
            elif answer == 3:
                print(cylinder.total_surface_area())
            elif answer == 4:
                print(cylinder.volume())
        except Exception as ex:
            print(ex)

    elif option == 8:
        """Parallelogram"""
        try:
            height = int(input("Enter the height of the parallelogram(cm): "))
            base_length = int(input("Enter the base length of the figure(cm): "))
            slant_width = int(input("Enter the slanted width of the parallelogram(cm): "))
            parallelogram = Parallelogram(height=height, base_length=base_length, width=slant_width)
            print("What would you like to do?")
            answer = int(input("1. Area\n2. Perimeter\n"))
            if answer == 1:
                parallelogram.area()
            elif answer == 2:
                parallelogram.perimeter()
        except Exception as ex:
            print(ex)

    elif option == 9:
        """Trapezium"""
        try:
            short_length = int(input("Enter the short length of the trapezium(cm): "))
            long_length = int(input("Enter the long length of the figure(cm): "))
            height = int(input("Enter the height of the figure(cm): "))
            first_slant_side = int(input("Enter the first slant length(cm): "))
            second_slant_side = int(input("Enter the second slant length(cm): "))
            trapezium = Trapezium(short_length=short_length, long_length=long_length, height=height,
                                  side_length=first_slant_side, second_side=second_slant_side)
            print("What would you like to do?")
            answer = int(input("1. Area\n2. Perimeter\n"))
            if answer == 1:
                trapezium.area()
            elif answer == 2:
                trapezium.perimeter()
        except Exception as ex:
            print(ex)


def main():
    while True:
        calculator()
        print("Would you like to do anything else(Y/N)?")
        option = input("Choose an option: ")
        if option in ("No", "N", "no", "n"):
            print("---------------------- Thank you for using the calculator --------------------")
            break


main()
# needs to add more shapes to the source code
