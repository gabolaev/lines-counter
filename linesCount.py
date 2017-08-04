#(for python2)
# -*- coding: utf-8 -*-
import argparse
import sys

def argumentsParser():

    parser = argparse.ArgumentParser('Get the number of lines in a file. \\ Рассчёт количества строк в файле.')
    parser.add_argument('-p', '--path', nargs=1, type=str, help='File full path. \\ Полный путь файла.')
    parser.add_argument('-b', '--buff', nargs=1, type=int, help='Buffer (chunk) size. \\ Размер буфера. (Default: 8192)')

    return parser

def getLinesCount(pathToFile, bufferSize):
    with open(pathToFile, 'r') as f:
        print(sum(chunk.count('\n') for chunk in iter(lambda: f.read(bufferSize), '')))

namespace = argumentsParser().parse_args(sys.argv[1:])

try:
    getLinesCount(namespace.path[0], namespace.buff[0] if namespace.buff else 8192)
except Exception as ex:
    print("{} \n See --help.".format(ex))
