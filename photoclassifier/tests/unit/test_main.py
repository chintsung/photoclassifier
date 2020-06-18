#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
from nose.tools import assert_equals
from nose.tools import assert_list_equal
from nose.tools import with_setup

import photoclassifier.__main__ as phototool

assert_equals.__self__.maxDiff = None

basepath = os.path.dirname(os.path.realpath(__file__))
photos_dir = os.path.join(basepath, '../data/photos')

expected_recur_pathnames = [
    os.path.join(os.path.abspath(photos_dir), '**/*.jpg'),
    os.path.join(os.path.abspath(photos_dir), '**/*.jpeg'),
    os.path.join(os.path.abspath(photos_dir), '**/*.png'),
]
expected_nonrecur_pathnames = [
    os.path.join(os.path.abspath(photos_dir), '*.jpg'),
    os.path.join(os.path.abspath(photos_dir), '*.jpeg'),
    os.path.join(os.path.abspath(photos_dir), '*.png'),
]

expected_recur_imagefiles = [
    os.path.abspath(os.path.join(photos_dir, 'photo1.png')),
    os.path.abspath(os.path.join(photos_dir, 'photo2.jpg')),
    os.path.abspath(os.path.join(photos_dir, 'photo3.jpeg')),
    os.path.abspath(os.path.join(photos_dir, 'funny/funny-photo1.png')),
    os.path.abspath(os.path.join(photos_dir, 'funny/funny_photo2.jpg')),
]
expected_recurpath_nonrecur_imagefiles = [
    os.path.abspath(os.path.join(photos_dir, 'funny/funny-photo1.png')),
    os.path.abspath(os.path.join(photos_dir, 'funny/funny_photo2.jpg')),
]
expected_nonrecur_imagefiles = [
    os.path.abspath(os.path.join(photos_dir, 'photo1.png')),
    os.path.abspath(os.path.join(photos_dir, 'photo2.jpg')),
    os.path.abspath(os.path.join(photos_dir, 'photo3.jpeg')),
]


def get_imagefiles_setup():
    """setup function for get_imagefiles"""
    expected_recur_imagefiles.sort()
    expected_recurpath_nonrecur_imagefiles.sort()
    expected_nonrecur_imagefiles.sort()


def get_sorted_list(list_):
    """Get sorted list.
    @param list_: List would be sorted.
    @retval Sorted list.
    """
    list_.sort()
    return list_


def test_get_pathnames():
    assert_equals(expected_recur_pathnames,
                  phototool.get_pathnames(photos_dir, True))
    assert_equals(expected_nonrecur_pathnames,
                  phototool.get_pathnames(photos_dir, False))


@with_setup(get_imagefiles_setup)
def test_get_imagefiles():
    assert_list_equal(expected_recur_imagefiles,
                      get_sorted_list(phototool.get_imagefiles(
                        expected_recur_pathnames, True)))
    assert_equals(expected_recurpath_nonrecur_imagefiles,
                  get_sorted_list(phototool.get_imagefiles(
                      expected_recur_pathnames, False)))
    assert_equals(expected_nonrecur_imagefiles,
                  get_sorted_list(phototool.get_imagefiles(
                      expected_nonrecur_pathnames, True)))
    assert_equals(expected_nonrecur_imagefiles,
                  get_sorted_list(phototool.get_imagefiles(
                      expected_nonrecur_pathnames, False)))
