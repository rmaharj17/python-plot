#!/bin/bash/env python3

'''
The sys library connects a Python program to the system it is running on.

The list sys.argv contains the command-line arguments that a program was run with.

Avoid silent failures.

The pseudo-file sys.stdin connects to a program’s standard input.
'''

import sys
import numpy

print("Version is", sys.version)
print("sys.argv is", sys.argv, "\n")      # argv means argument value:

def main():
    script = sys.argv[0]
    # filename = sys.argv[1]        # single fileneme use
    if len(sys.argv) == 1:          # no arguments, so print help message
        print("Usage: python reading.py arguments")
        
        for filename in sys.argv[1:]:
            data = numpy.loadtxt(filename, delimiter=',')
            for row_mean in numpy.mean(data, axis=1):
                print(row_mean)
            print("File calculated successfully\n")

# There is no output because we have defined a function, but haven’t actually called it. Let’s add a call to main:

if __name__ == '__main__':
    main()

# eg: python readings.py --max small-*.csv


'''
import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for filename in filenames:
        data = numpy.loadtxt(filename, delimiter=',')

        if action == '--min':
            values = numpy.min(data, axis=1)
        elif action == '--mean':
            values = numpy.mean(data, axis=1)
        elif action == '--max':
            values = numpy.max(data, axis=1)

        for val in values:
            print(val)

if __name__ == '__main__':
    main()

eg: python readings.py --max small-*.csv
'''

'''
# This is code/readings_08.py
import sys
import numpy

def main():
    script = sys.argv[0]
    if len(sys.argv) == 1: # no arguments, so print help message
        print("""Usage: python readings_08.py action filenames
                action must be one of --min --mean --max
                if filenames is blank, input is taken from stdin;
                otherwise, each filename in the list of arguments is processed in turn""")
        return

    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
            'Action is not one of --min, --mean, or --max: ' + action
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for filename in filenames:
            process(filename, action)

def process(filename, action):
    data = numpy.loadtxt(filename, delimiter=',')
        
    if action == '--min':
        values = numpy.min(data, axis=1)
    elif action == '--mean':
        values = numpy.mean(data, axis=1)
    elif action == '--max':
        values = numpy.max(data, axis=1)
    
    for val in values:
        print(val)

main()
'''
