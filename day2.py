day2_input = open("input_day2", "r").read().split('\n')

scores = {-2: 6,
          -1: 0,
          0: 3,
          1: 6,
          2: 0}

what_to_play_diff = {'X': -1, 'Y': 0, 'Z': 1}


def round_score_challenge_1(line: str):
    rnd = line.split(' ')
    opponent = 'ABC'.index(rnd[0])
    you = 'XYZ'.index(rnd[1])
    return you + 1 + scores[you - opponent]


def round_score_challenge_2(line: str):
    rnd = line.split(' ')
    opponent = 'ABC'.index(rnd[0])
    you = (opponent + what_to_play_diff[rnd[1]]) % 3
    return you + 1 + scores[you - opponent]


print(sum(round_score_challenge_1(line) for line in day2_input))
print(sum(round_score_challenge_2(line) for line in day2_input))
