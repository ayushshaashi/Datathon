import pandas
from pandas_profiling import ProfileReport

DataFile = pandas.read_csv("Data.csv")

Report = ProfileReport(DataFile)
Report.to_file(output_file="DataReport.html")