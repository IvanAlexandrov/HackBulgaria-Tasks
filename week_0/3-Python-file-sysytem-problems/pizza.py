import os
from time import time
from datetime import datetime
order_dict = {}


def take(name, price):
    price = float(price)
    if name in order_dict:
        order_dict[name] += price
    else:
        order_dict[name] = price
    print("Taking order from %s for %.2f" % (name, price))
    return order_dict


def status(orders):
    for client in orders.keys():
        print(client + " - %.2f" % float(orders[client]))
    return True


def save(orders):
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    orders_list = open("orders.txt", "a+")
    num_lines = sum(1 for line in open("orders.txt"))
    orders_list.write('[' + str(num_lines + 1) + ']' +
                      ' - orders_' + stamp + '\n'
                      )
    orders_list.close()

    fp = open("orders_" + stamp + '.txt', "w")
    for client in orders.keys():
        fp.write(client + " - %.2f" % orders[client] + '\n')
    fp.close()
    orders.clear()
    print("Saved the current order to" + "orders_" + stamp + '.txt')
    return True


def list_():
    if os.path.exists("orders.txt"):
        fp = open("orders.txt", "r")
        print(fp.read())
        fp.close()
        return True
    return False


def load(command):
    order = command.split(" ")
    index = '[' + order[1] + ']'
    file_name = ''
    fp = open("orders.txt", "r")

    for line in fp:
        if line.startswith(index):
            file_name = line.split(" - ")[1].rstrip("\n")
    fp.close()

    print("Loading orders " + file_name)
    fp = open(file_name + ".txt", "r")
    content = []

    for line in fp:
        content += line.rstrip("\n").split(" - ")
    fp.close()

    names = content[::2]
    prices = content[1::2]
    orders = dict(zip(names, prices))

    return orders


def main():
    print("Enter one of the following commands:\n"
          "take <name> <price> - place your order\n"
          "status - check the order status \n"
          "save - save order\n"
          "list - shows saved orders\n"
          "load <number> - load a saved order\n"
          "finish - exit the program")

    command = input("Enter your command> ")
    orders = {}
    is_saved = False
    is_empty = True
    is_printed = False

    discard = False

    while command != 'finish':
        discard = False
        if command.startswith('take'):
            order = command.split(" ")
            name = order[1]
            price = order[2]
            order = take(name, price)
            orders[name] = order[name]
            is_saved = False
            is_empty = False
        elif (command == 'status'):
            status(orders)

        elif command == 'save':
            is_saved = True
            is_printed = False
            save(orders)

        elif command == 'list':
            list_()
            is_printed = True

        elif command.startswith('load'):
            if is_printed is False:
                print("Use list command before loading")

            elif is_empty is True:
                orders = load(command)

            elif is_saved is False and discard is False:
                discard = True
                print("You have not saved the current order.\n"
                      "If you wish to discard it, type load <number> again.")

            elif is_saved is False and discard is True:
                orders.clear()
                orders = load(command)

        else:
            print("Unknown command! \n"
                  "Try one of the following:\n"
                  "take <name> <price>\n"
                  "status\n"
                  "save\n"
                  "list\n"
                  "load <number>\n"
                  "finish\n"
                  )

        command = input("Enter your command> ")

    else:
        if is_saved is False and is_empty is False:
            print("You have not saved your order.\n"
                  "If you wish to continue, type finish again.\n"
                  "If you want to save your order, type save\n"
                  )
            command = input("Enter your command> ")
            if command == 'save':
                save(orders)
                print("Your order has been saved. Goodbye!")
            elif command == 'finish':
                print("Finishing order. Goodbye!")
        else:
            exit()


if __name__ == '__main__':
    main()
