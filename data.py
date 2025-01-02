import pandas as pd
#Load datasets
#Filtered from World Bank Group Datasets, only from years 2000-2024
gdp = pd.read_csv(r"g:\Economic Indicators\gdp_2000_2024.csv")
cpi = pd.read_csv(r"g:\Economic Indicators\inflation_2000_2024.csv")
uem = pd.read_csv(r"g:\Economic Indicators\unemployment_2000_2024.csv")
#merging the data
merged_data = pd.merge(gdp, uem, on=["Country Name","Year"], how="outer")
merged_data = pd.merge(merged_data, cpi, on=["Country Name","Year"],how="outer")
merged_data.to_csv("merged_economic_indicators_2000_2024.csv", index=False)
print(merged_data.head(60))