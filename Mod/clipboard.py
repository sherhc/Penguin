#!/usr/bin/env python
# -*- coding: utf-8 -*-

import win32clipboard

def readclipb():
    win32clipboard.OpenClipboard(0)
    try:
        copytext=win32clipboard.GetClipboardData()
    except TypeError:
        copytext='Data in clipboard is not TEXT FORMAT!'
    else:
        return copytext
    win32clipboard.CloseClipboard()