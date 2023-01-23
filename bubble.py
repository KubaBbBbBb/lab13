#!/usr/bin/python
# -*- coding: utf-8 -*-

def sort_bubble(lst_to_change):

    for i in range(0, len(lst_to_change)):
        check = True
        for j in range(0, len(lst_to_change)-i-1):
            if lst_to_change[j+1] < lst_to_change[j]:
                lst_to_change[j + 1], lst_to_change[j] = lst_to_change[j], lst_to_change[j+1]
                check = False
        if check:
            break

    return lst_to_change

