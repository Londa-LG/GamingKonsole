
class Controller:
    def __init__(self,login,register,dashboard):
        self.login_view = login
        self.register_view = register
        self.dashboard_view = dashboard

        self.login_view.setRedirect(self.redirect)
        self.login_view.setLogin(self.login)

        self.register_view.setRedirect(self.redirect)
        self.register_view.setRegister(self.register)

        self.dashboard_view.setRedirect(self.redirect)

        self.login_view.display()

    def register(self,username,email,password):
        pass

    def login(self,email,password):
        pass

    def redirect(self,view):
        match(view):
            case "login":
                self.register_view.remove()
                self.dashboard_view.remove()
                self.login_view.display()
            case "register":
                self.register_view.display()
                self.dashboard_view.remove()
                self.login_view.remove()
            case "dashboard":
                self.register_view.remove()
                self.dashboard_view.display()
                self.login_view.remove()

