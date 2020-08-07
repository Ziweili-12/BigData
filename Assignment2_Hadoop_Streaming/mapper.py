import sys
import re
import datetime
from time import strptime

if __name__ == '__main__':
    for line in sys.stdin:
        results = re.findall("[0-9]+/([a-zA-Z]+)/(\d\d\d\d):[0-9]+:", line)
        for x in results:
            year = x[1]
            month = x[0]
            month_int = str(strptime(month, '%b').tm_mon).zfill(2)
            final1 = year + '-' + month_int
            sys.stdout.write("{}\t1\n".format(final1))







