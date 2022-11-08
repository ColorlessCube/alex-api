#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：alex-api 
@File    ：text.py
@Author  ：alex
@Date    ：2022/11/7 16:04 
"""
import re
import json
from flask import request
from flaskz.rest import init_model_rest_blueprint, get_rest_log_msg
from flaskz.log import flaskz_logger, get_log_data
from flaskz.utils import create_response

from app.api import api_bp
from app.utils import replace_str_by_index


@api_bp.route('/text/format', methods=['POST'])
def format_text():
    request_data = request.json
    text = request_data.get('text')
    response_data = _format_text(text, True, True)
    response_data = create_response(True, response_data)
    flaskz_logger.info(get_rest_log_msg('Format text.', request_data, True, response_data))
    return response_data


def _format_text(text, lower=False, serial=True):
    """
    Add some choices.
    @param text:
    @param lower:
    @param serial:
    @return:
    """
    text = add_word_blank(text)
    if lower:
        text = text.lower()
    if serial:
        text = format_serial(text)
    return text


def add_word_blank(text):
    """
    If the char before words or the char after words is a Chinese character, add a blank between them.
    @param text:
    @param lower:
    @return:
    """
    pattern = re.compile(r'[a-zA-Z0-9.\-_]+')
    res = re.finditer(pattern, text)
    # Record blank count, because the origin text will been changed in the process.
    # When replace the origin word, should add the offset.
    blank_count = 0
    for item in res:
        word = item.group()
        replace = word
        index = item.start() + blank_count
        end = item.end() + blank_count
        before = ''
        after = ''
        if index > 0:
            before = text[index - 1]
        if '\u4e00' <= before <= '\u9fa5':
            replace = ' ' + replace
            blank_count += 1
        if end <= len(text):
            after = text[end]
        if '\u4e00' <= after <= '\u9fa5':
            replace = replace + ' '
            blank_count += 1
        text = replace_str_by_index(text, index, end, replace)

    return text


def format_serial(text):
    """
    Format serial number in text, such as 1) or a), change them to 1., which is consistent with Markdown grammar.
    @param text:
    @return:
    """
    text = '\n' + text
    pattern = re.compile(r'\n[0-9a-z]+[）.]+[^ ]{0}')
    serials = re.findall(pattern, text)
    for origin in serials:
        new = '\n' + origin[1] + '. '
        text = text.replace(origin, new)
    text = text[1:]
    return text
