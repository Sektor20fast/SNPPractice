class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def  rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError

    player1,player1_move = players[0][0], players[0][1]
    player2,player2_move = players[1][0], players[1][1]

    valid_moves = {'R', 'P', 'S'}
    if player1_move not in valid_moves:
        raise NoSuchStrategyError()
    if player2_move not in valid_moves:
        raise NoSuchStrategyError()

    winning_rules = {
        ('R', 'S'): 1,
        ('S', 'P'): 1,
        ('P', 'R'): 1,
    }

    # Если ходы одинаковые или первый игрок выигрывает
    if player1_move == player2_move:
        winner_name, winner_move = player1, player1_move
    elif (player1_move, player2_move) in winning_rules:
        winner_name, winner_move = player1, player1_move
    else:
        winner_name, winner_move = player2, player2_move

    return f"{winner_name} {winner_move}"

try: print(rps_game_winner(['R', 'S', 'P']))
except WrongNumberOfPlayersError:
    print('WrongNumberOfPlayersError')

try: print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
except WrongNumberOfPlayersError: print('WrongNumberOfPlayersError')

try: print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
except NoSuchStrategyError: print('NoSuchStrategyError')

print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
