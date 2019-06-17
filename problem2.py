#!/usr/bin/python3

from googlesearch import search

URL= []

f= open("search history.txt","w+")

request=input("enter your search:")

print("searched URL are:")

for j in search(request, tld="com", num=1, start=0, stop= 10, pause=0):  

	URL.append(j)

	f.write(j)

	print(j)

f.close()

print("Searched URL are:",URL)

