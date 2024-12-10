# Title: Tools XTurbo
# Author: Alex Colombari - github.com/alexcolombari
# Date: 11/11/2024
# Created to daily use of support team of XTurbo Provedor de Internet

from xtb_tools import *

# CONSTANTS
PORTS_XTB = [80,443,8080,5296,51010]


def main():
	while True:
		try:
			clear_screen()
			print('----- Tools - Support -----')
			print('\n1 - MAC Vendors\n2 - Port Scanner\n3 - Ping / Tracer\n4 - Whois\n5 - DNS "dig"\n6 - Verify BGP ASN')
			print('\n---------------------------------')
			option = input('\nChoose an option: ')

			if option == '1':
				mac_vendors()
			elif option == '2':
				port_scan()
			elif option == '3':
				ping_tracer()
			elif option == '4':
				whois_check()
			elif option == '5':
				dns_check()
			elif option == '6':
				bgp_check()
			else:
				print('\n[INFO] Choose a valid option...')
				time.sleep(3)
				main()
		except KeyboardInterrupt:
			main()


if __name__ == '__main__':
	main()