"""
File: webcrawler.py
Name: Lydia
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        tbody = soup.find_all('tbody')
        # print(tbody)
        for item in tbody:
            # print(item)
            # print(item.text)
            data = item.text.split()  # divide item.text into a list
            # print(data)
            male_num = 0
            female_num = 0
            for i in range(200):  # there are 200 "set" of name and numbers from rank 1 to 200
                if data[i] == 'source':  # after 'source', we don't need it
                    break
                male_value = data[2 + i * 5]  # at this regular pattern, it indicates male name's numbers
                male_lst = male_value.split(',')
                male_num += int(male_lst[0])*1000+int(male_lst[1])
                female_value = data[4 + i * 5]  # at this regular pattern, it indicates female name's numbers
                female_lst = female_value.split(',')
                female_num += int(female_lst[0])*1000 + int(female_lst[1])
            print('Male Number: ', male_num)
            print('Female Number: ', female_num)


if __name__ == '__main__':
    main()
