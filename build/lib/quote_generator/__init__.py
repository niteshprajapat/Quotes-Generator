# MODULES

import requests
from bs4 import BeautifulSoup



headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}


# IMPLEMENTS

def motivational_quotes():
    try:
        url = "https://www.briantracy.com/blog/personal-success/26-motivational-quotes-for-success/"
        page = requests.get(url , headers = headers)
        soup = BeautifulSoup(page.content , "html.parser")
        quotes = soup.find_all("h3")


        for i in quotes:
            # print(i.get_text())
            data = i.get_text()
            print(data)
            
        

    except Exception as e:
        print(f"you are having an error like :- {e}")





def albert_einstein_quotes():
    try:
        url = "https://www.goalcast.com/2017/03/29/top-30-most-inspiring-albert-einstein-quotes/"
        page = requests.get(url , headers = headers)
        soup = BeautifulSoup(page.content , "html.parser")
        data = soup.find_all(class_="td_pull_quote td_pull_center")
        for i in data:
            quote = i.find("p").get_text()
            print(f"\n{quote}")
 
    
    except Exception as e:
        print(f"you are having an error like :- {e}")





def mahatma_gandhi_quotes():
    try:
        url = "https://www.goalcast.com/2017/03/20/top-20-inspiring-mahatma-gandhi-quotes/"
        page = requests.get(url , headers = headers)
        soup = BeautifulSoup(page.content , "html.parser")
        data = soup.find_all(class_="td_pull_quote td_pull_center")
        for i in data:
            quote = i.find("p").get_text()
            print(f"\n{quote}")
 
    
    except Exception as e:
        print(f"you are having an error like :- {e}")





def steve_jobs_quotes():
    try:
        url = "https://www.goalcast.com/2016/07/22/top-12-most-inspiring-steve-jobs-quotes/"
        page = requests.get(url , headers = headers)
        soup = BeautifulSoup(page.content , "html.parser")
        data = soup.find_all(class_="td_pull_quote td_pull_center")
        for i in data:
            quote = i.find("p").get_text()
            print(f"\n{quote}")
 
    
    except Exception as e:
        print(f"you are having an error like :- {e}")





def bill_gates_quotes():
    try:
        url = "https://www.goalcast.com/2017/12/07/27-bill-gates-quotes/"
        page = requests.get(url , headers = headers)
        soup = BeautifulSoup(page.content , "html.parser")
        data = soup.find_all(class_="td_pull_quote td_pull_center")
        for i in data:
            quote = i.find("p").get_text()
            print(f"\n{quote}")
 
    
    except Exception as e:
        print(f"you are having an error like :- {e}")





def elon_musk_quotes():
    try:
        url = "https://www.goalcast.com/2018/01/31/top-11-best-elon-musk-quotes/"
        page = requests.get(url , headers = headers)
        soup = BeautifulSoup(page.content , "html.parser")
        data = soup.find_all(class_="td_pull_quote td_pull_center")
        for i in data:
            quote = i.find("p").get_text()
            print(f"\n{quote}")
 
    
    except Exception as e:
        print(f"you are having an error like :- {e}")

def mark_zuckerberg_quotes():
    try:
        url = "https://www.inc.com/peter-economy/mark-zuckerberg-19-inspiring-power-quotes-for-success.html"
        page = requests.get(url , headers = headers)
        soup = BeautifulSoup(page.content , "html.parser")
        data = soup.find_all(class_="standardText")
        for i in data:
            quote = i.find("p").get_text()
            print(f"\n{quote}")
 
    
    except Exception as e:
        print(f"you are having an error like :- {e}")
