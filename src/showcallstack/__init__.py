"""showcallstack
By Al Sweigart al@inventwithpython.com

Shows a simplified view of the call stack."""

__version__ = '0.2.0'

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
    for i, v in enumerate(tracebackInfo):
        outputStrings.append('Function/method: %s(), Local variables: ' % (v.name) + pprint.pformat(localVars[i]))

    outputStrings.append('')
    return outputStrings

