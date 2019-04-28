#!/usr/bin/python3
# _*_coding: UTF-8 _*_
import requests
from bs4 import BeautifulSoup
import csv
def get_data(url):
	res=requests.get(url)
	res.encoding='utf-8'
	soup=BeautifulSoup(res.text,'html.parser')
	for pnews in soup.select('.item'):
	    for acontent in pnews.select('a'):
	        text=acontent.text
	        h=acontent['href']
	        print(text,h)
	        writer.writerow([text,h])
if __name__=='__main__':
	with open('E:/Download/nba.csv','w',newline='',encoding='utf-8-sig') as csvfile:
		writer=csv.writer(csvfile)
		writer.writerow(['titel','url'])
		get_data('http://sports.sina.com.cn/nba/')



https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&versionNumber=1.2.4&page=1&encode=utf-8&callback=feedCardJsonpCallback&_=1554027767928