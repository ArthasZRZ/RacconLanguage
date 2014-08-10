'''''
opts.py:
    Operator checker. If the parameter is a operator, return its id.

'''''

OPTS_DICT = {
            '+': 0
            }

def opts_checker(opt):
    if OPTS_DICT.has_key(opt) == True:
        return OPTS_DICT[opt]
    return -1
