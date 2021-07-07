import pandas

census_data = pandas.read_csv("census.csv")

mean = census_data[census_data.columns[0]].mean()
median = census_data[census_data.columns[0]].mean()
max = census_data[census_data.columns[0]].max()

print("Mean: {}" .format(mean))
print("Medain: {}" .format(median))
print("Max: {}" .format(max))
