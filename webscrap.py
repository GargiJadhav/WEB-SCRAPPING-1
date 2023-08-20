import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

data = requests.get(START_URL)
soup = BeautifulSoup(data.text , 'html.parser')

starsData=[]

for tr in soup.find("table").find_all("tr"):
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td]
    starsData.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(starsData)):
    name.append(starsData[i][1])
    distance.append(starsData[i][3])
    mass.append(starsData[i][5])
    radius.append(starsData[i][6])
    print(name)

df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
)
df.to_csv("data.csv")
    