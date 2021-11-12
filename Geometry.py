# ------------- TASK 2 -----------------
# Create class and sub-class objects which represent different
# geometrical shapes, such as Rectangles and Squares

import math


class Shape:
    """Instantiating the instance methods"""

    def __init__(self):
        self.name = ""
        self.length = int()
        self.width = int()
        self.angle = int()
        self.vertex = int
        self.num_of_lines = int

    def display_details(self):
        return f"This is a {self.name}. It has {self.num_of_lines} sides, {self.angle} angles and {self.vertex}"

    def area(self):
        """calculates the area of the shape"""
        area_of_shape = self.length * self.width
        return area_of_shape


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    @property
    def length(self):
        """Getter method for length"""
        return self.__length

    @length.setter
    def length(self, length):
        """Setter method for length"""
        # if not isinstance(length, int) or not isinstance(length, float):
        #     raise TypeError("Length must be an integer or float")
        if length < 0:
            raise ValueError("Length must be > 0")
        self.__length = length

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method for width"""
        # if not isinstance(width, int) or not isinstance(width, float):
        #     raise TypeError("width must be an integer or float")
        if width < 0:
            raise ValueError("Width must be > 0")
        self.__width = width

    def area(self):
        """calculate the area of the rectangle"""
        answer = self.__length * self.__width
        return f"The area of the rectangle with width {self.__width} and length {self.__length} is {answer}cm sq"

    def perimeter(self):
        """Calculates the perimeter or distance around the shape"""
        solution = (2 * self.__width) + (2 * self.__length)
        return f"The perimeter of the {self.name} is {solution}cm"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    @property
    def radius(self):
        """Getter method for radius"""
        return self.__radius

    @radius.setter
    def radius(self, radius):
        """Setter method for radius"""
        # if not isinstance(radius, float) or not isinstance(radius, int):
        #     raise TypeError("radius must be an integer or float")
        if radius <= 0:
            raise ValueError("radius must be > 0")
        self.__radius = radius

    def area(self):
        """calculate the area of the circle"""
        answer = self.__radius ** 2 * math.pi
        return "The area of the circle with radius {}  is {:.2f}cm sq".format(self.__radius, answer)

    def circumference(self):
        """calculate the circumference of the circle"""
        answer = 2 * math.pi * self.__radius
        return "The circumference of the circle with radius {} is {:.2f}cm".format(self.__radius, answer)


class Cylinder(Shape):
    """Instantiating the instance methods of the cylinder"""

    def __init__(self, height, radius):
        super().__init__()
        self.__height = height
        self.radius = radius

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for height"""
        if not isinstance(height, int) or not isinstance(height, float):
            raise TypeError("Height must be an integer or float")
        if height <= 0:
            raise ValueError("Height must be > 0")
        self.__height = height

    def area(self):
        """Calculates the base area of the cylinder"""
        answer = (self.radius ** 2) * math.pi
        return "The base area of the cylinder with radius {}cm is {:.2f}cm sq".format(self.radius, answer)

    def curved_surface_area(self):
        """Calculating the curved surface area of the cylinder"""
        answer = 2 * math.pi * self.radius * self.__height
        return "The curved surface area of the cylinder with radius {}cm and height {}cm is {:.2f}cm sq".format(
            self.radius,
            self.__height,
            answer)

    def total_surface_area(self):
        """Calculating the total surface area of the cylinder"""
        answer = 2 * math.pi * self.radius * (self.radius + self.__height)
        return "The total surface area of the cylinder with radius {}cm and height {}cm is {:.2f}cm sq".format(
            self.radius,
            self.__height, answer)

    def volume(self):
        """calculating the volume of the circle"""
        # self.height = ""
        answer = math.pi * (self.radius ** 2) * self.__height
        return "The volume of the circle with radius {}cm and height {} is {:.2f}cm cube".format(self.radius,
                                                                                                 self.__height, answer)


