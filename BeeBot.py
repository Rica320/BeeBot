#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:31:51 2020

@author: ricardo
"""

from selenium import webdriver
from time import sleep

file = open("Bee", "r")
r = open("est","r")

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/?hl=eg")

sleep(4)

# just in case its not in english...

driver.find_element_by_xpath(("//select[@class='hztqj']"))\
    .click()

sleep(6)
# need to accept terms (cookies) by yourself

driver.find_element_by_xpath(('//input[@name=\"username\"]'))\
    .send_keys(('name')) # insert name    
driver.find_element_by_xpath(('//input[@name=\"password\"]'))\
    .send_keys(('password')) # insert password 
driver.find_element_by_xpath(('//button[@type="submit\"]'))\
    .click()
    
sleep(5)  

driver.find_element_by_xpath(("//button[contains(text(),'Not Now')]"))\
    .click()
driver.find_element_by_xpath(("	//button[contains(@class,'HoLwm')]"))\
    .click()
sleep(5)  

driver.find_element_by_xpath(("//a[@class='xWeGp']//*[contains(@class,'_8-yf5')]"))\
    .click()
sleep(5)
driver.find_element_by_xpath(("//span[contains(@class,'R19PB')]"))\
    .click()


# 2 options::::

# for i in file:
#     i = i.rstrip()
#     if len(i)>0:
#         i = i.split()
#         for word in i:
#             driver.find_element_by_xpath(("//textarea[@placeholder='Mensagem...']"))\
#     .send_keys(word)
#             driver.find_element_by_xpath(("//button[contains(text(),'Enviar')]"))\
#     .click()

for i in r:
    i = i.rstrip()
    if len(i)>0:
        i = i.split()
        while True:
            driver.find_element_by_xpath(("//textarea[@placeholder='Mensagem...']"))\
    .send_keys(i)
            driver.find_element_by_xpath(("//button[contains(text(),'Enviar')]"))\
    .click()
            
