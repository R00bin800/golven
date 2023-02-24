import random
import pandas as pd
import os

waves = []
period = []

amount = 1000 #ammount of waves to generate

min_height = 5
max_height = 20

min_period = 5
max_period = 36

for i in range(amount):
    waves.append(random.randint(min_height,max_height))
    period.append(random.randint(min_period,max_period))

df = pd.DataFrame(list(zip(waves,period)),columns = ["golfhoogte", "golfperiode"]).transpose()
df = df[df.columns[0:]].apply(lambda x: ', '.join(x.dropna().astype(str)),axis=1)
df.to_excel("wavetestdata.xlsx", index=False, header=False)
