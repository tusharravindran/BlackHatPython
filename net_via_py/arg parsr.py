import argparse
'''
parser = argparse.ArgumentParser()
parser.parse_args()
'''

'''
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
'''
parser = argparse.ArgumentParser()
'''
parser.add_argument("square", help="display a square of a given number", type = int)
args = parser.parse_args()
print(args.square**2)
'''
'''
parser.add_argument("-v","--verbosity", help="increase output verbosity",action="store_true")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")'''
'''
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print("the square of {} equals {}".format(args.square, answer))
else:
    print(answer)
'''
'''
parser.add_argument("square", type=int,
                    help="display a square of a given number")
#parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
 #                   help="increase output verbosity")
parser.add_argument("-v", "--verbosity", type=int,help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity >= 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
    '''
#Advancedd
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
elif args.verbosity >= 1:
    print("{}^{} == {}".format(args.x, args.y, answer))
else:
    print(answer)