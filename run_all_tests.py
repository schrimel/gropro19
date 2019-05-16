import os
import sys

def main():
    if len(sys.argv) < 2:
        print('Nutzung: ' + sys.argv[0] + ' <executable> [test ordner pfad]')
        return

    if len(sys.argv) > 2:
        test_path = os.path.realpath(sys.argv[2])
    else:
        test_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'tests')

    test_files = [f for f in os.listdir(test_path) if not f.endswith('.gpl')]
    for f in test_files:
        full_path = os.path.join(test_path, f)
        exec_str = sys.argv[1] + ' "' + full_path + '" "' + full_path + '.gpl"'
        exec_str = "python "  + sys.argv[1] + " -i " + full_path + " -o " + full_path + ".gpl"
        print("Starte: " + exec_str)
        os.system(exec_str)


if __name__ == '__main__':
    main()
