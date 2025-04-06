import customtkinter as ctk

class Dashboard(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        pass

    def setRedirect(self, redirect):
        self.redirect = redirect

    def remove(self):
        pass

    def display(self):
        pass

## Login
class Login_Form(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.create()

    def create(self):

        title_label = ctk.CTkLabel(master = self, text = "Sign in:")
        new_acc_label = ctk.CTkLabel(master = self, text = "Don't have an account?")

        self.email  = ctk.CTkEntry(master = self, placeholder_text = "Email")
        self.password = ctk.CTkEntry(master = self, placeholder_text ="Password")

        button = ctk.CTkButton(master = self, text="Sign in", command = self.submit)
        new_acc_button = ctk.CTkButton(master = self, text="Create a new account", command = self.register)

        self.columnconfigure(index = 0, weight = 1)
        self.columnconfigure(index = 1, weight = 8)
        self.columnconfigure(index = 2, weight = 1)
        self.rowconfigure(index = (0,1,2,3,4,5), weight = 1)

        title_label.grid(pady= 10, row = 0, column = 1, sticky = "nesw")

        self.email.grid(pady= 5, row = 1, column = 1, sticky = "nesw")
        self.password.grid(pady= 5, row = 2, column = 1, sticky = "nesw")

        button.grid(pady= 10,row = 3, column = 1,sticky = "nesw")

        new_acc_label.grid(pady= 10, row = 4, column = 1, sticky = "nesw")
        new_acc_button.grid(pady= 10,row = 5, column = 1, sticky = "nesw")
        

    def display(self):
        self.place(relx = 0.3, rely= 0.25, relwidth = 0.40)

    def set_login(self, login):
        self.login = login

    def submit(self):
        email = str(self.email.get())
        password = str(self.password.get())

        self.login(email,password)
        self.redirect("dashboard")

    def set_redirect(self,redirect):
        self.redirect = redirect

    def register(self):
        self.redirect("register")

## Register
class Register_Form(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.create()

    def create(self):

        title_label = ctk.CTkLabel(master = self, text = "Register")
        have_acc_label = ctk.CTkLabel(master = self, text = "Already have an account?")

        self.username  = ctk.CTkEntry(master = self, placeholder_text = "Username")
        self.email = ctk.CTkEntry(master = self, placeholder_text ="Email address")
        self.password = ctk.CTkEntry(master = self, placeholder_text ="Password")

        button = ctk.CTkButton(master = self, text="Create account", command = self.submit)
        have_acc_button = ctk.CTkButton(master = self, text="Login", command = self.login)

        self.columnconfigure(index = 0, weight = 2)
        self.columnconfigure(index = 1, weight = 6)
        self.columnconfigure(index = 2, weight = 2)
        self.rowconfigure(index = (0,1,2,3,4,5,6), weight = 1)

        title_label.grid(pady= 10, row = 0, column = 1, sticky = "nesw")

        self.username.grid(pady= 5, row = 1, column = 1, sticky = "nesw")
        self.email.grid(pady= 5, row = 2, column = 1, sticky = "nesw")
        self.password.grid(pady= 5, row = 3, column = 1, sticky = "nesw")

        button.grid(pady= 10,row = 4, column = 1,sticky = "nesw")

        have_acc_label.grid(pady= 10, row = 5, column = 1, sticky = "nesw")
        have_acc_button.grid(pady= 10,row = 6, column = 1,sticky = "nesw")
        
    def display(self):
        self.place(relx = 0.3, rely= 0.25, relwidth = 0.40)

    def set_register(self,register):
        self.register = register

    def submit(self):
        username = str(self.username.get())
        email = str(self.email.get())
        password = str(self.password.get())

        self.register(username, email, password)
        self.redirect("dashboard")

    def set_redirect(self,redirect):
        self.redirect = redirect

    def login(self):
        self.redirect("login")

## Account views
class loginView(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.create()

    def create(self):
        self.form = Login_Form(self)

    def setRedirect(self,redirect):
        self.form.set_redirect(redirect)

    def setLogin(self,register):
        self.form.set_login(register)
        
    def display(self):
        self.form.display()
        self.pack(fill = "both", expand = True)

    def remove(self):
        self.pack_forget()

class registerView(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.create()

    def create(self):
        self.form = Register_Form(self)

    def setRedirect(self,redirect):
        self.form.set_redirect(redirect)
        
    def setRegister(self,register):
        self.form.set_register(register)
        
    def display(self):
        self.form.display()
        self.pack(fill = "both", expand = True)

    def remove(self):
        self.pack_forget()
