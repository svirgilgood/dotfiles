#!/bin/bash 

time="$(date '+%Y_%m_%d_%H_%M_%S')";

maim -s /tmp/screenshot_$time.png 2> /dev/null 

