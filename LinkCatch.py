#!/usr/bin/env python3
#https://github.com/emrekybs
import sys,os,time,requests
from bs4 import BeautifulSoup

print ("""
\033[39m 
#                                #####
#           #    #    #  #    # #     #    ##     #####   ####   #    #
#           #    ##   #  #   #  #         #  #      #    #    #  #    #
#           #    # #  #  ####   #        #    #     #    #       ######
#           #    #  # #  #  #   #        ######     #    #       #    #
#           #    #   ##  #   #  #     #  #    #     #    #    #  #    #
#######     #    #    #  #    #  #####   #    #     #     ####   #    #
 
\033[35m                                                 |By Emre Koybasi github: https://github.com/emrekybs|                            

""")

try:

	link = input("\033[33m  Website: ")

	start1 = link.startswith('http')
	start2 = link.startswith('https')
	if(start1 == False or start2 == False):
		link2 = ("https://" + link)
		if(len(link) == 0):
			print(" \n \033[33m Url Undefined")

		else:
			response = requests.get(link2)
			content = response.content
			soup = BeautifulSoup(content, "lxml")
			links = soup.find_all('a')
			for link in links:
				href = link.get('href')
				print( "\n\033[91m  Link Found: " + str(href))
				time.sleep(1)

except KeyboardInterrupt as exitt:
		sys.exit()
