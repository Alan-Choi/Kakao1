def main():
    n = set_length()
    m1 = fill_map1(n)  # Store decimal input to arr1
    m2 = fill_map2(n)  # Store decimal input to arr2
    m3 = fill_map3(n, m1, m2)  # Combine map1 and map2 to create map3 using bitwise operation, and append the end
    # value after converting to binary
    show_map1(n, m1)  # Convert decimal values to binary and display map 1
    print('+')
    show_map2(n, m2)  # Convert decimal values to binary and display map 2
    print('=')
    show_map3(n, m3)  # Display map 3


def set_length():
    repeat = True
    while repeat:
        try:
            n = int(input("Enter the length of a side between 1 and 16: "))
            if 1 <= n <= 16:  # 1 ≦ n  ≦ 16
                return n
            else:
                print("Value out of range. Input an integer between 1 and 16.")
        except ValueError:
            print("Invalid entry. Input an integer between 1 and 16.")


def fill_map1(n):
    repeat = True
    arr1 = []
    while repeat:
        try:
            for i in range(0, n, 1):
                x = int(input("Enter an integer for element #" + str(i + 1) + " for array 1: "))
                arr1.append(x)
                repeat = False
        except ValueError:
            print("Invalid entry. Input an integer between 1 and 16.")

    return arr1


def fill_map2(n):
    repeat = True
    arr2 = []
    while repeat:
        try:
            for i in range(0, n, 1):
                x = int(input("Enter an integer for element #" + str(i + 1) + " for array 2: "))
                arr2.append(x)
                repeat = False
        except ValueError:
            print("Invalid entry. Input an integer between 1 and 16.")

    return arr2


def fill_map3(n, m1, m2):
    arr3 = []  # Binary map 3
    for i in range(0, n, 1):
        m3 = m1[i] | m2[i]  # Bitwise Operation
        arr3.append(format(m3, '010b'))

    return arr3


def show_map1(n, m1):
    bimap1 = []  # Binary map 1
    for i in range(0, n, 1):
        bimap1.append(format(m1[i], '010b'))
        bimap1[i] = bimap1[i].replace('1', '#')  # Replace 1's with #'s
        bimap1[i] = bimap1[i].replace('0', ' ')  # Replace 0's with spaces
        print(bimap1[i])
    print()


def show_map2(n, m2):
    bimap2 = []  # Binary map 2
    for i in range(0, n, 1):
        bimap2.append(format(m2[i], '010b'))
        bimap2[i] = bimap2[i].replace('1', '#')  # Replace 1's with #'s
        bimap2[i] = bimap2[i].replace('0', ' ')  # Replace 0's with spaces
        print(bimap2[i])

    print()


def show_map3(n, m3):
    for i in range(0, n, 1):
        m3[i] = m3[i].replace('1', '#')  # Replace 1's with #'s
        m3[i] = m3[i].replace('0', ' ')  # Replace 0's with spaces
        print(m3[i])


main()
