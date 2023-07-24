import random


def convert(hexColor):
    # print(hexColor)
    hexColor = hexColor.lstrip("#")
    if hexColor is None or hexColor == "":
        print("no argument for hexcolor conversion")
    else:
        color = {
            "r": int(hexColor[:2], base=16),
            "g": int(hexColor[2:4], base=16),
            "b": int(hexColor[4:], base=16),
        }
    # print(str(color["r"]) + " " + str(color["g"]) + " " + str(color["b"]))
    return color
