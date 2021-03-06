import getopt
import sys

def main():
    try:
        # getopt.getopt(args, options[, long_options]) 
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    output = None
    verbose = False

    for o, a in opts:
        if o == "-v"
            verbose = True
        elif o in ("-h", "--help") :
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"

if __name__ == "__main__":
    main()
