def take(name, price):
    pass


def status():
    pass


def save():
    pass


def list_():
    pass


def load(number):
    pass


def finish():
    pass


def main():
    print(
        "Yuo can select one of the options below:\n"
        "\ttake <name> <price>\n"
        "\tstatus\n"
        "\tsave\n"
        "\tlist\n"
        "\tload <number>\n"
        "\tfinish"
        )
    while True:
        user_input = raw_input("Enter a command> ")
        if (user_input.startswith("take")):
            params = user_input.split()
            print("Taking order from %s for %d" %(params[1], params[2]))
            take(params[1], params[2])
        elif ((user_input == 'status')):
            status()
        elif ((user_input == save)):
            save()
        elif ((user_input == 'list')):
            list_()
        elif (user_input == 'finish'):
            finish()
        else:
            print("Invalid option")
    print(user_input)

if __name__ == '__main__':
    main()
