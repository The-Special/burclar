[![Version](https://badge.fury.io/py/burclar.svg)](https://pypi.python.org/pypi/burclar)
[![Downloads](https://img.shields.io/pypi/dm/burclar.svg)](https://pypi.python.org/pypi/burclar)
![Stars](https://img.shields.io/github/stars/The-Special/burclar)
![Commits](https://img.shields.io/github/commit-activity/w/The-Special/burclar)

Bu modulu burclar hakkinda gundelik bir sekilde bilgi alin diye yaptim ve sizler icin kullanima sunuyorum.
Modulun kullanimi asiri basit:


```
Ornek Kullanim V1:

from burclar import burclar

yay = burclar.yay('gunluk') & burclar.yay() #Buraya yay yerine burclarin adini yazarak istediginiz gundelik burc bilgisini alabilirsiniz.

yay = burclar.yay('haftalik') #Buraya yay yerine burclarin adini yazarak istediginiz haftalik burc bilgisini alabilirsiniz.


print(yay) # Konsola yorumun ciktisini verir.

"""
Gundelik olarak her gun kendini duzenler ve sadece burc yorum kismini size verir.

"""
```
```
Ornek Kullanim V2:

from burclar import burclarOz 

yay = burclarOz.yay() & burclarOz.yay('ozellikleri') #Buraya yay yerine burclarin adini yazarak istediginiz burcun ozellik bilgisini alabilirsiniz.

print(yay)
```

Bunun haricinde bir kullanimi yoktur. yay yazan yerlere farkli burclari yazarak bilgiler alabilirsiniz.

Burclar:

-terazi
-boga
-yay
-akrep
-kova
-aslan
-ikizler
-balik 
-koc
-yengec
-basak
-oglak

Modulu kullandiginiz icin tesekkur ederim , en kisa zamanda daha gelismisini sizlerin huzuruna sunacagim.
