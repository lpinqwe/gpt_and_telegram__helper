import gpt_assistant.web_driver
import urllib.request
import csv
import pyppeteer

class requester(gpt_assistant.web_driver.gpt_helper):
    default_page=r"https://www.pracuj.pl/praca/c%25252b%25252b%2520programmer"
    default_filepath=r"C:\Users\vwork\PycharmProjects\gpt_and_telegram__helper\test_file.csv"
    def get_page(self,page=default_page):
        fp = urllib.request.urlopen(page)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        print(mystr)
        return mystr
    def add_request(self,filepath=default_filepath):
        file = open(filepath)
        csvreader=csv.reader(file)
        headers=[]
        headers=next(csvreader)
        rows = []
        for row in csvreader:
            rows.append(row)
        #print(headers)
        #print(rows)
        #for i in rows:
        print(rows[0][1])
        text_request=self.get_page()
        #print(text_request)

rr=requester()
rr.add_request()