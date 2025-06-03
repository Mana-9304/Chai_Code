print("Hello world.")

import pandas as pd
import datetime
a = [{"Name" : "Gauri Shinde", "Emp role" : "Data Analyst", "Joining month" : "April", "Date" : "27/01/2025"}, {"Name" : "Nayan Halder", "Emp role" : "Data Analyst", "Joining month" : "January", "Date" : "01/04/2025"}]
df = pd.DataFrame(a)
pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)
print(df)   