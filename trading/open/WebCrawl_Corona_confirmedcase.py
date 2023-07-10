
# 한입에 웹크롤링 (BJ Public 출판, 김경록, 서영덕 지음 책 참조)

from urllib.request import urlopen
import json

import pandas as pd


def main():

    url = 'http://adrinfo.kr/chart'

    html = urlopen(url) # urllib로 html 가져오기
    # print(html.read())

    json_obj = json.load(html)
    print(json_obj)
    
##    dat_confirmed = json_obj['result']['emphasis'][0]['data']
##    # print(dat_confirmed)
##
##    dat_recovered = json_obj['result']['emphasis'][1]['data']
##    print(dat_recovered)
##    
##    dat_date = json_obj['result']['xAxis']
##    # print(dat_date)
##
##    dat_update = json_obj['result']['updatetime']
##
##    colList = list(zip(dat_date, dat_confirmed, dat_recovered))
##    
##    COVIDdf = pd.DataFrame(colList, columns = ['Date', 'AccuConfirm',
##                                                'AccuRecover'])
##
##    COVIDdf['AccuConfirmN'] = COVIDdf['AccuConfirm'].str.replace(',', '').astype(int)
##    COVIDdf['Date'] = COVIDdf['Date'].str.replace('.', '/')
##    # COVIDdf.iloc[:,1:].str.replace(',', '').astype(float)
##    print(COVIDdf.dtypes)
####    Cdf.read_csv('COVID19_Data_Korea'+dat_update[:11]+'.csv', sep=' ', \
####                 thousands=',')
##    COVIDdf['AccuConfirmN'] = COVIDdf['AccuConfirmN'].apply(pd.to_numeric)
##
##    COVIDdf['Day_ConfirmN'] = COVIDdf['AccuConfirmN'].diff()
##    # COVIDdf.set_index('Date', inplace=True)
##    print(COVIDdf.tail(10))
##
##    COVIDdf.to_csv('COVID19_Data_Korea_'+dat_update[:10]+'.csv', index=False)

    
# main 함수 로딩부
if __name__ == '__main__':
    main()

