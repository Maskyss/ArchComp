import menu


def check(num):
    # checking menu


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
