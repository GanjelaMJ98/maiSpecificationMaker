import sys
sys.path.append('../GUI/forms')
from modules.auth_module import authentication
from GUI.FirstWindow import FirstWindow
from GUI.CreateProject import CreateProject

def main():
    print("Start")
    name, status = authentication(test = 1)
    print("User: " + str(name) + " with status " +str(status))
    start = FirstWindow()
    print(str(name) + " selected " + str(start))
    if(start == "Create"):
        CreateProject()


if __name__ == "__main__":
   main()