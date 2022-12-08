day1_input = open("input_day1", "r").read()


def elves_list():
    return [[int(cal) for cal in elf] for elf in [elf.split('\n') for elf in day1_input.split('\n\n')]]


def elf_cal_count_sorted():
    return [sum(calories) for calories in sorted(elves_list(), key=lambda elf: sum(elf), reverse=True)]


def day1_challenge_1():
    return elf_cal_count_sorted()[0]


def day1_challenge_2():
    return sum(elf_cal_count_sorted()[0:3])


print(day1_challenge_1())
print(day1_challenge_2())
