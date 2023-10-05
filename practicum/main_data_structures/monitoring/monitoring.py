def matrix_transposing(lines, rows, incorrect_matrix):
    correct_matrix = [[0] * lines for _ in range(rows)]
    for line in range(lines):
        for row in range(rows):
            correct_matrix[row][line] = incorrect_matrix[line][row]
    for string in correct_matrix:
        string = " ".join(map(str, string))
        yield string


if __name__ == "__main__":
    lines = int(input())
    rows = int(input())
    incorrect_matrix = []
    for _ in range(lines):
        my_list = list(map(int, input().split(" ")))
        incorrect_matrix.append(my_list)
    for new_line in matrix_transposing(lines, rows, incorrect_matrix):
        print(new_line)
