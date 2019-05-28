import aiohttp
import asyncio
from bs4 import BeautifulSoup
async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
            
        return await res.text()
    
async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await get_html(session, url)
        soup = BeautifulSoup(html,'html.parser')
        #extracts number of questions for a package in stackoverflow
        items = soup.find('div', attrs={'class':'_3XNzf flex flex-row-reverse items-end'}).find('p').text
        items = (items.replace('\n','')).strip()
        items = (items.replace('questions','')).strip()
        url = url.replace('https://stackoverflow.com/questions/tagged/','')
        #writes the questions to a file
        with open('questions.txt', 'a') as the_file:
             the_file.write(url)
             the_file.write(' ')
             the_file.write(items)
             the_file.write('\n')
             print('done questions',url)
                
                
    
            
#---------------Control enters here           
urls=[]

#generates links for the following names and add them to urls list
l=["ember-cli-rework","ember-currency","ember-data-faker-adapter","ember-dev-fixtures","ember-file-drop"] 
for i in l:
    urls.append(f'https://www.npmjs.com/package/{i}')

#runs program for those links
loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.gather(*(main(url) for url in urls))
)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())