class Triangle(Shape):
    """Instantiating the instance methods of the class"""

    def __init__(self, base_length, height, length, second_slant):
        super().__init__()
        self.second_length = second_slant
        self.__base = base_length
        self.__height = height
        self.length = length

    @property
    def base_length(self):
        """Getter method for the base attribute"""
        return self.__base

    @base_length.setter
    def base_length(self, base_length):
        """Setter method for the base attribute"""
        # if not isinstance(base_length, int) or not isinstance(base_length, float):
        #     raise TypeError("Base length must be an integer or float")
        if self.__base < 0:
            raise ValueError("Base length must be > 0")
        self.__base = base_length

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for height"""
        # if not isinstance(height, int) or not isinstance(height, float):
        #     raise TypeError("Height must be an integer or float")
        if height <= 0:
            raise ValueError("Height must be > 0")
        self.__height = height

    def area(self):
        """calculating the area of the triangle"""
        # self.length = length
        answer = 0.5 * self.__base * self.__height
        return f"The area of the triangle with base length of {self.__base}cm and height, {self.__height}cm is {answer}cm sq"

    def perimeter(self):
        """Calculates the perimeter or distance around the shape"""
        solution = self.__base + self.second_length + self.length
        return f"The perimeter of the triangle is {solution}cm"


class EquilateralTriangle(Shape):
    """Instantiating the object methods and attributes"""

    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        """Calculates the area of an equilateral triangle"""
        answer = (3 ** 1 / 3) / 4 * (self.length ** 2)
        return f"The area of the equilateral triangle with length {self.length}cm is {answer}cm sq"

    def perimeter(self):
        """Calculating the perimeter of the equilateral triangle"""
        answer = 3 * self.length
        print("The perimeter of the equilateral triangle with length {}cm is {}cm".format(self.length, answer))


class IsoscelesTriangle(Shape):
    """Instantiating the methods and attributes of the class"""

    def __init__(self, length, second_length):
        super().__init__()
        self.second_length = second_length
        self.length = length

    def area(self):
        """Calculates the area of an isosceles triangle"""
        answer = (self.second_length / 4) * (((4 * self.length ** 2) - (self.second_length ** 2)) ** 0.5)
        return "The area of the isosceles triangle with sides {}cm and {}cm is {:.2f}cm sq".format(self.length,
                                                                                                   self.second_length,
                                                                                                   answer)

    def area_with_one_angle(self):
        """Calculates the area of the figure when an angle is given"""
        self.angle_btn_lengths = int()
        answer = 0.5 * self.length * self.second_length * math.sin(self.angle_btn_lengths)
        print("The area of the triangle with lengths {}cm and {}cm and angle {} degree(s) is {:.2f}".format(self.length, self.second_length, self.angle_btn_lengths, answer))

    def perimeter(self):
        """calculates the perimeter of the isosceles triangle"""
        answer = (2 * self.length) + self.second_length
        print("The perimeter of the isosceles triangle with length {}cm and base {}cm is {}cm".format(self.length,
                                                                                                      self.second_length,
                                                                                                      answer))


class Scalene(Shape):
    """Instantiating the object methods and attributes of the class"""

    def __init__(self, base_length, first_slant, second_slant):
        super().__init__()
        self.first_slant = first_slant
        self.second_slant = second_slant
        self.base_length = base_length

    def area(self):
        """calculates the area of the scalene triangle"""
        semi_peri = (self.base_length + self.first_slant + self.second_slant) / 2
        answer = (semi_peri(
            (semi_peri - self.base_length) * (semi_peri - self.first_slant) * (semi_peri - self.second_slant))) ** 0.5
        print("The area of the scalene triangle with sides {}cm, {}cm and {}cm is {}cm sq".format(self.base_length,
                                                                                                  self.first_slant,
                                                                                                  self.second_slant,
                                                                                                  answer))

    def perimeter(self):
        """calculates the perimeter of the scalene triangle"""
        answer = self.base_length + self.first_slant + self.second_slant
        print("The perimeter of the scalene triangle, with sides {}cm, {}cm and {}cm is {}cm".format(self.base_length,
                                                                                                     self.first_slant,
                                                                                                     self.second_slant,
                                                                                                     answer))


class Parallelogram(Shape):
    """Instantiating the instance methods and attributes of the class"""

    def __init__(self, height, base_length, width):
        super().__init__()
        self.__height = height
        self.base = base_length
        self.width = width

    @property
    def height(self):
        """Getter methods for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for height"""
        # if not isinstance(height, int) or not isinstance(height, float):
        #     raise TypeError("Height must be integer or float")
        if height < 0:
            raise ValueError("Height must be > 0")
        self.__height = height

    def area(self):
        """calculates the area of the parallelogram"""
        answer = self.base * self.__height
        print(
            "The area of the parallelogram with height {}cm and base {}cm is {}cm sq".format(self.__height, self.base,
                                                                                             answer))

    def perimeter(self):
        """calculates the perimeter of the parallelogram"""
        answer = 2 * (self.base + self.width)
        print("The perimeter of the parallelogram with base {}cm and width {}cm is {}cm".format(self.base, self.width,
                                                                                                answer))


class Trapezium(Shape):
    """Instantiating the methods and attributes of class"""

    def __init__(self, short_length, long_length, height, side_length, second_side):
        super().__init__()
        self.short_length = short_length
        self.long_length = long_length
        self.height = height
        self.side_length = side_length
        self.second_side = second_side

    def area(self):
        """Calculates the area of the trapezium"""
        answer = ((self.long_length + self.short_length) * self.height) / 2
        print("The area of the trapezium with height {}cm is {}cm sq".format(self.height, answer))

    def perimeter(self):
        """Calculates the perimeter of the trapezium"""
        answer = self.second_side + self.side_length + self.long_length + self.short_length
        print("The perimeter of the trapezium is {}cm".format(answer))
