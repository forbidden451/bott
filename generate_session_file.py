# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# This script wont run your bot, it just generates a session.

import os

from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv("config.env")

API_KEY = os.environ.get("API_KEY",1038939)
API_HASH = os.environ.get("API_HASH",4b5cc5f23a205ae8dc9c6280bb10c55b)

bot = TelegramClient('userbot',API_KEY, API_HASH)
bot.start()
