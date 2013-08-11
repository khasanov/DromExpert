#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    DromExpert Parser
    This script should read all html pages in a specific
    directory, extract data and write them to a plain text file.
    Single file is converted into one row.
    Headers of columns are
    Price in rubles, Year, Brand, Model, Engine, Transmission, Drive, Mileage, Wheel, Optional, City, Advertisment number (ID), Date of publication.
"""

import os
from BeautifulSoup import BeautifulSoup

html_directory = "./novosibirsk.drom.ru/lada/2111/"
output_file = "./2111.txt"
data = u""
delimiter = "\t"

def read_file(filePath):
    """ 
       Reads the file and returns its contents as a string.
    """
    try:
        f = open(filePath, "r")
    except IOError:
        print "Could not open file ", filePath

    html = f.read()

    try:
        f.close()
    except IOError:
        print "Could not close file ", filePath

    return html

def write_file(fileContent):
    """
        Gets the contents and writes it to a file.
    """
    try:
        f = open(output_file, "w")
    except IOError:
        print "Could not open file ", output_file

    f.write(fileContent)

    try:
        f.close()
    except IOError:
        print "Could not close file ", output_file


def parse_file(filePath):
    """
        Read advertisement and extract data to the string
    """
    car_price = car_year = car_brand = car_model = car_engine = car_transmission = car_drive = car_mileage = car_wheel = car_optional = adv_city = adv_id = adv_date = u"null"
    columns = []

    soup = BeautifulSoup(read_file(filePath))

    adv_id = os.path.basename(filePath)[:-5]  # cut-off last 5 characters (".html")
    adv_date = soup.find('p', attrs={'class':'autoNum'}).string.split()[-1]
    car_price = soup.find('div', attrs={'class':'price'}).contents[0].string.replace('&nbsp;', '')[:-4]

    tmp = soup.findAll('h3')
    if tmp[0].string == u"Автомобиль продан!":
        car_year = tmp[1].string.split()[-2]
        car_brand = tmp[1].string.split()[0]
        car_model = tmp[1].string.split()[1][:-1]
    else:
        car_year = tmp[0].string.split()[-2]
        car_brand = tmp[0].string.split()[0]
        car_model = tmp[0].string.split()[1][:-1]

    for l in soup.findAll('span', attrs={'class':'label'}):
        if l.next == u"Двигатель:":
            car_engine = l.next.next
        if l.next == u"Трансмиссия:":
            car_transmission = l.next.next
        if l.next == u"Привод:":
            car_drive = l.next.next
        if l.next == u"Пробег, км:":
            car_mileage = l.next.next
        if l.next == u"Руль:":
            car_wheel = l.next.next
        if l.next == u"Дополнительно:":
            car_optional = l.next.next
        if l.next == u"Город:":
            adv_city = l.next.next

    columns.append(car_price)
    columns.append(car_year)
    columns.append(car_brand)
    columns.append(car_model)
    columns.append(car_engine)
    columns.append(car_transmission)
    columns.append(car_drive)
    columns.append(car_mileage)
    columns.append(car_wheel)
    columns.append(car_optional)
    columns.append(adv_city)
    columns.append(adv_id)
    columns.append(adv_date)

    result = u""
    for i in columns:
        result += i + delimiter

    return result + "\n"


if  __name__ ==  "__main__":
    extension = ".html"
    filesList = [fileName for fileName in os.listdir(html_directory) if fileName.lower().endswith(extension)]

    counter = 0;
    for fileName in filesList:
        print "Processing ", fileName
        ad = parse_file(os.path.join(html_directory, fileName))
        data += ad
        counter += 1

    write_file(data.encode("utf-8"))
    print "Total ", counter, " ads processed."
