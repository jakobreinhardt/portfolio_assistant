import pandas as pd


# Load my portfolio
df = pd.read_csv("Depot.csv", delimiter=';',  skiprows=0, encoding= 'unicode_escape')
#thousands='.', 
# Letzte Zeile löschen 
df.drop(index=df.index[-1], axis=0, inplace=True)

#df nach Kurswert sortieren
#df.sort_values("Kurswert")

#Plot
#plt.scatter(df["Wertpapiername"], df["Kurswert"])
#plt.show()


#df['Kurswert'].str.replace('\.','').astype(float)

#Problem die Werte in bspw. Kurswert sind string nicht float