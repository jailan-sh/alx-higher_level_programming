#!/usr/bin/python3
def multiple_returns(sentence):
    tuplec = ()
    if sentence == "":
        tuplec = (0, None)
    else:
        tuplec = (len(sentence), sentence[0])
    return tuplec
