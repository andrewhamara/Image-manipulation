import sys
from PIL import Image
from manipulation.grayscale import grayscale
from manipulation.red_to_blue import red_to_blue

def main():
    filename = sys.argv[1]
    options = sys.argv[2]

    if len(sys.argv) < 2:
        print('Usage: python3 main.py <imageName> [-option1] [-option2]')
        sys.exit(1)

    options = [arg for arg in sys.argv[2:] if arg[0] == '-']

    image = Image.open(filename)

    for option in options:
        match option:
            case '-g':
                image = grayscale(image)
            case '-r2b':
                image = red_to_blue(image)

    image.save('updated.jpg')


if __name__ == "__main__":
    main()
