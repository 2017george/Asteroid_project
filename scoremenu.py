from tkinter import *
from GameFunc import *
from File import *

class scoremenu:
    def __init__(self, score, mainmenu, get_top10):
        self.get_top10 = get_top10
        self.score = score
        self.menu = Toplevel()
        self.menu.title("Main Menu")
        self.menu.protocol('WM_DELETE_WINDOW', lambda:self.exit_program())
        self.imgBackground = PhotoImage(file='images/space_background.png')
        self.menu.config(padx=10, background="black")
        self.canvas = Canvas(self.menu, width=self.imgBackground.width(), height=self.imgBackground.height())
        self.menu.geometry("%dx%d+%d+%d" % (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(),self.menu.winfo_screenwidth()//2 - self.canvas.winfo_reqwidth() //2, self.menu.winfo_screenheight()//2- self.canvas.winfo_reqheight() // 2))
        self.menu.grab_set()
        self.background_list = [0] * 2
        self.xpos = [0, self.imgBackground.width()]

        for i in range(len(self.background_list)):
            self.background_list[i] = self.canvas.create_image(self.xpos[i], 0, image=self.imgBackground, anchor='nw')
        self.background_timer()

        self.canvas.pack()

        self.lblLost = Label(self.canvas, font=('neuropol', 14), text="You have lost, But you got the score:", fg="white", bg="black", anchor="c")
        self.lblLost.place(x=self.canvas.winfo_reqwidth() // 4, y= self.canvas.winfo_reqheight() // 2 - 250)
        self.lblScore = Label(self.canvas, font=('neuropol', 14), text=self.score, fg="white", bg="black", anchor="c")
        self.lblScore.place(x=self.canvas.winfo_reqwidth() // 2 - 25, y= self.canvas.winfo_reqheight() // 2 - 200)
        self.btnBack = Button(self.canvas, font=('neuropol', 14), text="BACK", anchor="c", command=lambda:self.goBack(mainmenu))
        self.btnBack.place(x= 0 + self.btnBack.winfo_reqwidth() // 2, y=self.canvas.winfo_reqheight() - self.btnBack.winfo_reqheight() - 10)
        self.btnQuit = Button(self.canvas, font=('neuropol', 14), text="QUIT", anchor="c", command=lambda:self.exit_program())
        self.btnQuit.place(x=self.canvas.winfo_reqwidth() - self.btnQuit.winfo_reqwidth() * 2 - 10, y= self.canvas.winfo_reqheight() - self.btnQuit.winfo_reqheight() - 10)
        lblHighscores = LabelFrame(self.menu, width=700, height=350, bg="black", font="neuropol 14", text="Top 10 Highscores", fg="White")
        lblHighscores.place(x=self.canvas.winfo_reqwidth()//2 , y=self.canvas.winfo_reqheight()//2, anchor="c")
        txtOutput = scrolledtext.ScrolledText(lblHighscores, width=30, height=10, font="Courier 19", padx=5, pady=5, state="disabled")
        txtOutput.pack()
        files = top_file()
        txtOutput.config(state="normal")
        txtOutput.insert(END, "{0:<5s}{1:<15s}{2:<10s}\n\n".format("Rank", "Name","Score"))
        value = 0
        for y in range(len(files.top10())):

            for index, x in enumerate(files.top10()[y]):
                if not index % 2 == 0:
                    txtOutput.config(state="normal")
                    txtOutput.insert(END, "{0:<5d}{1:<15s}{2:<10s}\n".format(value + 1, x.get('name'), str(x.get('score'))))
                    value += 1
                    txtOutput.config(state="disabled")
        self.menu.resizable(False, False)

    def exit_program(self):
        answer = messagebox.askyesno("Asterpocalypse", "Are you sure you want to quit?")
        if answer == True:
            quit()
        else:
            pass
    def background_timer(self):
        global btid
        for i in range(len(self.background_list)):
            self.canvas.coords(self.background_list[i], self.xpos[i] - 5, 0)
            self.xpos[i] -= 5
        btid = self.menu.after(100, lambda: self.background_timer())

        if self.xpos[0] + self.imgBackground.width() <= 0:
            self.xpos[0] = self.xpos[1] + self.imgBackground.width()
        if self.xpos[1] + self.imgBackground.width() <= 0:
            self.xpos[1] = self.xpos[0] + self.imgBackground.width()
    def goBack(self, main_menu):
        self.menu.withdraw()
        self.get_top10()
        main_menu.grab_set()
        main_menu.update()
    def exit_program(self):
        answer = messagebox.askyesno("Asteroid", "Are you sure you want to quit?")
        if answer == True:
            quit()
        else:
            pass
