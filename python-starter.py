import argparse

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1', 'enable', 'on'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0', 'disable', 'off'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser.add_argument('--test', dest='isTest', const=True, nargs='?', type=str2bool,
                    help='True if testing')
parser.add_argument('--debug', dest='isDebug', help='True for debugging')

def main():
    isTest = False
    isDebug = False

    args = parser.parse_args()
    if args.isTest:
        isTest = True
    if args.isDebug:
        isDebug = True

def test():
  pass

if __name__ == '__main__':
    main()
