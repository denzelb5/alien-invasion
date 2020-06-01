#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 07:46:43 2019

@author: denisebaker
"""

import sys

import pygame

from rocket import Rocket
from dom_settings import Settings

def run_game():
    """Initialize game."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
            ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Domination")
    
    rocket = Rocket(screen)
    
    
    
    
    # Start the main loop for the game.
    while True:
        
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        rocket.blitme()
                
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
run_game()