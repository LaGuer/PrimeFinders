# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:43:39 2019
@author: LaGuer
"""
import codecs
import io
import os
import time
import random

HERE = os.path.abspath(os.path.dirname(__file__))

def crypto_random():
    """ Should print a random for cryptographic use that is not a pseudo random."""
    key_num = random.SystemRandom()
    # key_num.randint(0, sys.maxint) # produces an integer between 0 and the highest allowed by the OS.

    return key_num.random()

# --- FILE --- #
def save(string, name="prime"):
    """
    Write the string into a text file
    The file is called 'name + the time' (format YYYY-mm-dd)
    """
    os.getcwd()

    file = open(str(name) + "_" + str(time.strftime('%Y-%m-%d')) + '.txt', 'w')
    file.write(string)
    file.close()

    return os.path.realpath(file.name)


def read_into_lines_list(path, n=0):
    """
    Take a file and store all of its content into a list
    The n allow to skip the n number of lines
    Return a list of string
    """
    content = []
    with open(path, 'r') as file:
        content = file.readlines()

    return content[n:]


def read_with_codecs(*parts):
    """Return multiple read calls to different readable objects as a single
    string."""
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(HERE, *parts), 'r').read()


def read_advance(*filenames, **kwargs):
    """
    :param filenames:
    :param kwargs:
    :return:
    """
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)



# def convert(markdown_path):
#    """Convert a Markdown file to a reStructuredText file with the pypandoc"""
#    try:
#        import pypandoc
#        output = pypandoc.convert(markdown_path, 'rst')
#        # pypandoc.convert(markdown_path, 'rst', outputfile="README.rst") # Create the rst file
#    except(IOError, ImportError):
#        output = open(markdown_path).read()

#    return output
    


# --- TIME --- #
def timex(func, *param):
    """
    Calculates the time a function takes to run
    Return the function's time
    """
    t = time.time()
    func(*param)
    t = time.time() - t

    return t
