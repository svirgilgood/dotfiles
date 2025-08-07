#!/usr/bin/env bash
#
# https://git.sr.ht/~oscarcp/ghostfiles/tree/master/item/sway_wm/scripts/sway_bar.sh
#
# Date and time
date_and_week=$(date "+%Y-%m-%d")
current_time=$(date "+%H:%M")

###############
# Commands
# #############

# Battery or charger
battery_charge=$(upower --show-info $(upower --enumerate | grep 'BAT') | grep -E "percentage" | awk '{print $2}')
battery_status=$(upower --show-info $(upower --enumerate | grep 'BAT') | grep -E "state" | awk '{print $2}')

# Using MPD to show song playing
song_artist=$(mpc current -f "%artist%")

if [ "$song_artist" = "" ]; then
  song_title="$(basename "$(mpc current -f "%file%")")"
elif [ -n "$song_artist" ]; then
  song_title="$(mpc current -f '%artist% - %title%')"

else
  song_title=""
fi

if [ "$song_title" != "" ]; then
  song_title="$song_title |"
fi

# Network
network=$(ip route get 1.1.1.1 | grep -Po '(?<=dev\s)\w+' | cut -f1 -d ' ')
#network=$(ip route get 1.1.1.1 )
# interface_easyname grabs the "old" interface name before systemd renamed it
#interface_easyname=$(dmesg | grep $network | grep renamed | awk 'NF>1{print $NF}')
ping=$(ping -c 1 www.google.com | tail -1 | awk '{print $4}' | cut -d '/' -f 2 | cut -d '.' -f 1)

# Others
language=$(swaymsg -r -t get_inputs | awk '/1:1:AT_Translated_Set_2_keyboard/;/xkb_active_layout_name/' | grep -A1 '\b1:1:AT_Translated_Set_2_keyboard\b' | grep "xkb_active_layout_name" | awk -F '"' '{print $4}')
loadavg_5min=$(cat /proc/loadavg | awk -F ' ' '{print $2}')

if [ $battery_status = "discharging" ]; then
  battery_pluggedin='⚠'
else
  battery_pluggedin='⚡'
fi

if ! [ $network ]; then
  network_active="⛔"
else
  network_active="⇆"
fi
echo "$song_title ⌨ $language | $network_active $interface_easyname ($ping ms) | 🏋 $loadavg_5min  $battery_pluggedin $battery_charge | $date_and_week 🕘 $current_time"
