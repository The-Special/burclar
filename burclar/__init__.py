import requests
from bs4 import BeautifulSoup

"""
Bu modül burçlar ile ilgilenen arkadaşlarımın işine yarayacaktır.
Çok basit bir kullanımı mevcuttur.
Bir sorunuz olursa seve seve yardım etmek isterim profilimdeki linklerden bana ulaşabilirsiniz.

"""

def makeAPIRequest(path: str, type: str) -> str:
    type = type if (type == "gunluk") or (type == "haftalik") else "gunluk"
    r = requests.get(f"https://www.mynet.com/kadin/burclar-astroloji/{path}-burcu-{type}-yorumu.html")
    soup = BeautifulSoup(r.content , "html.parser")
    data = soup.find_all("div" , {"class":"detail-content-inner"})
    burc = (data[0].contents) [len(data[0].contents) -6]
    burcYorum = burc.text
    return burcYorum 


burcList = [ "yengec", "koc", "boga", "ikizler", "aslan", "basak", "terazi", "akrep", "yay", "oglak", "kova", "balik" ]
burcStr = ",".join(burcList)

class burclar:
    def burc(name: str, type = "gunluk") -> str:
        if name not in burcList:
            raise Exception(f"Geçerli bir burç giriniz. ({burcStr})")
        return makeAPIRequest(name, type)

    def yengec(type = "gunluk") -> str:
        return makeAPIRequest("yengec", type)

    def koc(type = "gunluk") -> str:
        return makeAPIRequest("koc", type)

    def boga(type = "gunluk") -> str:
        return makeAPIRequest("boga", type)

    def ikizler(type = "gunluk") -> str:
        return makeAPIRequest("ikizler", type)

    def aslan(type = "gunluk") -> str:
        return makeAPIRequest("aslan", type)

    def basak(type = "gunluk") -> str:
        return makeAPIRequest("basak", type)

    def terazi(type = "gunluk") -> str:
        return makeAPIRequest("terazi", type)

    def akrep(type = "gunluk") -> str:
        return makeAPIRequest("akrep", type)

    def yay(type = "gunluk") -> str:
        return makeAPIRequest("yay", type)

    def oglak(type = "gunluk") -> str:
        return makeAPIRequest("oglak", type)

    def kova(type = "gunluk") -> str:
        return makeAPIRequest("kova", type)

    def balik(type = "gunluk") -> str:
        return makeAPIRequest("balik", type)
    
def makeAPIRequestOz(path: str , type: str) -> str:
    type = type if (type == "ozellikleri") else "ozellikleri"
    y = requests.get(f"https://www.mynet.com/kadin/burclar-astroloji/{path}-burcu-ozellikleri.html")
    soupOz = BeautifulSoup(y.content , "html.parser")
    dataOz = soupOz.find_all("div" , {"class":"medyanet-content"})
    burcOz = (dataOz[0].contents) [len(dataOz[0].contents) -12]
    burcYorumOz = burcOz.text
    return burcYorumOz


class burclar_oz:
    def burcOz(name: str, type = "ozellikleri") -> str:
        if name not in burcList:
            raise Exception(f"Geçerli bir burç giriniz. ({burcStr})")
        return makeAPIRequestOz(name, type)

    def yengecOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("yengec", type)

    def kocOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("koc", type)

    def bogaOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("boga", type)

    def ikizlerOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("ikizler", type)

    def aslanOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("aslan", type)

    def basakOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("basak", type)

    def teraziOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("terazi", type)

    def akrepOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("akrep", type)

    def yayOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("yay", type)

    def oglakOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("oglak", type)

    def kovaOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("kova", type)

    def balikOz(type = "ozellikleri") -> str:
        return makeAPIRequestOz("balik", type)









