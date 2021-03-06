# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 13:51:46 2017

@author: allisson
"""

# Function to read HTML codes
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def get_next_target(page):
    
    start_link = page.find('<a href=')
    
    if start_link == -1:
        return None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote