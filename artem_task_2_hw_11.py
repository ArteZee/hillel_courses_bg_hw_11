# function with try/except
def foo(word: str, x: int):
    try:
        letter = word[x]
        print(letter)
    except IndexError as a:
        print("Yor index bigger than word", a)


foo("artem", 10)


# function with try/finally
def foo(word: str, x: int):
    try:
        letter = word[x]
        print(letter)
    finally:
        print("it doesnt matter have you problem or not, You still alive! ")


foo("artem", 2)


# create  our class exception
class Mybad(Exception):
    print("You get the wrong way ")
    pass


def doomed():
    raise Mybad()


try:
    doomed()
except Mybad:
    print("Pls change your way")


# function with raise
def foo():
    try:
        raise IndexError
    finally:
        print("You are crazy if You raise up this error")
