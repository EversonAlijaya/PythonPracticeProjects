#will add more shapes

import math


def get_value(label):
    while True:
        try:
            return float(input(f"Enter the {label}: "))
        except ValueError:
            print("Please enter a number")


def format_result(shape, **dims):
    dim_str = ", ".join(f"{k}={v}" for k, v in dims.items())
    return f"{shape}: {dim_str}"


def print_answer(measurement, shape, value):
    print(f"The {measurement} of the {shape} is: {value:.2f}")
    print("(Rounded to 2 decimal points)")


def run_shape_menu(options):
    while True:
        for i, name in enumerate(options, 1):
            print(f"{i}. {name}")
        option = input(f"Select an option (1-{len(options)}): ").strip()
        if option in [str(i) for i in range(1, len(options) + 1)]:
            return option
        print("Enter a valid shape")


def calculate():
    history = []
    while True:
        print("\nShape Calculator")
        print("1. 3D shapes")
        print("2. 2D shapes")
        print("3. History")
        print("4. Exit")
        main_option = input("Select an option (1-4): ").strip()

        if main_option == "1":
            option = run_shape_menu(["Rectangular Prism", "Prism", "Tube", "Sphere", "Cone", "Square Pyramid", "Torus", "Hemisphere"])

            if option == "1":
                length = get_value("length")
                width = get_value("width")
                height = get_value("height")
                volume = length * width * height
                surface_area = 2 * (length * width + length * height + width * height)
                result = format_result("Rectangular Prism", volume=volume, surface_area=surface_area, length=length, width=width, height=height)
                print_answer("volume", "rectangular prism", volume)
                print_answer("surface area", "rectangular prism", surface_area)

            elif option == "2":
                height = get_value("height")
                length = get_value("length")
                width = get_value("width")
                hypotenuse = math.sqrt(length ** 2 + height ** 2)
                volume = height * length * width * 0.5
                surface_area = length * height + (length + height + hypotenuse) * width
                result = format_result("Prism", volume=volume, surface_area=surface_area, height=height, length=length, width=width)
                print_answer("volume", "prism", volume)
                print_answer("surface area", "prism", surface_area)

            elif option == "3":
                radius = get_value("radius")
                height = get_value("height")
                volume = math.pi * radius ** 2 * height
                surface_area = 2 * math.pi * radius * (radius + height)
                result = format_result("Tube", volume=volume, surface_area=surface_area, radius=radius, height=height)
                print_answer("volume", "tube", volume)
                print_answer("surface area", "tube", surface_area)

            elif option == "4":
                radius = get_value("radius")
                volume = (4 / 3) * math.pi * radius ** 3
                surface_area = 4 * math.pi * radius ** 2
                result = format_result("Sphere", volume=volume, surface_area=surface_area, radius=radius)
                print_answer("volume", "sphere", volume)
                print_answer("surface area", "sphere", surface_area)

            elif option == "5":
                radius = get_value("radius")
                height = get_value("height")
                slant = math.sqrt(radius ** 2 + height ** 2)
                volume = (1 / 3) * math.pi * radius ** 2 * height
                surface_area = math.pi * radius * (radius + slant)
                result = format_result("Cone", volume=volume, surface_area=surface_area, radius=radius, height=height)
                print_answer("volume", "cone", volume)
                print_answer("surface area", "cone", surface_area)

            elif option == "6":
                base = get_value("base side length")
                height = get_value("height")
                slant = math.sqrt((base / 2) ** 2 + height ** 2)
                volume = (1 / 3) * base ** 2 * height
                surface_area = base ** 2 + 2 * base * slant
                result = format_result("Square Pyramid", volume=volume, surface_area=surface_area, base=base, height=height)
                print_answer("volume", "square pyramid", volume)
                print_answer("surface area", "square pyramid", surface_area)

            elif option == "7":
                R = get_value("major radius (center to tube center)")
                r = get_value("minor radius (tube radius)")
                volume = 2 * math.pi ** 2 * R * r ** 2
                surface_area = 4 * math.pi ** 2 * R * r
                result = format_result("Torus", volume=volume, surface_area=surface_area, major_radius=R, minor_radius=r)
                print_answer("volume", "torus", volume)
                print_answer("surface area", "torus", surface_area)

            elif option == "8":
                radius = get_value("radius")
                volume = (2 / 3) * math.pi * radius ** 3
                surface_area = 3 * math.pi * radius ** 2
                result = format_result("Hemisphere", volume=volume, surface_area=surface_area, radius=radius)
                print_answer("volume", "hemisphere", volume)
                print_answer("surface area", "hemisphere", surface_area)

            history.append(result)

        elif main_option == "2":
            option = run_shape_menu(["Rectangle", "Triangle", "Circle", "Square", "Trapezoid", "Parallelogram", "Ellipse", "Pentagon", "Hexagon"])

            if option == "1":
                length = get_value("length")
                width = get_value("width")
                area = length * width
                result = format_result("Rectangle", area=area, length=length, width=width)
                print_answer("area", "rectangle", area)

            elif option == "2":
                base = get_value("base")
                height = get_value("height")
                area = base * height * 0.5
                result = format_result("Triangle", area=area, base=base, height=height)
                print_answer("area", "triangle", area)

            elif option == "3":
                radius = get_value("radius")
                area = radius ** 2 * math.pi
                result = format_result("Circle", area=area, radius=radius)
                print_answer("area", "circle", area)

            elif option == "4":
                side = get_value("side length")
                area = side ** 2
                result = format_result("Square", area=area, side=side)
                print_answer("area", "square", area)

            elif option == "5":
                base1 = get_value("base 1")
                base2 = get_value("base 2")
                height = get_value("height")
                area = (base1 + base2) / 2 * height
                result = format_result("Trapezoid", area=area, base1=base1, base2=base2, height=height)
                print_answer("area", "trapezoid", area)

            elif option == "6":
                base = get_value("base")
                height = get_value("height")
                area = base * height
                result = format_result("Parallelogram", area=area, base=base, height=height)
                print_answer("area", "parallelogram", area)

            elif option == "7":
                a = get_value("semi-axis a")
                b = get_value("semi-axis b")
                area = math.pi * a * b
                result = format_result("Ellipse", area=area, a=a, b=b)
                print_answer("area", "ellipse", area)

            elif option == "8":
                side = get_value("side length")
                area = (math.sqrt(25 + 10 * math.sqrt(5)) / 4) * side ** 2
                result = format_result("Pentagon", area=area, side=side)
                print_answer("area", "pentagon", area)

            elif option == "9":
                side = get_value("side length")
                area = (3 * math.sqrt(3) / 2) * side ** 2
                result = format_result("Hexagon", area=area, side=side)
                print_answer("area", "hexagon", area)

            history.append(result)

        elif main_option == "3":
            if not history:
                print("No calculations yet")
            else:
                print("\nCalculation History:")
                for i, result in enumerate(history, 1):
                    print(f"{i}. {result}")

        elif main_option == "4":
            print("Goodbye")
            break

        else:
            print("Enter a valid option")


calculate()
