import customtkinter as ctk
from controller import Controller
from views import (
    loginView, 
    registerView, 
    Dashboard
)

class Front_End(ctk.CTk):
    def __init__(self,title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        ctk.set_appearance_mode("dark")

        self.controller = Controller(loginView(self), registerView(self), Dashboard(self))

        self.mainloop()


if __name__ == "__main__":
    Front_End("gameKonsle",[800,600])

