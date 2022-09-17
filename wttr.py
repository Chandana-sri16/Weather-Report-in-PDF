from fpdf import FPDF
import os
import requests

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=12)
citydata = input('Enter city name: ')
print(citydata)
url = 'https://wttr.in/{}?format\n"Location:%l\nWeather condition:%c\nTemperature:%t\nMoon phase:%m\nWeather:%C\n' \
      'Humidity:%h\nTemp feels like:%h\nWind:%w\nMoon day:%M\nPrecipitation:%p\nPressure:P\nUV index:%u"'.format(citydata)
res = requests.get(url)
print(res.text)

pdf.cell(200, 8, txt='weather report', ln=1, align='L')

pdf.output("weather8.pdf")
os.system("weather8.pdf")
