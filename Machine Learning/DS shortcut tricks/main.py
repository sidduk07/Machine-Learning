import pandas as pd
from pandas_profiling import ProfileReport

df =pd.read_csv("Social_Network_Ads.csv")

print(df)

#genarte report
profile = ProfileReport(df)
profile.to_file(output_file="social-network-ads-anlysed-report.html")