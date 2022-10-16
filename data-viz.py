import pandas as pd
import statistics
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

def stats(ds):
  print(f"\nAverage CO2 per capita emission (metric tonnes): {ds.mean()}\n")
  print(f"Median CO2 per capita emission (metric tonnes): {ds.median()}\n")
  print(f"Standard Deviation of CO2 per capita emission (metric tonnes): {ds.std()}\n")
  print(f"Variance of CO2 per capita emission (metric tonnes): {(ds.std())**2}\n")
  
def co2vsgdp(df):
  xdata = df['Year']
  ydata1 = df['CO2']
  ydata2 = df['GDP']

  plt.figure(num = 3, figsize=(9, 5))
  plt.plot(xdata, ydata2)
  plt.plot(xdata, ydata1, 
           color='red',   
           linewidth=1.0,  
           linestyle='-.' 
          )
  plt.title("Per Capita CO2 Emission V/S Per Capita GDP (India)")
  plt.xlabel("P.C. CO2 emission and P.C. Indian GDP")
  plt.ylabel("Year")
  plt.legend(['Per Capita GDP', 'Per Capita CO2 Emission'])
  plt.show()
  
def ga_indvsworld():
  file = "world CO2 emission.csv"
  df3 = pd.read_csv(file)

  indiadata = df3.loc[71]
  indiadata = list(map(lambda x : x/max(indiadata[1:]) if x > 0 else x, indiadata[1:]))

  worlddata = df3.loc[177]
  worlddata = list(map(lambda x : x/max(worlddata[1:]) if x > 0 else x, worlddata[1:]))

  years = list(df3.columns[1:])
  years = list(map(lambda x : int(x) if x.isdigit() else x, years))

  plt.figure(num = 3, figsize=(12, 7))
  plt.plot(years,indiadata)
  plt.plot(years,worlddata,
           color='red',   
           linewidth=1.0,  
           linestyle='-.')

  plt.ticklabel_format(style="plain")
  plt.title("Growth analysis of CO2 Emissions by India and World")
  plt.ylabel("<--- CO2 Emissions India vs CO2 Emissions India --->")
  plt.xlabel("<--- Year --->")
  plt.legend(['CO2 Emissions : India', 'CO2 Emissions : World'])
  plt.show()
  
def ga_top5vsworld():
  file = "world CO2 emission.csv"
  df3 = pd.read_csv(file)

  chinadata = df3.loc[29]
  chinadata = list(map(lambda x : x/max(chinadata[1:]) if x > 0 else x, chinadata[1:]))

  usadata = df3.loc[168]
  usadata = list(map(lambda x : x/max(usadata[1:]) if x > 0 else x, usadata[1:]))

  indiadata = df3.loc[71]
  indiadata = list(map(lambda x : x/max(indiadata[1:]) if x > 0 else x, indiadata[1:]))

  russiadata = df3.loc[128]
  russiadata = list(map(lambda x : x/max(russiadata[1:]) if x > 0 else x, russiadata[1:]))

  japandata = df3.loc[79]
  japandata = list(map(lambda x : x/max(japandata[1:]) if x > 0 else x, japandata[1:]))

  worlddata = df3.loc[177]
  worlddata = list(map(lambda x : x/max(worlddata[1:]) if x > 0 else x, worlddata[1:]))

  years = list(df3.columns[1:])
  years = list(map(lambda x : int(x) if x.isdigit() else x, years))

  plt.figure(num = 3, figsize=(13, 6))
  plt.subplot(2, 3, 1)
  plt.plot(years,chinadata,color='red',linewidth = 1.0)
  plt.fill_between(years, chinadata, color='red')
  plt.legend(["China"])
  plt.subplot(2, 3, 2)
  plt.plot(years,usadata,color='blue',linewidth = 1.0)
  plt.fill_between(years, usadata, color='blue')
  plt.legend(["USA"])
  plt.subplot(2, 3, 3)
  plt.plot(years,indiadata,color='green',linewidth = 1.0)
  plt.fill_between(years, indiadata, color='green')
  plt.legend(["India"])
  plt.subplot(2, 3, 4)
  plt.plot(years,russiadata,color='black',linewidth = 1.0)
  plt.fill_between(years, russiadata, color='black')
  plt.legend(["Russia"])
  plt.subplot(2, 3, 5)
  plt.plot(years,japandata,color='orange',linewidth = 1.0)
  plt.fill_between(years, japandata, color='orange')
  plt.legend(["Japan"])
  plt.subplot(2, 3, 6)
  plt.plot(years,worlddata,color='pink',linewidth = 1.0)
  plt.fill_between(years, worlddata, color='pink')
  plt.legend(["World"])

  plt.suptitle("Growth analysis of CO2 Emissions by top 5 CO2 Emitting countries and the World")
  plt.show()

def co2_top5():
  file = "world CO2 emission.csv"
  df3 = pd.read_csv(file)

  chinadata = df3.loc[29]

  usadata = df3.loc[168]

  indiadata = df3.loc[71]

  russiadata = df3.loc[128]

  japandata = df3.loc[79]

  plt.figure(num = 2, figsize=(10, 4))

  dataf = [chinadata[1],usadata[1],indiadata[1],russiadata[1],japandata[1]]
  datal = [chinadata[-1],usadata[-1],indiadata[-1],russiadata[-1],japandata[-1]]
  country = ['China','USA','India','Russia','Japan']

  explode = (0, 0, 0.1, 0,0)
  plt.suptitle("CO2 Emission of top 5 countries (1981 vs 2020)")
  plt.subplot(1, 2, 1)
  plt.pie(dataf, labels = country,autopct='%.1f%%',shadow=True,explode=explode)
  plt.subplot(1, 2, 2)
  plt.pie(datal, labels = country,autopct='%.1f%%',shadow=True,explode=explode)

  plt.show()

  
  
  
file = 'Per-capita co2-gdp data.csv'
df = pd.read_csv(file)


ds = df["CO2"]

stats(ds)
co2vsgdp(df)
ga_indvsworld()
ga_top5vsworld()
co2_top5()
