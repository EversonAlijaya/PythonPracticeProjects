#will add more shapes

import math
def get_value(x):
    while True:
        try:
            value = float(input(f"Enter the {x}: "))
            return value
        except ValueError:
            print("Please enter a number")

def get_result(shape,**dims):
    dim_str = ", ".join(f"{k}={v}" for k,v in dims.items())
    result = f"{shape}: {dim_str}"
    return result

def printanswer(x,shape,value):
    print (f"The {x} of the {shape} is: {value:.2f}")
    print ("(Rounded to 2 decimal points)")

def calculate():
    history = []
    while True:
        print ("\n shape calculator")
        print ("1. 3D shapes")
        print ("2. 2D shapes")
        print ("3. History")
        print ("4. Exit")
        mainoption= (input("Select an option (1-4): ").strip()) #strip removes extra whtespaces before and after a string
        if mainoption == "1": #WIP
            while True:
                print("1.Cube")
                print("2.prism")
                print("3.Tube")
                option = (input("Select an option (1-3): ").strip())

                if option == "1":
                    length = get_value("length")
                    width = get_value("width")
                    height = get_value("height")
                    volume = length * width * height
                    result = get_result("Cube",volume = volume,length = length,width = width,height = height)
                    printanswer("volume","cube",volume)
                    history.append(result)
                    break

                elif option == "2":
                    height = get_value("height")
                    length = get_value("length")
                    width = get_value("width")
                    volume = height * length * width * 0.5
                    result = get_result("prism",volume = volume,height = height,length = length,width = width)
                    printanswer("volume","prism",volume)
                    history.append(result)
                    break

                elif option == "3":
                    radius = get_value("radius")
                    height = get_value("height")
                    volume = radius **2 * math.pi * height
                    result = get_result("Tube",volume = volume, radius = radius, height = height)
                    printanswer("volume","tube",volume)
                    history.append(result)
                    break

                else:
                    print("enter a valid shape")

        elif mainoption == "2":
            while True:
                print("1.Rectangle")
                print("2.Triangle")
                print("3.Circle")
                option = (input("Select an option (1-3): ").strip())


                if option == "1":
                    length = get_value("length")
                    width = get_value("width")
                    area = length * width
                    result = get_result("rectangle", area = area, length=length, width=width)
                    printanswer( "area","rectangle",area)
                    history.append(result)
                    break

                elif option == "2":
                    height = get_value("height")
                    base = get_value("base")
                    area = height * base * 0.5
                    result = get_result("triangle", area = area, height=height, base=base)
                    printanswer("area","triangle",area)
                    history.append(result)
                    break

                elif option == "3":
                    radius = get_value("radius")
                    area = radius ** 2 * math.pi
                    result = get_result("circle", area = area, radius=radius)
                    printanswer("area","circle", area)
                    history.append(result)
                    break

                else:
                    print("enter a valid shape")

        elif mainoption == "3":
            if not history:
             print("no calculations yet")
            else:
                print("\n calculation History:")
                i = 1
                for result in history:
                    print(f"{i}. {result}")
                    i = i + 1

        elif mainoption == "4":
            print("goodbye")
            break

        else:
             print("enter a valid option")

calculate()



