from tkinter import *
import math
from tkinter import messagebox
import main


class Screen:

    def __init__(self, squares, legal_words):
        self.__screen = Tk()
        self.__screen.geometry("550x550")
        self.__leftframe = Frame(self.__screen)
        self.__topframe = Frame(self.__screen)
        self.__bottomframe = Frame(self.__screen)
        self.__legal_words = legal_words
        self.pack_frames()
        self.__buttons_list = []
        self.__screen.title("boggle")
        self.__operator = ""
        self.__text_input = StringVar()
        self.squares = squares
        self.__txtDisplay = self.txtdisplay()
        self.__duration = 180
        self.__timer_label = Label(self.__screen, text="0:0", font=
            ('ariel', 15, 'bold'), fg="blue", height=2, width=10,
                                         bg="light grey")
        self.__time_label = Label(self.__screen, text="Time", font="ariel")
        self.run_timer()
        self.__clicked_coor = []
        self.__score_val = StringVar()
        self.__score_val.set("0")
        self.__points = 0
        self.create_game()
        self.__end_game = False

    def score(self):
        scoreTitle = Label(self.__bottomframe, text="Score", font="ariel")
        scoreTitle.pack()
        score = Label(self.__bottomframe, height=2, width=10,
                      textvariable=self.__score_val, fg="blue", bg="light "
                                                                   "grey",
                      font=('ariel', 15, 'bold'))
        score.pack()
        space = Label(self.__bottomframe, height=1, width=10,
                      textvariable='\n')
        space.pack()

    def update_score(self, val):
        self.__score_val.set(str(val))

    def run_timer(self):
        self.__time_label.pack()
        self.__timer_label.pack()
        self.countdown(20)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.__duration = remaining
        if self.__duration == 0:
            self.game_over()
        else:
            mins = self.__duration // 60
            sec = self.__duration % 60
            if sec < 10:
                sec = "0"+str(sec)
            self.__timer_label.config(text=(str(mins) + ':' + str(sec)))
            self.__duration -= 1
            self.__screen.after(1000, self.countdown, self.__duration)

    def start_main_loop(self):
        self.__screen.mainloop()

    def pack_frames(self):
        self.__leftframe.pack(side=LEFT)
        self.__topframe.pack(side=TOP)
        self.__bottomframe.pack(side=BOTTOM)

    def create_game(self):
        self.char_btns()
        self.list_box()
        self.score()

    def add_word(self):
        Button(self.__leftframe, width=4, height=1, padx=18,
               pady=12,
               bd=10, fg="black", font=('ariel', 20, 'bold'), text="add",
               command=self.append_word,
               bg="green"
               ).grid(row=6, column=0, columnspan=2)

    def append_word(self):
        new_word = self.__operator[:]
        if new_word in self.__legal_words:
            self.__points += (len(new_word))**2
            self.__listbox.insert(0, new_word)
            self.update_score(self.__points)
        self.delete_word()

    def delete_word(self):
        self.__operator = ''
        self.__text_input.set("")
        self.__clicked_coor = []
        for button in self.__buttons_list:
            button.config(bg="powder blue")

    def delete(self):
        Button(self.__leftframe, width=4, height=1, padx=18,
               pady=12,
               bd=10, fg="black", font=('ariel', 20, 'bold'), text="delete",
               command=self.delete_word,
               bg="red"
               ).grid(row=6, column=2, columnspan=6)

    def valid_check(self, char):
        if len(self.__clicked_coor) == 0:
            self.btn_click(char)
        char_row, char_column = char[2]
        last_coor = self.__clicked_coor[-1]
        if (char_row, char_column) not in self.__clicked_coor:
            if math.fabs(char_row - last_coor[0]) <= 1:
                if math.fabs(char_column - last_coor[1]) <= 1:
                    self.btn_click(char)

    def btn_click(self, char):
        self.__clicked_coor.append(char[2])
        self.__operator = self.__operator + char[0]
        self.__buttons_list[char[1]].config(bg="blue")
        self.__text_input.set(self.__operator)

    def char_btns(self):
        my_squares = self.squares
        for i in range(len(my_squares)):
            my_row, my_column = my_squares[i].get_coor()
            my_char = my_squares[i].get_char()
            self.__buttons_list.append(Button(self.__leftframe, width=2, height=1,
                                   padx=18,
                          pady=12,
                   bd=10, fg="black", font=('ariel', 20, 'bold'),
                   text=my_char, bg="powder blue",
                   command=lambda char=(my_char, i, (my_row, my_column)): self.valid_check(char)
                   ))
            self.__buttons_list[i].grid(row=1 + my_row, column=my_column)

    def list_box(self):
        label = Label(self.__topframe,
                      text="words you found" + '\n',
                      font="ariel")
        self.__listbox = Listbox(self.__topframe, height=20, width=20)

        label.pack()
        self.__listbox.pack(side=BOTTOM)

    def txtdisplay(self):
        entry = Entry(self.__leftframe, width=23, font=('ariel', 20,
                                                        'bold'),
                      textvariable=self.__text_input, bd=15, insertwidth=4,
                      bg="powder blue",
                      justify="left").grid(row=0, columnspan=4)
        return entry

    def game_over(self):
        msgbox = messagebox.askquestion('game over',
        'you got ' + str(self.__points) + ' points' + '\n' + 'do you want '
                                                             'play again?', icon='question')
        if msgbox == 'no':
            self.__screen.destroy()
        else:
            self.__end_game = True

    # def get_end_game(self):
    #     return self.__end_game



# def start_new_game():
#     main.main()


