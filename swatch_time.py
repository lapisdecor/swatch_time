#!usr/bin/env/python3

from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from math import floor
import time
import sys

while True:

    current_time = datetime.now()

    BIEL = ZoneInfo("Europe/Berlin")

    dt_biel = current_time.astimezone(BIEL)

    soma = 3600*dt_biel.hour + 60*dt_biel.minute + dt_biel.second
    swatch_time = floor(soma/86.4)
    raw = str(soma/86.4)
    i = raw.find('.')
    centibeats = raw[i: i+3]
    
    #swatch_time = soma/86.4
    print("@" + f"{swatch_time:03}" + centibeats, end='\r')
    sys.stdout.flush()
    time.sleep(0.5)
