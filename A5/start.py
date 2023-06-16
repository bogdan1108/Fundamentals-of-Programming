from repo import Repository
from UI import UI
from controller import Controller

def start() :
    """
    Starts the application.
    """
    repo = Repository()
    ctrl = Controller(repo)
    ui = UI(ctrl)
    ui.run()

if __name__ == '__main__' :
    start()