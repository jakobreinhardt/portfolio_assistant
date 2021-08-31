import pandas as pd
import matplotlib.pyplot as plt
from yahoofinancials import YahooFinancials


# Load my portfolio
df = pd.read_csv("Depotbewertung_8004165926_20210526.csv", delimiter=';',  skiprows=5, encoding= 'unicode_escape')
#thousands='.', 
# Letzte Zeile löschen 
df.drop(index=df.index[-1], axis=0, inplace=True)

#df nach Kurswert sortieren
df.sort_values("Kurswert")

#Plot
plt.scatter(df["Wertpapiername"], df["Kurswert"])
plt.show()



df['Kurswert'].str.replace('\.','').astype(float)

#Problem die Weter in bspw. Kurswert sind string nicht float