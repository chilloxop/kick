
__author__ = 'JonesBBQ'

import requests
from bs4 import BeautifulSoup
import colorama
import re
from colorama import Fore, Back, Style


print(Fore.RED + """
            ______              
         .-'      `-.           
       .'            `.         
      /                \        
     ;                  ;      
     |                  |;       
     ;                 ;|
     '\               / ;       
      \`.           .' /        
       `.`-._____.-' .'         
         / /`_____.-'           
        / / /                   
       / / /
      / / /
     / / /
    / / /
   / / /
  / / /
 / / /
/ / /
\/_/""")

url = input(Fore.MAGENTA + '\nEnter URL you want to scrap : ')  # makes it more user friendly i guess (note: its full address)
site_data = requests.get(url)
html_element = input('\nEnter elements to target with BeautifulSoup  ||e.g body, table, iframe||  : ')
special_class_tag = input('Enter special class tag ||leave blank for any||  : ')


class sc: # class for all items you want idk
    phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', site_data.text)
    emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', site_data.text)


soup = BeautifulSoup(site_data.text, 'html.parser')

special_html_tag = soup.find(html_element, {'class': special_class_tag})

print('\n######################  ||  REGEX PLAIN PHONE AND EMAIL ||  ######################')
print('\n', sc.phones, sc.emails)
print('\n######################  ||  SOUP PARSED  ||  ######################')
print('\n', soup.text)
print('\n######################  ||  RAW SOUP HTML  ||  ######################')
print('\n', special_html_tag)
print('\n\n\n\n\n\n\n\n\n\n')
print('\nEnd of task')





















