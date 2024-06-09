import pyautogui
import time


def get_positions():
    print('Make Sure That You Are In the home page of TradingView')
    time.sleep(5)
    print(f'Hover your mouse over the search box')

    time.sleep(5)

    searchbox_pos = pyautogui.position()



    print(f'We have secured the position of the search box')
    print(f'Now, search for an arbitrary stock ticker, then move your mouse over the  My script bar')

    time.sleep(20)

    myscript_pos = pyautogui.position()

    print(f'We have secured the position of the My Script bar')
    print(f'Now, move to the more button')
    time.sleep(10)
    more_pos = pyautogui.position()

    print("We have secured the positions of more button")
    print(f'Now, in the appeared menu, move your mouse over the add alert button')
    time.sleep(20)

    add_alert_pos = pyautogui.position()

    print(f'we hve secured the position of the add alert button')
    print(f'Now, In the Opened box, move your mouse over the create button')

    time.sleep(20)

    create_pos = pyautogui.position()

    with open('positions.txt', 'w') as f:
        f.write(str(searchbox_pos) + '\n')
        f.write(str(myscript_pos) + '\n ')
        f.write(str(more_pos) + '\n')
        f.write(str(add_alert_pos) + '\n')
        f.write(str(create_pos) + '\n')


if __name__ == "__main__":

    get_positions()
