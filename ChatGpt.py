import asyncio
from ChatGPT_lite.ChatGPT import Chatbot

class MyChatGPT:

    def __init__(self,env):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.chat = Chatbot(env["token_key"], 'https://gpt.pawan.krd')
        self.loop.run_until_complete(self.chat.wait_for_ready())
        
    def ask(self, prompt, id=None):
        res = self.loop.run_until_complete(self.chat.ask(prompt))
        return res['answer']
        
    def close(self):
        self.chat.close()
        self.loop.stop()


    