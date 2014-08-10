'''''
parser.py:
    General parser module of Raccon Language. Mainly used to recognize
    these formats:
    * [operator] [item]

    It will take only one line as the parse target.

'''''

import sys
import opts as opts_module

def parser(target_line):
    _target_list = target_line.split(' ')
    
    if len(_target_list) == 0:
        return None

    _opt = _target_list[0]
    _opt = opts_module.opts_checker(_opt)
    _item = _target_list[0:]
    if _opt != -1:
        _item = _target_list[1:]

    return (_opt, _item)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "Usage: [file for parser]"
    else:
        f = open(sys.argv[1], "r")
        for ln in f.readlines():
            print parser(ln)
