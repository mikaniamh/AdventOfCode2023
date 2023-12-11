DIGITS = "1234567890"
NORMAL_CHAR = ".\n"


# The problem
# [ $ 5 2 ]
# [ 2 . 1 ]

def check_adjacent_values(row: int, col: int, all_lines) -> int:
    to_sum = []

    # check left
    if col >= 1:
        to_sum.append(check_left(all_lines, col, row))

    # check right
    if col < len(all_lines[row]):
        to_sum.append(check_right(all_lines, col, row))

    # check top
    if row > 0:
        if all_lines[row - 1][col] in DIGITS:
            to_sum.append(check_both(all_lines, col, row - 1))
        else:
            to_sum.append(check_left(all_lines, col, row - 1))
            to_sum.append(check_right(all_lines, col, row - 1))

    if row < len(all_lines) - 1:
        if all_lines[row + 1][col] in DIGITS:
            to_sum.append(check_both(all_lines, col, row + 1))
        else:
            to_sum.append(check_left(all_lines, col, row + 1))
            to_sum.append(check_right(all_lines, col, row + 1))

    to_sum = [n for n in to_sum if n != -1]
    return (to_sum[0] * to_sum[1]) if len(to_sum) == 2 else 0


def check_right(all_lines, col, row):
    curr_col = 1
    right_digits = ""
    while (col + curr_col) < len(all_lines[row]) and all_lines[row][col + curr_col] in DIGITS:
        right_digits += all_lines[row][col + curr_col]
        curr_col += 1
    return int(right_digits or -1)


def check_both(all_lines, col, row):
    curr_col = 0
    both_digits = ""
    while (col + curr_col) >= 0 and all_lines[row][col + curr_col] in DIGITS:
        both_digits = all_lines[row][col + curr_col] + both_digits
        curr_col -= 1
    curr_col = 1
    while (col + curr_col) < len(all_lines[row]) and all_lines[row][col + curr_col] in DIGITS:
        both_digits += all_lines[row][col + curr_col]
        curr_col += 1
    return int(both_digits or -1)


def check_left(all_lines, col, row):
    curr_col = -1
    left_digits = ""
    while (col + curr_col) >= 0 and all_lines[row][col + curr_col] in DIGITS:
        left_digits = all_lines[row][col + curr_col] + left_digits
        curr_col -= 1
    return int(left_digits or -1)


def day3(all_lines):
    row = 0
    total = 0
    for line in all_lines:
        col = 0

        for x in line:
            if x == '*':
                total += check_adjacent_values(row, col, all_lines)
            col += 1

        row += 1
    return total


def main():
    file = open("day3_data.txt")
    all_lines = file.readlines()
    # all_lines = ['25$']

    print(day3(all_lines))
    file.close()


# MAIN
if __name__ == '__main__':
    main()
