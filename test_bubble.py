#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from bubble import sort_bubble

lists_to_sort = [([2, 0, 4, 7, -1, 10, 9], [-1, 0, 2, 4, 7, 9, 10]),
                  ([-5, -6, 12, 0, 3, 5, 8], [-6, -5, 0, 3, 5, 8, 12])]


@pytest.mark.parametrize('sample, expected', lists_to_sort)
def test_sort(sample, expected):
    sorted_list = sort_bubble(sample)
    assert sorted_list == expected



