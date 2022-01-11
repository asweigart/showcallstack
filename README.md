# ShowCallStack

Shows a simplified view of the call stack.

This module is similar to Python's built-in `traceback` and `inspect` modules, but is easier to use and displays more simple output. This module is useful for demonstrating what the call stack looks like during recursive function calls. Simply add a `from showcallstack import showCallStack` line and then call `showCallStack()` from wherever you wish to see the state of the call stack and the local variables in each call frame.

Example Usage
=============

This program...

    from showcallstack import showcallstack

    def a():
        varA = 42
        b()

    def b():
        varB = 86
        c()

    def c():
        varC = 99
        showcallstack()

    a()

...outputs this:

    The call stack is 3 call(s) deep:
    (Here is the "bottom" of the call stack.)
    Function/method: a(), Local variables: {'varA': 42}
    Function/method: b(), Local variables: {'varB': 86}
    Function/method: c(), Local variables: {'varC': 99}
    (Here is the "top" of the call stack.)

This recursive factorial program...

    from showcallstack import showcallstack

    def factorial(num):
        showcallstack()
        if num == 1:
            return 1
        else:
            return num * factorial(num - 1)

    factorial(4)

...outputs this:

    The call stack is 1 call(s) deep:
    (Here is the "bottom" of the call stack.)
    Function/method: factorial(), Local variables: {'num': 4}
    (Here is the "top" of the call stack.)

    The call stack is 2 call(s) deep:
    (Here is the "bottom" of the call stack.)
    Function/method: factorial(), Local variables: {'num': 4}
    Function/method: factorial(), Local variables: {'num': 3}
    (Here is the "top" of the call stack.)

    The call stack is 3 call(s) deep:
    (Here is the "bottom" of the call stack.)
    Function/method: factorial(), Local variables: {'num': 4}
    Function/method: factorial(), Local variables: {'num': 3}
    Function/method: factorial(), Local variables: {'num': 2}
    (Here is the "top" of the call stack.)

    The call stack is 4 call(s) deep:
    (Here is the "bottom" of the call stack.)
    Function/method: factorial(), Local variables: {'num': 4}
    Function/method: factorial(), Local variables: {'num': 3}
    Function/method: factorial(), Local variables: {'num': 2}
    Function/method: factorial(), Local variables: {'num': 1}
    (Here is the "top" of the call stack.)

You can also call the `showcallstack.getcallstack()` function to get this output as a list of strings.

Support
-------

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
