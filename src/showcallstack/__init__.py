"""showcallstack
By Al Sweigart al@inventwithpython.com

Shows a simplified view of the call stack."""

__version__ = '0.3.0'

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

        if frame.f_back is None:
            # Grab the global variables:
            globalVars = frame.f_globals
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
        outputStrings.append('  showcallstack() was called in the global scope and not in a function call.')
    else:

        outputStrings.append('(Here is the "bottom" of the call stack.)')
        for i, v in enumerate(tracebackInfo):
            outputStrings.append('Local variables of call to %s():' % (v.name))#  + pprint.pformat(localVars[i]))
            for localVarName, localVarValue in localVars[i].items():
                outputStrings.append('  ' + localVarName + ' (type: ' + type(localVarValue).__qualname__ + ') == ' + repr(localVarValue))

        outputStrings.append('(Here is the "top" of the call stack.)')
    outputStrings.append('')

    # Filter the global variables.
    reportedGlobalVars = {}
    for k, v in globalVars.items():
        if k.startswith('__') or inspect.isfunction(v) or inspect.ismodule(v) or inspect.isclass(v):
            # Skip variables that are functions, modules, classes, etc:
            continue
        reportedGlobalVars[k] = (type(v).__qualname__, v)

    outputStrings.append('Global variables:')
    if len(reportedGlobalVars) == 0:
        outputStrings.append('  No global variables.')
    else:
        for k in sorted(list(reportedGlobalVars.keys())):
            varTypeAsStr = reportedGlobalVars[k][0]
            varValueAsStr = repr(reportedGlobalVars[k][1])
            outputStrings.append('  ' + k + ' (type: ' + varTypeAsStr + ') == ' + varValueAsStr)

    outputStrings.append('')
    return outputStrings

