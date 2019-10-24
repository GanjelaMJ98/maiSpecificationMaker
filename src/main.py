from modules.auth_module import authentication


def main():
    print("Start")
    name, status = authentication()
    print("User: " + str(name) + " with status " +str(status))


if __name__ == "__main__":
   main()