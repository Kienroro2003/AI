# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

if __name__ == '__main__':
    data4 = [1, 2, 3]
    print(data4)
    swap(data4, 0, 2)
    print(data4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
