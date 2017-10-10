from guizero import *


def calc_sum():
    total = 0
    num = tbxNum.get()
    if num.isdigit():
        if int(num) >= 2:
            for each in range(2, int(num) + 1):
                total += 1 / each
            txtSum.set(total)
        else:
            error(title="Data Entry Error", text="'n' must be >= 2")
    else:
        error(title="Data Entry Error", text="'n' must be an integer")


window = App(title="Sum a Series", width=300, height=250, layout="grid")

Text(window, text="     ", grid=[0, 0])  # spacer

Text(window, text="Series:", grid=[1, 1], align="right")
Text(window, text="1/2 + 1/3 + 1/4 + ... + 1/n",
     grid=[1, 2], align="left")

Text(window, grid=[2, 0])  # spacer

Text(window, text="n = ", grid=[3, 1], align="right")
tbxNum = TextBox(window, grid=[3, 2], align="left")

Text(window, grid=[4, 0])  # spacer

Text(window, text="Sum = ", grid=[5, 1], align="right")
txtSum = Text(window, grid=[5, 2], align="left")

Text(window, grid=[6, 0])  # spacer

PushButton(window, text="Calc Sum", command=calc_sum, grid=[7, 1])
PushButton(window, text="  Quit  ", command=quit, grid=[7, 2])

window.display()
