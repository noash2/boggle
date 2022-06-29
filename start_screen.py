from tkinter import *
from screen import *
from PIL import ImageTk

class Start_screen:
    def __init__(self):
        self.__start_screen = Tk()
        self.__start_screen.geometry("465x500")

    def start_menu(self):
        canvas = Canvas(self.__start_screen, width=550, height=300,)
        canvas.pack(expand=YES, fill=BOTH)

        image = ImageTk.PhotoImage(file="Bogg.png")
        canvas.create_image(10, 10, image=image, anchor=NW)

        start_button = Button(self.__start_screen, width=10, height=1, padx=18,
                              pady=12, bd=10, fg="black", font=('ariel', 20, 'bold'),
                              text="start game",
                              command=self.create_game_screen, bg="pink")
        start_button.pack()
        self.__start_screen.mainloop()

    def create_game_screen(self):
        self.__start_screen.destroy()



