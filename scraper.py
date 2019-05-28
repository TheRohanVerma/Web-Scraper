# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:42:29 2019

@author: ROHAN
"""

import aiohttp
import asyncio
from bs4 import BeautifulSoup


#Following code is called by the syntax written below
async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
        return await res.text()
    
async def main(url):
    async with aiohttp.ClientSession() as session:
        #following will be the code with beautiful soup for specific element data extraction
        html = await get_html(session, url)
        soup = BeautifulSoup(html,'html.parser')
        #write soup.find etc methods to extract data
                
                
    
            
#---------------Control enters here ------------------     
#Enter the links in urls list
urls=[]
        
#runs asynchronous loop for urls in the list urls
loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(*(main(url) for url in urls))
)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())