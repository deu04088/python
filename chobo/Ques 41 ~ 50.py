#41번
ticker_B = "btc_krw"
ticker_B1 = ticker_B.upper()
print(ticker_B1)

#42번
ticker_S = "BTC_KRW"
ticker_S1 = ticker_S.lower()
print(ticker_S1)

#43번
h = "hello"
h = h.capitalize()
print(h)

#44번
file_name = "보고서.xlsx"
file_name.endswith("xlsx")

#45번
file_name.endswith(("xlsx", "xls"))

#46번
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")

#47번
a = "hello world"
a.split()
print(a)

#48번
ticker_SW = "btc_krw"
ticker_SW.split("_")
print(ticker_SW)

#49번
date = "2020-05-01"
date.split("-")
print(date)

#50번
data = "039490     "
data = data.strip()
print(data)