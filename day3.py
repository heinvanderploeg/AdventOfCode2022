day3_input = open("input_day3", "r").read().split('\n')

prios = list(map(chr, range(ord('a'), ord('z') + 1))) + list(map(chr, range(ord('A'), ord('Z') + 1)))

# challenge 1
compartments = [(rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]) for rucksack in day3_input]


def get_duplicate(compartment1, compartment2) -> str:
    for character in compartment1:
        if compartment2.count(character) > 0:
            return character


print(sum([prios.index(duplicate) + 1 for duplicate in
           [get_duplicate(compartment[0], compartment[1]) for compartment in compartments]]))

# challenge 2
groups = list(zip(*[iter(day3_input)] * 3))


def get_badge(rucksacks):
    for character in rucksacks[0]:
        if rucksacks[1].count(character) > 0 and rucksacks[2].count(character) > 0:
            return character


print(sum([prios.index(badge) + 1 for badge in
           [get_badge(rucksacks) for rucksacks in groups]]))
