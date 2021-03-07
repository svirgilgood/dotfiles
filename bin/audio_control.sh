#!/bin/bash 


OPTION=$1

if [ $OPTION == 'up' ]; then
    pulsemixer --change-volume +5
fi

if [ $OPTION == 'down' ]; then
    pulsemixer --change-volume -5
fi

VOLUME=$(pulsemixer --get-volume | sed 's/\([0-9]*\)/\1\%/g')


notify-send 'Current Volume' "$VOLUME" --icon=dialog-information -t 2000
