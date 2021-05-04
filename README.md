# Web-Scraper
Asynchronous Web Scraper to get data from hundreds of websites simultaneously.
# Detailed Description  
This python asynchronous requests hundreds of webpages simultaneously and then uses beautiful soup to get that from the web pages. The number of webpages simultaneously is limited by the number of requests the server can handle.
The server might temporarily block your ip address because large number of requests, then you reduce the number of web pages you fetch data from.
Documentation has been done and an additional example.py has been provided for better understanding.
# Scraper.py
This is the main scraper file, you can add you beautiful soup code in this and run in directly
# Example.py
This is an example file which gets the number of questions for a NPM package and then writes them to a file.
---Warning---
This program might show looping running warning. You can ignore it and rerun the program once it has scraped desired data from all the input links.
