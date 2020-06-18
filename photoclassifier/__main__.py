#! python 3
# -*- coding: utf-8 -*-
"""
Package: photoclassifier
Brief: Classify photos under date.
"""

import os
import time
import glob
import shutil

from argparse import ArgumentParser


# available image file format list
imagefileformats = ['jpg', 'jpeg', 'png']


def makedirs(path):
    """Create directories recursively.
    @param path: Path of the leaf directory
    """
    if not os.path.isdir(path):
        os.makedirs(path)


def get_pathnames(directory, recursive):
    """Get pathnames in specified directory for pattern matching.
    @param directory: Directory path which photos are in. Can be either
                      absolute (like /usr/image/test) or relative (
                      like ../../image).
    @param recursive: If get path recursively.
    """
    if not os.path.isdir(directory):
        print('Invalid folder name.')
        raise Exception
    pathname = (os.path.join(os.path.abspath(directory), '**/*.') if recursive
                else os.path.join(os.path.abspath(directory), '*.'))
    return [''.join([pathname, fileformat]) for fileformat in imagefileformats]


def get_imagefiles(pathnames, recursive):
    """Get a list of image files.
    @param pathnames: List of pathname for image files matching.
                      To get pathnames from function get_pathnames.
    @param recursive: If get matched image files recursively.
    """
    imagefiles = list()
    for pathname in pathnames:
        imagefiles += glob.glob(pathname, recursive=recursive)
    return imagefiles


def process_image(imagefiles):
    cnt = 0
    try:
        for image in imagefiles:
            localtime = time.localtime(os.path.getmtime(image))
            date = time.strftime('%Y.%m.%d_%w', localtime)
            (head, tail) = os.path.split(image)
            dest = os.path.join(os.path.join(head, date), tail)
            makedirs(os.path.dirname(dest))
            shutil.move(image, dest)
            print('move file {} to {}'.format(image, dest))
            cnt += 1
    finally:
        print('Process {} photos totally.'.format(cnt))


def main(args):
    pathnames = get_pathnames(args.dir, args.recursive)
    imagefiles = get_imagefiles(pathnames, args.recursive)
    process_image(imagefiles)


if __name__ == '__main__':
    folder_help = ''.join(['specified directory to process photos; default is',
                           ' current working directory if ignored this.'])
    parser = ArgumentParser()
    parser.add_argument('-d', '--dir', default=os.getcwd(),
                        help=folder_help,)
    parser.add_argument('-r', '--recursive', action='store_true',
                        default=False,
                        help='process photos in directories recursively',)
    args = parser.parse_args()
    main(args)
