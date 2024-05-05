from g4f.client import Client


class GPTHelper:
    def __init__(self):
        self.client: Client = Client()
        self.message = [{"role": "user", "content": "My prompt"}]

    def send_request(self, prompt: str) -> str:
        self.message[0]["content"] = prompt
        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
                                                       messages=self.message)
        response = response.choices[0].message.content

        return response


bot = GPTHelper()
print(bot.send_request("2+2"))
