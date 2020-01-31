'''
This module contains generic utilties used to write scripts by Sean. (Sean-Scripts)
'''

def get_forwarded_sys_args():
    '''Return args after the first "--" in sys.argv'''
    import sys
    return get_forwarded_args(sys.argv[1:])

def get_forwarded_args(args):
    '''Return args after the first "--"'''
    try:
        idx = args.index('--')
        args = args[idx+1:]
    except ValueError:
        pass
    return args
