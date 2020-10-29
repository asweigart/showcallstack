# showcallstack
Shows a simplified view of the call stack.

This module is similar to Python's built-in `traceback` and `inspect` modules, but is easier to use and displays more simple output. This module is useful for demonstrating what the call stack looks like during recursive function calls.

Example Usage
=============

This program...

    from showcallstack import showCallStack

    def a():
        varA = 42
        b()

    def b():
        varB = 86
        c()

    def c():
        varC = 99
        showCallStack()

    a()

...outputs this:

    The call stack is 3 call(s) deep:
    Function/method: a(), Local variables: {'varA': 42}
    Function/method: b(), Local variables: {'varB': 86}
    Function/method: c(), Local variables: {'varC': 99}

This recursive factorial program...

    from showcallstack import showCallStack

    def factorial(num):
        showCallStack()
        if num == 1:
            return 1
        else:
            return num * factorial(num - 1)

    factorial(4)

...outputs this:

    The call stack is 1 call(s) deep:
    Function/method: factorial(), Local variables: {'num': 4}

    The call stack is 2 call(s) deep:
    Function/method: factorial(), Local variables: {'num': 4}
    Function/method: factorial(), Local variables: {'num': 3}

    The call stack is 3 call(s) deep:
    Function/method: factorial(), Local variables: {'num': 4}
    Function/method: factorial(), Local variables: {'num': 3}
    Function/method: factorial(), Local variables: {'num': 2}

    The call stack is 4 call(s) deep:
    Function/method: factorial(), Local variables: {'num': 4}
    Function/method: factorial(), Local variables: {'num': 3}
    Function/method: factorial(), Local variables: {'num': 2}
    Function/method: factorial(), Local variables: {'num': 1}

You can also call the `showcallstack.getCallStack()` function to get this output as a list of strings.
