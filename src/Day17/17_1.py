from utils import parse_heat_loss_map_from_input, find_least_heat_loss_path


heat_loss_map = parse_heat_loss_map_from_input("../../Inputs/17")
heat_cost = find_least_heat_loss_path(heat_loss_map, 1, 3)
print()
print(heat_cost)