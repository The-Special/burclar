import requests
from bs4 import BeautifulSoup
"""
Bu modül burçlar ile ilgilenen arkadaşlarımın işine yarayacaktır.
Çok basit bir kullanımı mevcuttur.
Bir sorunuz olursa seve seve yardım etmek isterim profilimdeki linklerden bana ulaşabilirsiniz.

"""
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

    def balik():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/balik-burcu-gunluk-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def yengecHaftalik():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/yengec-burcu-haftalik-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def kocHaftalik():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/koc-burcu-haftalik-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum
    
    def bogaHaftalik():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/boga-burcu-haftalik-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum
    
    def ikizlerHaftalik():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/ikizler-burcu-haftalik-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def aslanHaftalik():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/aslan-burcu-haftalik-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def basakHaftalik():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/basak-burcu-haftalik-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def teraziHaftalik():
        r = requests.get("https://www.mynet.com/kadin/burclar-astroloji/terazi-burcu-haftalik-yorumu.html")
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def akrepHaftalik():
        r = requests.get('https://www.mynet.com/kadin/burclar-astroloji/akrep-burcu-haftalik-yorumu.html')
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum
    
    def yayHaftalik():
        r = requests.get('https://www.mynet.com/kadin/burclar-astroloji/yay-burcu-haftalik-yorumu.html')
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def oglakHaftalik():
        r = requests.get('https://www.mynet.com/kadin/burclar-astroloji/oglak-burcu-haftalik-yorumu.html')
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def kovaHaftalik():
        r = requests.get('https://www.mynet.com/kadin/burclar-astroloji/kova-burcu-haftalik-yorumu.html')
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum

    def balikHaftalik():
        r = requests.get('https://www.mynet.com/kadin/burclar-astroloji/balik-burcu-haftalik-yorumu.html')
        soup = BeautifulSoup(r.content , "html.parser")
        data = soup.find_all("div" , {"class":"detail-content-inner"})
        burc = (data[0].contents) [len(data[0].contents) -6]
        burcYorum = burc.text
        return burcYorum
