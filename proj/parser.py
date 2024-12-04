import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    # subparsers = parser.add_subparsers(required=True, dest='prog')
    # parser_sub_prog = subparsers.add_parser('sub_prog')
    parser.add_argument('-v', '--verbose', action='store_true', help='enable verbose mode', default=False)
    parser.add_argument('-l', '--log_level', type=str, help='set log level', default="INFO")
    
    return parser