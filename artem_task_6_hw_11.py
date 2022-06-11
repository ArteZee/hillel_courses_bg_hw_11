def example_1():
    for i in range(3):
        try:
            x: int = int(input("enter a number: "))
            y: int = int(input("enter another number: "))
            print(x, '/', y, '=', x / y)
        except ZeroDivisionError:
            print("You cant division on zero!")


def example_2(user_list: list ):

    print("\n\nExample 2")

    sum_of_pairs = []

    for i in range(len(user_list)-1):
        try:
            sum_of_pairs.append(user_list[i] + user_list[i + 1])
        except Exception as a:
            print("Oops you got the problem - ", a)

    print("summarize of pairs = ", sum_of_pairs)


def get_upper_file(file_name):
    file = open(file_name, "r")
    for line in file:
        print(line.upper())
    file.close()


def main():
    example_1()
    data_list= [10, 3, 5, 6, 9, 3]
    example_2(data_list)
    example_2([10, 3, 5, 6, "NA", 3])
    try:
        get_upper_file("doesNotExistYest.txt")
        get_upper_file("./Dessssktop/misspelled.txt")
    except Exception as w:
        print("\n\nOops in get_upper_file", w )



main()