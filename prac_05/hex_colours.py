COLOR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "BISQUE": "#FFE4C4",
    "CORNFLOWERBLUE": "#6495ED",
    "DARKORANGE": "#FF8C00",
    "GOLD": "#FFD700",
    "LAVENDER": "#E6E6FA",
    "MEDIUMSPRINGGREEN": "#00FA9A",
    "TOMATO": "#FF6347"
}

def lookup_color_code():
    color_name = input("Enter a color name (or blank to stop): ").lower()

    while color_name:
        color_code = COLOR_CODES.get(color_name, "None")
        print(f"The color code for {color_name} is {color_code}")
        color_name = input("Enter a color name (or blank to stop): ").upper()


lookup_color_code()