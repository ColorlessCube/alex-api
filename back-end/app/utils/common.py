#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：back-end 
@File    ：common.py
@Author  ：alex
@Date    ：2022/11/8 10:58 
"""

def replace_str_by_index(string, start, end, sub_str):
    """
    Replace substring by given index.
    @param string:
    @param start:
    @param end:
    @param sub_str:
    @return:
    """
    res = string[:start] + sub_str + string[end:]
    return res