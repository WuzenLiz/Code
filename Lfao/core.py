"""
MACHIME PLAYER AI ALGORITHM FOR THE DOT GAME
"""
import copy
class MachinePlayer:
    """LOGIC FOR MACHINE PLAYER
        - select random available position
        - select the position that can get the most points
    """
    def __init__(self, chessboard):
        self.chessboard = chessboard

    def _get_available_positions(self):
        available_positions = []
        for row in range(self.chessboard.size):
            for col in range(self.chessboard.size):
                if self.chessboard.board[row][col] == 0:
                    available_positions.append((row, col))
        print(f"Available positions: {available_positions}")
        return available_positions

    def find_best_move(self):
        best_move = (None, None)
        available_positions = self._get_available_positions()
        current_score = self.chessboard.player2_score
        for row, col in available_positions:
            new_chessboard = copy.deepcopy(self.chessboard)
            new_chessboard.add_unit(row, col, player=new_chessboard._PLAYER_2)
            new_chessboard._convert_surrounding_units(row, col, player=new_chessboard._PLAYER_2)
            if new_chessboard.player2_score > current_score:
                current_score = new_chessboard.player2_score
                best_move = (row, col)
        return best_move
    
    def machine_move(self):
        print("Machine is thinking...")
        row, col = self.find_best_move()
        print(f"Machine move: {row}, {col}")
        return row, col

"""
Core CHESSBROAD for the game
"""
class Chessboard:
    _PLAYER_UNIT = 1
    _PLAYER_1 = 'player'
    _MACHINE_UNIT = -1
    _PLAYER_2 = 'machine'

    def __init__(self, size):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.current_player = self._PLAYER_1
        self.player1_score = 0
        self.player2_score = 0

    def add_unit(self, row, col,player=None):
        if player == self._PLAYER_1:
            self.board[row][col] = self._PLAYER_UNIT
            self.player1_score += 1
        else:
            self.board[row][col] = self._MACHINE_UNIT
            self.player2_score += 1

        self.current_player = self._switch_player()

    def _convert_surrounding_units(self, row, col, player=None):
        axises = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in axises:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.size and 0 <= new_col < self.size:
                if player == self._PLAYER_1:
                    if self.board[new_row][new_col] == self._MACHINE_UNIT or self.board[new_row][new_col] == 0:
                        if self.board[new_row][new_col] == self._MACHINE_UNIT:
                            self.player2_score -= 1
                            self.board[new_row][new_col] = self._PLAYER_UNIT
                            self.player1_score += 1
                        else:
                            self.board[new_row][new_col] = self._PLAYER_UNIT
                            self.player1_score += 1
                else:
                    if self.board[new_row][new_col] == self._PLAYER_UNIT or self.board[new_row][new_col] == 0:
                        if self.board[new_row][new_col] == self._PLAYER_UNIT:
                            self.board[new_row][new_col] = self._MACHINE_UNIT
                            self.player2_score += 1
                            self.player1_score -= 1
                        else:
                            self.board[new_row][new_col] = self._MACHINE_UNIT
                            self.player2_score += 1
            else:
                continue

    def _switch_player(self):
        if self.current_player == self._PLAYER_1:
            return self._PLAYER_2
        else:
            return self._PLAYER_1

    def _is_ended(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True

    def _reset_board(self):
        self.__init__(self.size)

    def make_com_move(self):
        machine_player = MachinePlayer(chessboard=self)
        row, col = machine_player.machine_move()
        if row is None or col is None:
            return
        self.add_unit(row, col)
        self._convert_surrounding_units(row, col)