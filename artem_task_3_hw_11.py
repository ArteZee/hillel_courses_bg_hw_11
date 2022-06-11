def user_function():
    """
    function do division on two numbers with try/except/finally
    :return: int
    """
    try:
        first_num: int = int(input("Put your first number:\n"))
        second_num: int = int(input("Put your second number:\n"))

        division = first_num / second_num
        print(division)
    except ZeroDivisionError:
        print("ай яй яй делить на ноль можно не многим")
    except Exception as e:
        print("Your problem is -", e)
    finally:
        print("I 'am happy that you learn python")


user_function()
