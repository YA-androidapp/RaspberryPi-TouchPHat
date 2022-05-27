#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.
#
# https://learn.pimoroni.com/article/getting-started-with-touch-phat


import sys
import time
import touchphat


stopped = True
runtime = 0


@touchphat.on_touch("Enter")
def start_stop():
    global start
    global stopped
    global runtime
    if stopped:
        touchphat.all_off()
        start = time.time()
        stopped = False
    else:
        stopped = True
        runtime += (time.time() - start)


@touchphat.on_touch("Back")
def reset():
    global runtime
    runtime = 0
    touchphat.all_off()


blanks = " " * 25 + "\r"

try:
    while True:
        if stopped and runtime > 0:
            sys.stdout.write(blanks)
            sys.stdout.write("Timer stopped: %i seconds\r" % runtime)
            sys.stdout.flush()
        elif stopped:
            sys.stdout.write(blanks)
            sys.stdout.write("Touch enter to start!\r")
            sys.stdout.flush()
        else:
            run_sec = int(runtime + time.time() - start) % 60
            run_sec_str = format(run_sec, '06b')
            for led in range(0, 6):
                if run_sec_str[led:led+1] == '1':
                    touchphat.led_on(led+1)
                else:
                    touchphat.led_off(led+1)
            sys.stdout.write(blanks)
            sys.stdout.write("Timer running: %i seconds\r" % run_sec)
            sys.stdout.flush()
        time.sleep(0.1)
except KeyboardInterrupt():
    sys.exit()
