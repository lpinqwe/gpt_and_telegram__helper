from g4f.client import Client


class GPTHelper:
    message = [{"role": "user", "content": "print ONLY 'test' "}]
    lest_response = None
    flag = True

    def add_request(self, text):
        self.message = [{"role": "user", "content": f'''jezeli w tym html kodzie jest oferta pracy SPELNIAJACA WSZYSTKIE
                                                    PODANE warunki napisz TYLKO 'YES123'+W nactepnej linijce wypisz
                                                    krotko informacje o tej ofercie i podaj jej html kod + wytlumacz
                                                    czemu wybrales to+ podaj slowa kluczowe ktore przekonaly ciebie.
                                                    inaczej 'NO321'. 
                                                    POSTARAJ SIE
                                                    ODPOWIADAJ TYLKO PO POLSKU LUB ANGIELSKU
                                                    warunki:i need a low code  vacancy with a more than 6000zl salary
                                                    albo do dogadania. 
                                                    '''}]

    def send_request(self):
        self.flag = False
        client = Client()
        response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=self.message)
        self.lest_response = response.choices[0].message.content
        self.flag = True
        # print(self.lest_response)


"""
bot = gpt_helper()
bot.add_request('m')
bot.send_request()
print(bot.lest_response)
"""
