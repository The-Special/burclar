import requests
from bs4 import BeautifulSoup

class burclar:
    def yengec():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/yengec-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def koc():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/koc-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def boga():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/boga-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def ikizler():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/ikizler-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def aslan():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/aslan-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def basak():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/basak-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def terazi():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/terazi-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def akrep():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/akrep-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def yay():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/yay-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def oglak():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/oglak-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def kova():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/kova-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def balık():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/balik-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

















    
    
