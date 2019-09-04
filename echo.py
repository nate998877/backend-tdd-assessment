#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import sys

"""An enhanced version of the 'echo' cmd line utility"""
__author__ = "nate"


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument('text', type=str, help='text to be manipulated')
    parser.add_argument('-u', "--upper", help="convert text to uppercase", action='store_true')
    parser.add_argument('-l', "--lower", help="convert text to lowercase", action='store_true')
    parser.add_argument('-t', "--title", help="convert text to titlecase", action='store_true')
    return parser


def main(args):
    """Implementation of echo"""
    if args.title:
        print(args.text.title(), end = '')
    elif args.lower:
        print(args.text.lower(), end = '')
    elif args.upper:
        print(args.text.upper(), end = '')
    else:
        print(args.text, end = '')


if __name__ == '__main__':
    args = create_parser().parse_args()
    main(args)