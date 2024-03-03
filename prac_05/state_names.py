"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformatting this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# Print all states and names
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")


state_code = input("Enter short state: ").upper()
while state_code:
    state_name = CODE_TO_NAME.get(state_code, "Invalid short state")
    print(f"{state_code} is {state_name}")
    state_code = input("Enter short state: ").upper()

