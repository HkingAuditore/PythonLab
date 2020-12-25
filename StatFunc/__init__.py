import xlwings as xw


@xw.func
def double_sum(x, y):
    return 2 * (x + y)


def main():
    print("Hello World!")


def say_hi():
    print("!")


if __name__ == '__main__':
    main()

import numpy as np
import xlwings as xw


def world():
    wb = xw.Book.caller()
    wb.sheets[0].range('A1').value = 'Hello World!'


say_hi()
