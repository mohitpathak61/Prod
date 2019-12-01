#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:40:16 2019

@author: m
"""

while True:
	try:
		cal = Calculator(raw_input("Enter An Equation: ")) #You may need to change raw_input to input if you are using python 3
		print(cal.result)
	except:
		print("Sorry There's an error")