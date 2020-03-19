from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

precios = pd.DataFrame(columns=('Potencia','Precio'))

driver = webdriver.Chrome()
page = driver.get('http://www.macrosolar.cl/productos/index.php?g=67')
vector = []
pot=""
val=""
df = pd.read_html(driver.page_source)[7]
for index, row in df.iterrows():
    for element in row:
        if(isinstance(element, str)):
            aux = element.split()
            for word in aux:
                if ("W" in word):
                    pot=word.replace('W','')
                elif ("$" in word):
                    val=word.replace('$','')
        if(len(pot)>0 and len(val)>0):
            vector.append([float(pot),float(val)])
            pot=""
            val=""
precios = pd.DataFrame(vector, columns=['Potencia [W]','Precio [clp]'])
precios['ratio [clp/W]'] = precios.apply(lambda row: row[1]*1000/row[0], axis=1)
precios = precios.sort_values(by=['ratio [clp/W]'])
print(precios)
