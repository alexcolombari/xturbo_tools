# Title: Tools XTurbo
# Author: Alex Colombari - github.com/alexcolombari
# Date: 11/11/2024
# Created to daily use of support team of XTurbo Provedor de Internet

import dns.resolver
import webbrowser
import os, time
import socket

# Clear screen command
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

# Function to verify if the entered IP belongs to CGNAT or not
def cgnat_verify(target):
	ip = target.strip()
	if ip.startswith('100.64.'):
		print('[INFO] Invalid IP! This IP belongs to CGNAT!')
		time.sleep(4)
		port_scan()

# MAC Vendors API function
def mac_vendors():
	while True:
		try:
			clear_screen()
			print('----- Mac Vendors -----')
			mac_addr = input('Enter MAC number: ')
			os.system(f'curl https://api.macvendors.com/{mac_addr}')

			option = input('\n[INFO] Press Enter to continue or type "exit" to go back to main menu: ')
			if option == 'exit':
				main()
		except KeyboardInterrupt:
			main()

# Check BGP
def bgp_check():
	while True:
		try:
			clear_screen()
			print('----- BGP HE -----')
			as_number = input('Enter the BGP ASN to verify: ')
			print('\n[INFO] Wait a moment...')
			time.sleep(2)
			webbrowser.open(f'https://bgp.he.net/AS{as_number}')
			main()
		except KeyboardInterrupt:
			main()

# Ping or Trace Route
def ping_tracer():
	while True:
		try:
			clear_screen()
			print('----- Ping / Tracer -----')
			print('\n1 - Ping\n2 - Tracer\n0 - Main menu')
			option = input('\nSelect an option: ')

			if option == '1':
				target = input('\nEnter the IP or Domain: ')
				print('\n[INFO] Starting...')
				time.sleep(2)
				print('[INFO] Wait a moment...!\n')
				os.system(f'ping {target}')

				option = input('\n[INFO] Press Enter to continue or type "exit" to go back to main menu: ')
				if option == 'exit':
					main()

			if option == '2':
				target = input('\nEnter the IP or Domain: ')
				print('\n[INFO] Starting traceroute test...\n')
				time.sleep(2)
				print('[INFO] Wait until the end of test!\n')
				os.system(f'tracert {target}')

				option = input('\n[INFO] Press Enter to continue or type "exit" to go back to main menu: ')
				if option == 'exit':
					main()

			elif option == '0':
				main()
			else:
				print('[INFO] Choose a valid option...')
				time.sleep(3)
				ping_tracer()
		except KeyboardInterrupt:
			ping_tracer()

# Verify IP Whois
def whois_check():
	while True:
		try:
			clear_screen()
			print('----- Whois -----')
			target = input('Enter an IP to verify: ')
			print('\n[INFO] Starting...\n')
			time.sleep(2)
			webbrowser.open(f'whois.com/whois/{target}')

			option = input('\n[INFO] Press Enter to continue or type "exit" to go back to main menu: ')
			if option == 'exit':
				main()
		except KeyboardInterrupt:
			main()

# DNS "dig"
def dns_check():
	while True:
		try:
			clear_screen()
			print('----- DNS -----')
			domain_name = input('Enter the domain: ')
			dns_server = input('Enter DNS server IP: ')
			print('\n[INFO] Starting...')
			time.sleep(2)

			resolver = dns.resolver.Resolver()
			resolver.nameservers = [dns_server]


			try:
				answers = resolver.resolve(domain_name, 'A')

				for answer in answers:
					print(f'\nIP Address for {domain_name}: {answer.address}')

			except dns.resolver.NoAnswer:
		   		print("No answers were found for the domain.")
			except dns.resolver.NXDOMAIN:
				    print("The domain doesn't exists.")
			except dns.exception.Timeout:
				    print("DNS query timed out.")


			option = input('\n[INFO] Press Enter to continue or type "exit" to go back to main menu: ')
			if option == 'exit':
				main()
		except KeyboardInterrupt:
			main()

# Port Scan
def port_scan():
	while True:
		try:
			clear_screen()
			print('----- Port Scanner -----')
			print('\n1 - Specific Port\n2 - XTurbo Router Ports\n0 - Main Menu')
			option = input('\nSelect an option: ')


			if option == '1':
				clear_screen()
				target = input('Enter the IP or Domain: ')
				cgnat_verify(target)
				port = input('Port: ')
				s = socket.socket()
				s.settimeout(0.05)
				print('\n')
				if s.connect_ex((target, int(port))) == 0:
					print(f'{target} Port {port} [TCP] => Open')
				else:
					print(f'{target} Port {port} [TCP] => Closed')

				option = input('\n[INFO] Press Enter to continue or type "exit" to go back to main menu: ')

				if option == 'exit':
					main()

			elif option == '2':
				clear_screen()
				target = input('Enter the IP or Domain: ')
				cgnat_verify(target)
				s = socket.socket()
				s.settimeout(0.05)
				print('[INFO] Starting...')
				time.sleep(2)
				print('\n')
				for ports in PORTS_XTB:
					if s.connect_ex((target, int(ports))) == 0:
						print(f'{target} Port {ports} [TCP] => Open')

				option = input('\n[INFO] Press Enter to continue or type "exit" to go back to main menu: ')
				if option == 'exit':
					main()

			elif option == '0':
				main()
			else:
				print('\n[INFO] Choose a valid option...')
				time.sleep(3)
				port_scanner()

		except KeyboardInterrupt:
			port_scan()