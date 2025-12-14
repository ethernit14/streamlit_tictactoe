import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3+1, (j+1)*3+1)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False


def minimax(position, depth, is_maximizing, ai_player, human_player):
    if position.current_winner == ai_player:
        return {'position': None, 'score': 1 * (position.num_empty_squares() + 1)}
    elif position.current_winner == human_player:
        return {'position': None, 'score': -1 * (position.num_empty_squares() + 1)}
    elif not position.empty_squares():
        return {'position': None, 'score': 0}
    
    if is_maximizing:
        max_eval = {'position': None, 'score': -math.inf}
        for possible_move in position.available_moves():
            position.make_move(possible_move, ai_player)
            eval = minimax(position, depth + 1, False, ai_player, human_player)
            position.board[possible_move] = ' '
            position.current_winner = None
            eval['position'] = possible_move
            if eval['score'] > max_eval['score']:
                max_eval = eval
        return max_eval
    else:
        min_eval = {'position': None, 'score': math.inf}
        for possible_move in position.available_moves():
            position.make_move(possible_move, human_player)
            eval = minimax(position, depth + 1, True, ai_player, human_player)
            position.board[possible_move] = ' '
            position.current_winner = None
            eval['position'] = possible_move
            if eval['score'] < min_eval['score']:
                min_eval = eval
        return min_eval


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = minimax(game, 0, True, 'O', 'X')['position']
        else:
            square = int(input(f"{letter}'s turn. Input move (1-9): ")) - 1
            while square not in game.available_moves():
                square = int(input("Invalid move. Try again (1-9): ")) - 1
        
        game.make_move(square, letter)
        
        if print_game:
            print(f'\n{letter} makes a move to square {square + 1}')
            game.print_board()
            print()
        
        if game.current_winner:
            if print_game:
                print(f'{letter} wins!')
            return letter
        
        letter = 'O' if letter == 'X' else 'X'
    
    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    game = TicTacToe()
    play(game, 'X', 'O', print_game=True)