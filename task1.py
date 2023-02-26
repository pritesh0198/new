from bs4 import BeautifulSoup
import requests
import csv
url="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
HEADERS = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'}
webpage = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "html.parser")
k=soup.find_all("div",attrs={"data-component-type": "s-search-result"})

filename = "task1.csv"
fields = ['link', 'title', 'price', 'review','rating']
rows=[]

for item in k:
	print("https://www.amazon.in" + ((item.find_all("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"))[0]).get("href"))
	print(((item.find_all("span", class_="a-size-medium a-color-base a-text-normal"))[0]).get_text())
	link=("https://www.amazon.in" + ((item.find_all("a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"))[0]).get("href"))
	title=((item.find_all("span", class_="a-size-medium a-color-base a-text-normal"))[0]).get_text()
	try:
		price=((item.find("span", class_="a-price-whole"))).get_text()
		print(price)
	except:
		price="Not Avliable"
		print(price)
	try:
		review=(item.find("span", class_="a-size-base s-underline-text")).get_text()
		print(review)
	except:
		review="Not Avliable"
		print(review)
	try:
		rating=((item.find("span", class_="a-icon-alt"))).get_text()
		print(rating)
	except:
		rating="Not Avliable"
		print(rating)

	a=[link,title,price,review,rating]
	rows.append(a)

with open(filename, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(fields)
	csvwriter.writerows(rows)
	print("We have written in csv")
