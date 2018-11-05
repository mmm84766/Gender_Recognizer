# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 08:37:50 2016

@author: varshith
"""
print(''' 
us - USA
ar - Argentina
uy - Uruguay
uk - United Kingdom
''')
cclist = ['us','ar','uy','uk']

while True:
    country_code = input('Enter country code :')
    if country_code in cclist:
        break
    else:
        print('Entered country code not valid')

while True:
    name = input('Enter first name :')
    if name.find(' ') != -1:
        print('Entered name not valid, Enter first name only')       
    else:
        break

from gender_detector import GenderDetector
detector = GenderDetector(country_code) 
print(detector.guess(name))

