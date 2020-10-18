import tictac

ticTacToe = tictac.build_matrix()
current_tour = tictac.set_initial_tour(ticTacToe)
tictac.print_matrix(ticTacToe)

while True:
    # check if we have a winner
    if not tictac.winner_found(ticTacToe):
        # check if we can play
        if tictac.game_possible(ticTacToe):
            credentials = input()
            credentials.strip()
            char_assigned = False
            if tictac.credentials_correct(credentials):
                char_assigned = tictac.try_assign(ticTacToe, int(credentials[0]), int(credentials[2]), current_tour)
                if char_assigned:
                    current_tour = tictac.switch_tour(current_tour)
                    tictac.print_matrix(ticTacToe)
        else:
            break
    else:
        break
