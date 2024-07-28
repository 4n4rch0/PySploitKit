import sys
import scanenv
from pyfiglet import Figlet


def banner(titel):
    f = Figlet(font='avatar')
    print(f.renderText(titel))

class AttackController:

    def __init__(self, user_action):
        self.user_action = user_action

def main():

    try:

        banner("PY$SPLOIT")

        command = input("[1]\tICMP ECHO")
        AttackController(command)


    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        print(f"[-] Error occured - {e}")
        sys.exit()

if __name__ == '__main__':

    main()