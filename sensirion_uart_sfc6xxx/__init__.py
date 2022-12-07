#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from .version import version as __version__  # noqa: F401

from sensirion_uart_sfc6xxx.device import Sfc6xxxDevice  # noqa: F401

__all__ = ['Sfc6xxxDevice']
