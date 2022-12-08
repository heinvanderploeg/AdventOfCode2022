day4_input = open("input_day4", "r").read().split('\n')

elf_pairs = [pair.split(',') for pair in day4_input]


def assignment_to_range(assignment):
    return range(int(assignment[0]), int(assignment[1]))


def range_in_other(range1: range, range2: range):
    return (range1.start >= range2.start and range1.stop <= range2.stop) \
           or (range2.start >= range1.start and range2.stop <= range1.stop)


def range_overlaps(range1: range, range2: range):
    return (range2.start <= range1.start <= range2.stop) or \
           (range1.start <= range2.start <= range1.stop) or \
           (range2.start <= range1.stop <= range2.stop) or \
           (range1.start <= range2.stop <= range1.stop)

    # hmm, why does this not work
    # return range1.start in range2 or range1.stop in range2 or range2.start in range1 or range2.stop in range1


def get_ranges(elf_pair):
    return assignment_to_range(elf_pair[0].split('-')), assignment_to_range(elf_pair[1].split('-'))


def have_full_overlap(elf_pair):
    range1, range2 = get_ranges(elf_pair)
    return range_in_other(range1, range2)


def have_partial_overlap(elf_pair):
    range1, range2 = get_ranges(elf_pair)
    return range_overlaps(range1, range2)


# challenge 1
print(len([elf_pair for elf_pair in elf_pairs if have_full_overlap(elf_pair)]))
# challenge 2
print(len([elf_pair for elf_pair in elf_pairs if have_partial_overlap(elf_pair)]))
