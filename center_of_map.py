import pandas
df=pandas.read_csv("Volcanoes-USA.txt")
print("Mean Elevation ",df["ELEV"].mean())
print("Mean Latitude ",df["LAT"].mean())
print("Min Elevation ", min(df["ELEV"]))
