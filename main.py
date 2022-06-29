import boggle_board_randomizer as bbr
from screen import*
from start_screen import*


class Main_boggle:
    def __init__(self):
        self.__words_list = self.open_list()
        self.__board = self.board_builder()
        self.__squares = self.squares_builder(self.__board)
        self.__clicked_squares = []
        self.__founded_words = []
        self.start_screen = Start_screen()

    def single_game(self):
        self.start_screen.start_menu()
        screen = Screen(self.__squares, self.__words_list)
        screen.add_word()
        screen.run_timer()
        screen.delete()
        screen.start_main_loop()

    def get_board(self):
        return self.__board

    def board_builder(self):
        board_matrix = bbr.randomize_board()
        return board_matrix

    def squares_builder(self, board):
        squares_list = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                coor = row, col
                square = Square(coor, board[row][col])
                squares_list.append(square)
        return squares_list

    def get_squares(self):
        return self.__squares

    def open_list(self):
        f = open("boggle_dict.txt", "r")
        words = (f.read())
        word_list = words.splitlines()
        return word_list


class Square:

    def __init__(self, coordinate, char):
        self.__coordinate = coordinate
        self.__char = char

    def get_coor(self):
        return self.__coordinate

    def get_char(self):
        return self.__char

    def square_click(self):
        return True


def main():
    runner = Main_boggle()
    runner.single_game()



if __name__ == '__main__':
    main()
