# commader_15spy
Zyxels LTE3301-M209, LTE3301-Q222, LTE3302-M432 and LTE5366-M608 Keygen

Much thanks to Selenium at hashkiller for implementing the /usr/bin/commander into an emulator to allow debugging\
Commander is found in the firmware for the Zyxels LTE3301-M209, LTE3301-Q222, LTE3302-M432 and LTE5366-M608\
Four modes in this function cover mode 15,16,19,20,21,22 and all use a sub function in wlan_reset_defaults called create_key_setting\
Not much is known as no corresponding router has been found that uses these\
It does generate the SSID for a few clues on some\
15 SSID is %s HHHH (last two bytes of mac)\
16 SSID is DWR-921-HHHH (always last two bytes of mac)\
20-21 SSID are Zyxel_HHHH\
22 two versions of commander either Telia_HHHH or noodoe-LTEHHHH

Usage: python3 commander_15s.py 112233445566 -mode 0

Credit to drsnooker for his Matlab script that this was converted from: https://forum.hashkiller.io/index.php?threads/unpublished-wpa-key-algorithms.19944/post-343296
