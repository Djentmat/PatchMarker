#!/usr/bin/python3
# -*- coding: utf-8 -*-

import keyboard

def get_keycode():
    while True:
        print(keyboard.read_key())


get_keycode()