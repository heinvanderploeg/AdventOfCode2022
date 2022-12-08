import copy
import re

day5_input = open("input_day5", "r").read().split('\n')

stacks = [[], [], [], [], [], [], [], [], []]

pattern = r'|'.join(['move ', 'from ', 'to '])
moves = [[int(x) for x in re.split(pattern, line)[1::]] for line in day5_input[10:]]


for i in range(0, 8):
    line = day5_input[i]
    for j in range(1, len(line), 4):
        if line[j] != ' ':
            stacks[j // 4].insert(0, line[j])

stacks_challenge_1 = copy.deepcopy(stacks)

for move in moves:
    for i in range(0, move[0]):
        stacks_challenge_1[move[2] - 1] += stacks_challenge_1[move[1] - 1].pop()

print(''.join([stack[-1] for stack in stacks_challenge_1]))


stacks_challenge_2 = copy.deepcopy(stacks)

for move in moves:
    from_stack = stacks_challenge_2[move[1] - 1]
    to_stack = stacks_challenge_2[move[2] - 1]
    moving_crates = from_stack[-move[0]:]
    to_stack += moving_crates
    del from_stack[-len(moving_crates):]

print(''.join([stack[-1] for stack in stacks_challenge_2]))
