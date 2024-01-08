# much thanks to Selenium at hashkiller for implementing the /usr/bin/commander into an emulator to allow debugging
# commander is found in the firmware for the Zyxels LTE3301-M209, LTE3301-Q222, LTE3302-M432 and LTE5366-M608
# four modes in this function cover mode 15,16,19,20,21,22 and all use a sub function in wlan_reset_defaults called create_key_setting
#
# not much is known as no corresponding router has been found that uses these
# it does generate the SSID for a few clues on some
# 15 SSID is %s HHHH (last two bytes of mac)
# 16 SSID is DWR-921-HHHH (always last two bytes of mac)
# 20-21 SSID are Zyxel_HHHH
# 22 two versions of commander either Telia_HHHH or noodoe-LTEHHHH

import hashlib
import argparse

def commander_15s(mac, mode):

	if mode == 1:
		pwd_len = 16
	else:
		pwd_len = 10

	# charset 0 for commander mode 15
	# charset 1 for commander mode 16
	# charset 2 for commander mode 20,21#
	# charset 3 for commander mode 22
	charset = [
		'987654321ABCDEFGHIJKLMNPQRSTUVWXYZ',
		'98765432abcdefghjknpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ',
		'ABCDEFGHJKLMNPQRSTUVWXYZ23456789',
		'98765432abcdefghijkmnpqrstuvwxyz'
	]


	actual_charset = charset[mode]
	filler = 'AMITTW'
	
	mac_bytes = []
	for i in range(0, 12, 2):
		mac_bytes.append(mac[i:i+2].upper())

	input_string = ''
	for i in range(0, 6):
		input_string += filler[i]
		input_string += mac_bytes[i]

	digest = hashlib.sha1()
	digest.update(input_string.encode())
	digest = digest.digest()

	password = ''
	for i in range(0, pwd_len):
		letter = digest[i] % len(actual_charset)
		password += actual_charset[letter]
	print(password)




parser = argparse.ArgumentParser(description='Zyxels LTE3301-M209, LTE3301-Q222, LTE3302-M432 and LTE5366-M608 Keygen')
parser.add_argument('mac', help='Mac address')
parser.add_argument('-mode', help='Mode to use', default=0, type=int)
args = parser.parse_args()

commander_15s(args.mac, args.mode)
