#!/usr/bin/env python3
from os import listdir
from importlib import import_module
from random import choice as rchoice
from bot import config_dict, LOGGER
from bot.helper.themes import skull

AVL_THEMES = {
    theme[5:-3]: import_module(f'bot.helper.themes.{theme[:-3]}')
    for theme in listdir('bot/helper/themes')
    if theme.startswith('skull_') and theme.endswith('.py')
}

def BotTheme(var_name, **format_vars):
    text = None
    theme_ = config_dict['BOT_THEME']

    if theme_ in AVL_THEMES:
        text = getattr(AVL_THEMES[theme_].SKULL(), var_name, None)
        if text is None:
            LOGGER.error(f"{var_name} not Found in {theme_}. Please recheck with Official Repo")
    elif theme_ == 'random':
        rantheme = rchoice(list(AVL_THEMES.values()))
        LOGGER.info(f"Random Theme Chosen: {rantheme}")
        text = getattr(rantheme.SKULL(), var_name, None)
        
    if text is None:
        text = getattr(skull.SKULL(), var_name)

    return text.format_map(format_vars)
