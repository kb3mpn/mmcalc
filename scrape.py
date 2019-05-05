import urllib.request
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
url = "https://www.megamillions.com/cmspages/utilservice.asmx/GetLatestDrawData"
headers={'User-Agent':user_agent,} 
request=urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(request)
drta = response.read() 
with open ('outfile', 'wb') as f:
     f.write(drta)
import os
#os.system('dos2unix outfile')
#print('done fixing file')
#this next part is WAY FUCKING EASIER WITH BASH
with open('outfile', 'r') as fin:
    data = fin.read().splitlines(True)
with open('outfile', 'w') as fout:
    fout.writelines(data[1:])
with open('outfile', 'r') as fin:
    lines = fin.readlines()
    lines[0] = lines[0][36:] # Strip just the first 36
with open('outfile', 'w') as fout:
    for line in lines:
        fout.write(line)
with open('outfile', 'rb+') as filehandle:
    filehandle.seek(-9, os.SEEK_END)
    filehandle.truncate()
import json
with open('outfile', 'r') as g:
    datastore = json.load(g)
cash_value = int(datastore["Jackpot"]["NextCashValue"])
immediate = 0.76
first_year = 0.63
NY = 0.0881
MO = 0.04
AZ = 0.05
KS = 0.05
print(' ')
print(f"The cash value is:", format(int(round(cash_value)), ',d'))
print(' ')
print(f"The value after initial federal tax is:", format(int(round(cash_value * immediate)), ',d'))
print(f"The value after initial tax and state for JC is:", format(int(round(cash_value * (immediate - NY))), ',d'))
print(f"The value after initial tax and state for Emmett is:", format(int(round(cash_value * (immediate - AZ))), ',d'))
print(f"The value after initial tax and state for Jonathan is:", format(int(round(cash_value * (immediate - AZ))), ',d'))
print(f"The value after initial tax and state for Mike (Missouri) is:", format(int(round(cash_value * (immediate - MO))), ',d'))
print(f"The value after initial tax and state for Mike (Kansas) is:", format(int(round(cash_value * (immediate - KS))), ',d'))
print(' ')
print(f"The value after first year federal tax is", format(int(round(cash_value * first_year)), ',d'))
print(f"First-year after total tax for JC is:", format(int(round(cash_value * (first_year - NY))), ',d'))
print(f"First-year after total tax for Emmett is:", format(int(round(cash_value * (first_year - AZ))), ',d'))
print(f"First-year after total tax for Jonathan is:", format(int(round(cash_value * (first_year - AZ))), ',d'))
print(f"First-year after total tax for Mike (Missouri) is:", format(int(round(cash_value * (first_year - MO))), ',d'))
print(f"First-year after total tax for Mike (Kansas) is:", format(int(round(cash_value * (first_year - KS))), ',d'))
print(' ')

