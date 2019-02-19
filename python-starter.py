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


class Foo:
    def __init__(self, arg):
        self._arg = arg
        
    def __enter__(self, arg):
        self.__init__(arg)

    def __exit__(self, exception_type, exception_value, traceback):
        print('Error \'{}\' failed with \'{}\':\n{}'.format(exception_type, exception_value, traceback))
        self.crash_close()

    def crash_close(self):
        """
        crash close ensures that errors are effectively traced and
        all dependencies are safely exited
        """
        # TODO add required exits here
        pass
    
    @property
    def arg(self):
        return self._arg
    
    @arg.setter
    def arg(self, value):
        # add value checks here
        self._arg = value

def run():
    pass

def test():
    pass

def main():
    args = parser.parse_args()
    
    if args.isTest:
        test()
    else:
        run()

if __name__ == '__main__':
    main()
