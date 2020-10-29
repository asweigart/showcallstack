"""ShowCallStack
By Al Sweigart al@inventwithpython.com

Shows a simplified view of the call stack."""

__version__ = '0.1.0'

import traceback, inspect, pprint



def showCallStack():
    print('\n'.join(getCallStack()))



def getCallStack():
    outputStrings = []

    tracebackInfo = list(reversed(traceback.extract_stack()[:-2]))
    localVars = []
    frame = inspect.currentframe().f_back
    while frame is not None:
        localVars.append(frame.f_locals)
        frame = frame.f_back

    # Get rid of frame/global variables in the global scope.
    tracebackInfo.pop()
    localVars.pop()

    tracebackInfo.reverse()
    localVars.reverse()

    # Display the frame and local variable info:
    outputStrings.append('The call stack is %s call(s) deep:' % (len(tracebackInfo)))
    for i, v in enumerate(tracebackInfo):
        outputStrings.append('Function/method: %s(), Local variables: ' % (v.name) + pprint.pformat(localVars[i]))

    outputStrings.append('')
    return outputStrings

