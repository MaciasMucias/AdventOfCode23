from utils import parse_reports_from_input, predict_next_value

reports = parse_reports_from_input("../../Inputs/9")

predicted_sum = 0
for report in reports:
    predicted_value = predict_next_value(report)
    predicted_sum += predicted_value

print(predicted_sum)
