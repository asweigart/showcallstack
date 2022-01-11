"""showcallstack
By Al Sweigart al@inventwithpython.com

Shows a simplified view of the call stack."""

__version__ = '0.2.1'

import traceback, inspect, pprint


def showcallstack():
    print('\n'.join(getcallstack()))


def getcallstack():
    outputStrings = []

    tracebackInfo = list(reversed(traceback.extract_stack()[:-2]))
    localVars = []
    frame = inspect.currentframe().f_back
    while frame is not None:
        currentLocalVars = dict(frame.f_locals)
        if 'showcallstack' in currentLocalVars:
            del currentLocalVars['showcallstack']
        if 'getcallstack' in frame.f_locals:
            del currentLocalVars['getcallstack']

        localVars.append(currentLocalVars)
        frame = frame.f_back

    # Get rid of frame/global variables in the global scope.
    tracebackInfo.pop()
    localVars.pop()

    tracebackInfo.reverse()
    localVars.reverse()

    # Display the frame and local variable info:
    outputStrings.append('The call stack is %s call(s) deep:' % (len(tracebackInfo)))
    if len(tracebackInfo) == 0:
        # Show a special message explaining that we were called from the global scope.
        outputString.append('  showcallstack() was called in the global scope and not in a function call.')
        ouptutString.append('')
        return outputStrings

    outputStrings.append('(Here is the "bottom" of the call stack.)')
    for i, v in enumerate(tracebackInfo):
        outputStrings.append('Function/method: %s(), Local variables: ' % (v.name) + pprint.pformat(localVars[i]))

    outputStrings.append('(Here is the "top" of the call stack.)')
    outputStrings.append('')
    return outputStrings

