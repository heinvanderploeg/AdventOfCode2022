import numpy as np
input_day8 = open("input_day8", "r").read().split('\n')
# input_day8 = open("example_day8", "r").read().split('\n')
matrix = [[int(char) for char in line] for line in input_day8]
np_matrix = np.array(matrix)


def is_visible(row_idx, col_idx):
    tree_height = matrix[row_idx][col_idx]
    right = matrix[row_idx][col_idx + 1::]
    left = matrix[row_idx][:col_idx:]
    column = [row[col_idx] for row in matrix]
    bottom = column[row_idx + 1::]
    top = column[:row_idx:]
    return bool(left) and len([tree for tree in left if tree < tree_height]) == len(left) or \
           bool(right) and len([tree for tree in right if tree < tree_height]) == len(right) or \
           bool(bottom) and len([tree for tree in bottom if tree < tree_height]) == len(bottom) or \
           bool(top) and len([tree for tree in top if tree < tree_height]) == len(top)


def viewing_distance(height, trees) -> int:
    dist = 0
    for tree in trees:
        dist += 1
        if tree >= height:            
            break
    return dist


def scenic_score(row_idx, col_idx) -> int:
    tree_height = np_matrix[row_idx][col_idx]
    right = viewing_distance(tree_height, np_matrix[row_idx][col_idx + 1::])
    left = viewing_distance(tree_height, np_matrix[row_idx][:col_idx:][::-1])
    column = [row[col_idx] for row in np_matrix]
    bottom = viewing_distance(tree_height, column[row_idx + 1::])
    top = viewing_distance(tree_height, column[:row_idx:][::-1])
    return right * left * top * bottom


visible_tree_count = len(matrix) * 2 + len(matrix[0]) * 2 - 4
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[i]) - 1):
        if is_visible(i, j):
            visible_tree_count += 1

print(visible_tree_count)

scenic_scores = []
for i in range(0, len(np_matrix)):
    for j in range(0, len(np_matrix[i])):
        scenic_scores += [scenic_score(i, j)]

print(max(scenic_scores))
