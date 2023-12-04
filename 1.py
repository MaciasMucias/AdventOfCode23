def load_input(path):
    with open(path, "r") as f:
        return f.readlines()


total_calibration_value = 0
for line in load_input("Inputs\\1"):
    value = ""
    for character in line:
        if character.isnumeric():
            value += character
            break

    for character in reversed(line):
        if character.isnumeric():
            value += character
            break

    total_calibration_value += int(value)

print(total_calibration_value)