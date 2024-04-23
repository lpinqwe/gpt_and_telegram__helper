from g4f.client import Client




class gpt_helper:
    message=[{"role": "user","content":"print ONLY 'error' "}]
    lest_responce=None
    flag=True
    def add_request(self,text):
        self.message=[{"role": "user","content":f"{text}"}]
    def send_request(self):
        self.flag = False
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.message,

        )
        self.lest_responce=response.choices[0].message.content
        self.flag=True
        #print(self.lest_responce)

'''
bot = gpt_helper()
bot.send_request()
print(bot.lest_responce)
'''