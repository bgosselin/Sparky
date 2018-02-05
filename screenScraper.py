import re

'''
Screen Scrape VLAN info from the user input
Return the first 1 to 4 digit number as the vlan
'''


def get_vlan(input_string):
    vlan = re.compile(r'\d{1,4}')
    return re.findall(vlan, input_string)[0]


'''
Screen Scrape a MAC address from the user input
'''


def get_mac_address(input_string):
    mac = re.compile(ur'\s(?:[0-9a-fA-F]:?){12}\s')
    return re.findall(mac, input_string)[0]
