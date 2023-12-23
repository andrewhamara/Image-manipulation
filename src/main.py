import sys
from manipulation.grayscale import grayscale

def main():
    filename = sys.argv[1]
    options = sys.argv[2]

    if 'g' in options: # grayscale
        grayscale(filename)

if __name__ == "__main__":
    main()
