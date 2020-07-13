from selenium import webdriver
class operasyon:
    gizlisekme = False
    görünmez = False
    driveryolu = ""
    chrome = ""
    def başlat(self):
        opsiyonlar = webdriver.ChromeOptions()
        if(self.görünmez):
            opsiyonlar.add_argument("--headless")
        if (self.gizlisekme):
            opsiyonlar.add_argument("--incognito")
        if(self.driveryolu != ""):
            self.chrome = webdriver.Chrome(options=opsiyonlar, executable_path=self.driveryolu)
        else:
            self.chrome = webdriver.Chrome(options=opsiyonlar)

    def git(self,url):
        self.chrome.get(url)
    def başlıkal(self):
        return self.chrome.title
    def gerigit(self):
        self.chrome.back()
    def sayfayıyenile(self):
        self.chrome.refresh()
    def sekmeyikapat(self):
        self.chrome.close()
    def tarayıcıyıkapat(self):
        self.chrome.quit()
    def tamekranyap(self):
        self.chrome.maximize_window()
    def pencereboyutuayarla(self,yükseklik,genişlik):
        self.chrome.set_window_size(yükseklik,genişlik)
    def ssal(self,dosyayolu):
        self.chrome.save_screenshot(dosyayolu)
    def kaynakkodual(self):
        return self.chrome.page_source
    def elementbul_id(self,id):
        return self.chrome.find_element_by_id(id)
    def elementbul_class(self, classadı):
        return self.chrome.find_element_by_class_name(classadı)
    def elementleribul_class(self, classadı):
        return self.chrome.find_elements_by_class_name(classadı)
    def elementbul_xpath(self, xpath):
        return self.chrome.find_element_by_xpath(xpath)
    def elementleribul_xpath(self, xpath):
        return self.chrome.find_elements_by_xpath(xpath)
    def elementbul_cssselector(self,selector):
        return self.chrome.find_element_by_css_selector(selector)
    def elementleribul_cssselector(self,selector):
        return self.chrome.find_elements_by_css_selector(selector)
    def elementbul_name(self, name):
        return self.chrome.find_element_by_name(name)
    def elementleribul_name(self, name):
        return self.chrome.find_elements_by_name(name)
    def elementbul_tagname(self, tagname):
        return self.chrome.find_element_by_tag_name(tagname)
    def elementleribul_tagname(self, tagname):
        return self.chrome.find_elements_by_tag_name(tagname)
    def elementbul_linktext(self, linktext):
        return self.chrome.find_element_by_link_text(linktext)
    def elementleribul_linktext(self, linktext):
        return self.chrome.find_elements_by_link_text(linktext)
    def elementbul_partiallinktext(self, linktext):
        return self.chrome.find_element_by_partial_link_text(linktext)
    def elementleribul_partiallinktext(self, linktext):
        return self.chrome.find_elements_by_partial_link_text(linktext)




