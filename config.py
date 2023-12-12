import os
from dotenv import load_dotenv

import main

load_dotenv()

if main.bot_teste:

    token = os.getenv("TOKEN_TS")
else:
    token = os.getenv("TOKEN_OF")
