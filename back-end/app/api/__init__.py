#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：alex-api 
@File    ：__init__.py.py
@Author  ：alex
@Date    ：2022/11/7 16:03 
"""
from flask import Blueprint

api_bp = Blueprint('api', __name__)

from .text import *
