import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import csv
import re
import os


paginas_comestibles=['https://listado.mercadolibre.com.ar/supermercado/almacen/#origin=supermarket_navigation&from=search-frontend'
                     ]
                   
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'} 

registro={}
listado=[]

for page in paginas_comestibles:
    url = requests.get(page, headers=headers)
    soup = BeautifulSoup(url.text, "html.parser")
    
    resultados = soup.find_all('div',{"class":"rowItem item highlighted item--grid new"})
    
    for producto in resultados:
            fecha = str(date.today())                 
            descripcion=producto.h2.text                       
            precio=producto.find('span',{"class":"price__fraction"}).text           
            descuento=producto.find('div',{"class":"item__discount"})
            registro={'Fecha':fecha, 'Descripcion':descripcion, 'Precio':precio,'Descuento':descuento}
            listado.append(registro)

df=pd.DataFrame(listado)
fecha_creacion= str(date.today()) 
df.to_csv((os.path.join(path, str(fecha_creacion)+'.csv', index=False, encoding='iso-8859-1')))
#df.to_excel(str(fecha_creacion)+'.xlsx')
print("Se generó un archivo csv con la sig informacion: ")
print(df.info())