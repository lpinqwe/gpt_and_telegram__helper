import csv

import gpt_assistant.web_driver
from gpt_assistant.html_getter import HTMLGetter


class Requester(gpt_assistant.web_driver.GPTHelper):
    template = f'''jezeli w tym html kodzie jest oferta pracy SPELNIAJACA WSZYSTKIE
                   PODANE warunki napisz TYLKO 'YES123'+W nactepnej linijce wypisz
                   krotko informacje o tej ofercie i podaj jej html kod + wytlumacz
                   czemu wybrales to+ podaj slowa kluczowe ktore przekonaly ciebie.
                   Inaczej 'NO321'. 
                   POSTARAJ SIE
                   ODPOWIADAJ TYLKO PO ANGIELSKU
                   warunki:
                   '''
    output_message = ''
    bufpage = None
    strbuf = None
    default_page = r"https://www.pracuj.pl/praca/c%25252b%25252b%2520programmer"
    default_filepath = r"C:\Users\vwork\PycharmProjects\gpt_and_telegram__helper\test_file.csv"

    def get_page(self, page=default_page):
        print(f"page={page} ,buf={self.bufpage}")
        if page == self.bufpage:
            return self.strbuf
        else:
            self.bufpage = page
            getter = HTMLGetter()
            mystr = getter.get_html(page)
            self.strbuf = mystr
            return mystr

    def add_request(self, filepath=default_filepath):
        file = open(filepath)
        csvreader = csv.reader(file)
        headers = next(csvreader)

        for row in csvreader:
            req = row[0]
            url = row[1]
            html = self.get_page(url)
            print(f"req={req}\nurl={url} html={html[1:10]}")

        # print(headers)
        # print(rows)
        # for i in rows:

        # print(text_request)

    def get_output_msg(self):
        return self.output_message


rr = Requester()
rr.add_request()
