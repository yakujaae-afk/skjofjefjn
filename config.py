#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8714143838:AAHy_RyVRchPHxHMOd5w_ssmImCQsH-XHmg")
    # This fetches the env, and if it's empty or None, uses the default string
temp_api_id = os.environ.get("API_ID")
API_ID = int(temp_api_id) if temp_api_id and temp_api_id.strip() else 30296254
    API_HASH = os.environ.get("API_HASH", "c2b5306f4ccd2d795405a026c10b4c62")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7660916897")
