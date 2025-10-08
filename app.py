#scraps data from amazon website

#beautifulSoup4
#lxml
#requests

from bs4 import BeautifulSoup
import requests
import csv 

url = "https://www.amazon.in/Apple-Headphones-Cancellation-Transparency-Personalised/dp/B0DGJB8CW4/ref=sr_1_4?crid=3CI48EUYUX5K9&dib=eyJ2IjoiMSJ9.y08pMqaeTlUXGU64oyMGl8EvkLP-ctao4odnzlJbDvxyJQhiy-WZ_7832ETM7QPjcDDiBsj7kqxrvdgoyXnLqUT7NJb_27pKTiX_aLpslJSZGQxwZQRoqCUX6ACgPayBEJqMwQs--S42XVUThjVZRAgCuo8-yPy4zF7-Z-ZC7_1k-EXBP-S-xKL0wnW9_ooK-TEORnUCPNaFcDd1Sib7ElEbAsQgfnfURER0QYJCuRc.NDVlp7aTkHdT2tJD9gNYuT2q8zpgtYaLQUyeKsAePMA&dib_tag=se&keywords=apple%2Bairpods%2Bpro%2Bmax&nsdOptOutParam=true&qid=1759920185&sprefix=apple%2Bairpods%2Bpromax%2Caps%2C382&sr=8-4&th=1"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"} 

response = requests.get (url, headers=headers)

if response.status_code ==200:
    #print(response.status_code)
    html_content = response.text

else:
    print("fetching error", response.status_code)

#print(html_content)

soup = BeautifulSoup(html_content, 'lxml')

#print (soup.prettify())

product_title = soup.find("span", id="productTitle").text.strip()
product_price = soup.find("span", class_="a-price-whole").text.strip()
product_rating = soup.find ("span", id="acrPopover").text.strip()
product_info = soup.find ("ul", class_="a-unordered-list a-vertical a-spacing-mini").text.strip()
product_description = soup.find ("div", id="productDescription").text.strip()
reviews = soup.find ("ul", id="cm-cr-dp-review-list").text.strip()


#print(product_title)
#print(product_price)
#print(product_rating)
#print(product_info)
#print(product_description)
#print(reviews)

#find, find_all 

#saving the data

with open("amazon_airpod pro max.csv", mode= 'w', newline ='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["product_title", "product_price", "product_rating", "product_info","product_description", "reviews"])

    writer.writerow([product_title, product_price, product_rating, product_info, product_description, reviews])

print("data saved")