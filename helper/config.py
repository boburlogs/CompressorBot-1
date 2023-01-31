#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("APP_ID","25409033")
    API_HASH = config("API_HASH","64d00ccecaf56eb88f29df7075d51848")
    BOT_TOKEN = config("BOT_TOKEN","5759879693:AAHsX8yP_t2TgGvVB8OCpBfqi594kPgvb5k")
    OWNER = config("OWNER_ID",5035334529)
    LOG = config("LOG_CHANNEL",-1001696677378)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
