
![enter image description here](https://www.selenium.dev/images/selenium_logo_large.png)
> **Seleniuma yeni başlayan yada türkçeleştirilmiş modül kullanmak isteyenler için kendi yaptığım işlevli bir modül.(henüz pypi de yok indirip import etmelisiniz)**

## Dökümenasyon
Öncelikle scripti `import basicselenium as <ad>` olarak import ettikten **operasyon** öğesinden miras almanız gerekiyor çünkü scriptin içindeki olaylar operasyon adındaki classtan ilerliyor

**Örnek Olarak**

    import basicselenium as bs
    örnekmiras = bs.operasyon()

**Şimdi örnek miras ile yapılabileceklere gelelim**

> başlat() fonksiyonundan önce ayarlayabileceğiniz 3 adet parametre var.
>> **gizlisekme**(boolean,false) = tarayıcının gizli sekme olup olmadığını ayarlar
>> **görünmez**(boolean,false) = tarayıcının görünmez olup olmadığını ayarlar
> > **driveryolu**(string,null) = chromedriver yolunu tarif eder. eğer driver path ta varsa boş bırakın yoksa ayrıca belirtin
> 
> başlat() fonksiyonundan sonra kullanabileceğiniz fonksiyonlar 
> ise şunlar.
> > git(url)  url ye götürür
> > başlıkal() = sitenin başlığını döndürür
> > gerigit() bir önceki sayfaya gider
> > sayfayıyenile() sayfayı yeniler
> > sekmeyikapat() sekmeyi kapatır
> > tarayıcıyıkapat() tarayıcıyı kapatır
> > tamekranyap() siteyi tam ekran yapar
> > ssal("dosyayolu") sayfayı ss alır
> >kaynakkodual() sayfanın kaynak kodunu geri döndürür

Bunların dışında locator yani konumlandırıcı komutlarda var

>> 1 adet element döndürenler elementbul_
>> çoklu element döndürenler elementleribul_

döndürme tiplerine göre

> id
> class
> xpath
> cssselector
> name
> tagname
> linktext
> partiallinktext

Örnek olarak

    örnekmiras.elementbul_tagname("br")

Tabi bunlara normal seleniumda olan .click() ve .sendkeys("") gibi komutlar gönderilebilir.
