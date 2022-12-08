day6_input = open("input_day6", "r").read()

for i in range(3, len(day6_input)):
    if len({day6_input[i - 3], day6_input[i - 2], day6_input[i - 1], day6_input[i]}) == 4:
        print(i + 1)
        break

for i in range(13, len(day6_input)):
    if len({day6_input[i - j] for j in range(0, 14)}) == 14:
        print(i + 1)
        break
