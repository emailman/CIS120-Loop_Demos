from guizero import *


def calc():
    first = tbxFirstInt.get()
    last = tbxLastInt.get()

    # Check if both text boxes contain integers
    if first.isdigit() and last.isdigit():
        # Convert inputs from string to integer
        first_int = int(first)
        last_int = int(last)

        # Check if the integers are out of order
        if first_int <= last_int:
            # Sum the range of integers from first to last
            total = 0
            for each in range(first_int, last_int + 1):
                total += each
                print(each, total)

            # Show the sum
            txtSum.set(total)

        else:
            txtSum.set("")
            warn(title="Data Entry Error",
                  text="First number must be less than last number")
    else:
        txtSum.set("")
        error(title="Data Entry Error",
              text="Missing or non-integer data found")


window = App(title="Sum of Integers", layout="grid",
             height=250, width=280)

Text(window, text="    ", grid=[0, 0])  # Spacer

Text(window, text="First Int  ", grid=[1, 1], align="right")
tbxFirstInt = TextBox(window, grid=[1, 2])

Text(window, grid=[2, 0])  # Spacer

Text(window, text="Last Int  ", grid=[3, 1], align="right")
tbxLastInt = TextBox(window, grid=[3, 2])

Text(window, grid=[4, 0])  # Spacer

Text(window, text="Sum  = ", grid=[5, 1], align="right")
txtSum = Text(window, grid=[5, 2], align="left")

Text(window, grid=[6, 0])  # Spacer

PushButton(window, text="CALC SUM", command=calc, grid=[7, 1],
           align="left")
PushButton(window, text="QUIT", command=quit, grid=[7, 2],
           align="right")

window.display()
