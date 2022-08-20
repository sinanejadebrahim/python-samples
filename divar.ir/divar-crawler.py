import requests 
from bs4 import BeautifulSoup as bs
import re 

# divar.ir website crawler based on price - output contains (car name - price - usage - direct link to product)


def ml_data():
    # format data for ML operations 
    with open (f"{price}-tomani-cars.txt", "r") as f:
        # for somereason none of the right ways for this works(re.sub - str replace - etc...)
        # so i had to do it one by one 
        s = f.read()
        s = s.replace('۰', '0')
        s = s.replace('۱', '1')
        s = s.replace('۲','2')
        s = s.replace('۳','3')
        s = s.replace('۴','4')
        s = s.replace('۵','5')
        s = s.replace('۶','6')
        s = s.replace('۷','7')
        s = s.replace('۸','8')
        s = s.replace('۹','9')
        s = s.replace(',', '')
        print(s)
    
    
def search_by_price(price):
    
    req = requests.get(f'https://divar.ir/s/tehran/car?price={price}')
    
    soup = bs(req.text, 'html.parser')
    
    # get all needed elemetns (name - price - usage - etc...)
    full_result = soup.find_all('div', attrs={'class': 'kt-post-card__body'})
    names = soup.find_all('h2', attrs={'class': 'kt-post-card__title'})
    desc = soup.find_all('div', attrs={'class': 'kt-post-card__description'})
    links = soup.find_all('div', attrs={'class': 'waf972 wbee95 we9d46'})
    
    # add all URLs to our list 
    link = []    
    for each in links:
        temp_link = each.find_all('a')
        main_link = re.findall(r'href=\"(.*?)\"',str(temp_link))
        link += main_link
    
    
    # write our result to a file 
    with open (f"{price}-tomani-cars.txt", "w") as f:
        
        for i in range(len(full_result)):
            f.write(f'{names[i].text}\n')
            f.write(f'{desc[i].text}\n')
            f.write(f'{desc[i+1].text}\n')
            f.write(f'https://divar.ir{link[i]}\n')
            f.write('\n')
            
    
    ml_data()


def start_crawling():
    print('''
    input help:
        200000000
        # shows cars under 200,000,000
        200000000-500000000
        # shows cars between 200,000,000 and 500,000,000

        ''')
    user_input = input('Enter your price range: ')

    # checking to get currect input from user
    
    global price 
    try:
        min,max = user_input.split('-')
        if min and max:
            price = f"{min}-{max}"
    except ValueError as error:
        price = f"-{user_input}"
    
    search_by_price(f"{price}")

    
start_crawling()


