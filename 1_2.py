from utils import load_input

STRING_DIGITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def digit_from_string(string, i):
    return STRING_DIGITS.get(string[i:i + 3], False) \
        or STRING_DIGITS.get(string[i:i + 4], False) \
        or STRING_DIGITS.get(string[i:i + 5], False)


total_calibration_value = 0
for line in load_input("Inputs\\1"):
    digits = []
    padded_line = line + "____"
    for line_range in ((0, len(line), 1), (len(line) - 1, -1, -1)):
        for ind in range(*line_range):
            character = line[ind]
            if character.isnumeric():
                digits.append(int(character))
                break
            if possible_digit := digit_from_string(padded_line, ind):
                digits.append(possible_digit)
                break

    total_calibration_value += 10 * digits[0] + digits[-1]

print(total_calibration_value)
