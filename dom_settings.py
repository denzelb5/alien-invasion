#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 13:21:20 2019

@author: denisebaker
"""

class Settings():
    """A class to store all settings for Domination."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 76,153)