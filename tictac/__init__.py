from string import digits


def build_matrix():
    matrix = [['_' for x in range(3)] for y in range(3)]
    return matrix


def winner_found(matrix) -> bool:
    wins = [['X', 'X', 'X'], ['O', 'O', 'O']]
    win_count = 0
    winner = ''
    for row in matrix:
        if row in wins:
            win_count += 1
            winner = row[0]

    for i in range(0, 3):
        col = [row[i] for row in matrix]
        if col in wins:
            win_count += 1
            winner = col[0]

    diagonal_1 = [matrix[0][2], matrix[1][1], matrix[2][0]]
    diagonal_2 = [matrix[0][0], matrix[1][1], matrix[2][2]]
    if diagonal_1 in wins or diagonal_2 in wins:
        win_count += 1
        winner = matrix[1][1]
    if win_count == 1:
        print(f'{winner} wins')
        return True
    elif win_count > 1:
        print('Impossible')
        return True
    return False


def game_possible(matrix) -> bool:
    O_count = 0
    X_count = 0
    blanks = 0
    for row in matrix:
        for el in row:
            if el == 'O':
                O_count += 1
            if el == 'X':
                X_count += 1
            if el == '_':
                blanks += 1
    if abs(O_count - X_count) > 1:
        print('Impossible')
        return False
    if blanks > 0:
        print('Enter the coordinates:')
        return True
    else:
        print('Draw')
        return False


def print_matrix(matrix):
    print('---------')
    print(f'| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |')
    print(f'| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |')
    print(f'| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |')
    print('---------')
    return


def credentials_correct(credentials) -> bool:
    if len(credentials) != 3:
        return False
    else:
        r = credentials[0]
        c = credentials[2]
    if r not in digits or c not in digits:
        print('You should enter numbers!')
        return False
    elif int(r) > 3 or int(c) > 3:
        print('Coordinates should be from 1 to 3!')
        return False
    return True


def try_assign(matrix, x, y, tour):
    cols = {1: 0, 2: 1, 3: 2}
    rows = {1: 2, 2: 1, 3: 0}
    if matrix[rows[y]][cols[x]] == '_':
        matrix[rows[y]][cols[x]] = tour
        return True
    else:
        print('This cell is occupied! Choose another one!')
        return False


def set_initial_tour(matrix) -> str:
    O_count = 0
    X_count = 0
    for row in matrix:
        for el in row:
            if el == 'O':
                O_count += 1
            if el == 'X':
                X_count += 1
    if X_count <= O_count:
        return 'X'
    else:
        return 'O'


def switch_tour(current):
    if current == 'X':
        return 'O'
    else:
        return 'X'
