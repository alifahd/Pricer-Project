import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
import requests
from bs4 import BeautifulSoup

items = {}
count = 0

class AddScreen(Screen):
    itemURL = ObjectProperty(None)

    def scrape(self):
        global count
        response = requests.get(self.itemURL.text)

        soup = BeautifulSoup(response.text, 'html.parser')

        price = soup.find(class_='price_FHDfG large_3aP7Z')
        title = soup.find(class_='productName_19xJx')
        modnum = soup.find(itemprop='model')
        webcode = soup.find(itemprop='sku')

        if (price == None):
            price = soup.find(class_='price_FHDfG large_3aP7Z salePrice_kTFZ3').get_text()
        else:
            price = price.getText();

        title = title.getText();
        modnum = modnum.getText();
        webcode = webcode.getText();

        items[count] = {0: title, 1: price, 2: modnum, 3: webcode}
        print (items)
        count += 1
        self.reset()

    def reset(self):
        self.itemURL.text = ""

class HomeScreen(Screen):
    def printer(self, *kwargs):
        self.ids.numItems.rows = len(items)
        for x in items:
            self.ids.itemTitles.text = str(items[x][0])
            self.ids.itemInfo.text = "Price: " + str(items[x][1]) + "   Model Number: " + str(items[x][2]) + "  Web Code: " + str(items[x][3])

class ConfirmScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("pricer.kv")

class PricerApp(App):
    def build(self):
        return kv

PricerApp().run()

#python main.py
#kivy_venv\Scripts\activate
