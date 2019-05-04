import menu


def check(num):
    commands = {
        '1': ui.print_tasks,
        '2': ui.add_tasks,
        '3': delete_tasks,
        '4': update_tasks
    }
    if num in commands:
        commands[num]()
    else:
        return num


def controll():
    if check(menu.menu2()) == 0:
        check_in = input("Do you want exit from program Y/N ?")
        if check_in.lower == "n":
            controll

    else:
        controll


if __name__ == '__main__':
    inp = menu.menu1()

    if inp == '1':
       # server part  
    if inp == '2':
        controll()
