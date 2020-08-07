import sys
import re
if __name__ == '__main__':
    
    current_key = None
    total = 0

    for line in sys.stdin:

        key,val = line.split('\t')
        val = int(val)

        if key == current_key:
            total += val
        else:
            if current_key is not None:
                sys.stdout.write('{},{}\n'.format(current_key,total))

            current_key = key
            total = val

    sys.stdout.write("{},{}\n".format(current_key,total))

