import sys
import scanenv
from pyfiglet import Figlet


def banner(titel):
    f = Figlet(font='avatar')
    print(f.renderText(titel))

class ExploitController:

    def __init__(self) -> None:
        pass


def main():

    try:

        banner("PY$SPLOIT")



    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        print(f"[-] Error occured - {e}")
        sys.exit()

if __name__ == '__main__':

    main()