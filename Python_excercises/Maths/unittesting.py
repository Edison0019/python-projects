import sys

def test(valuetoevaluate):
    #this prints the result of a test and return its positions within the code. this is good for debuggin
    linenum = sys._getframe(1).f_lineno
    if valuetoevaluate:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)