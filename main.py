# Utilizando a lib discord.py
# Toda a documentação disponível em https://discordpy.readthedocs.io/en/stable/

import discord
import time
from datetime import datetime

class MyClient(discord.Client):

    # Quando o bot estiver conectado
    async def on_ready(self):
        await self.wait_until_ready() # Bloqueia a execução enquanto não estiver tudo pronto
        print('Logged on as {0}!'.format(self.user))
        self.alert_channel = self.get_channel(000000000000000000) # Canal que vai receber os alertas (pegar id pela ação on_message)
        self.loop.create_task(self.verify_pending()) # Inicia a thread do timer

    # Sempre que um usuário digitar alguma coisa
    async def on_message(self, message):
        if message.content.startswith('t!'): # "t!mensaagem"
            print(message.channel.id) # Log do id do canal onde a mensagem foi enviada

    # Timer
    async def verify_pending(self):
        while True:
            # print('verify_pending')
            # print(str(datetime.now().time()).startswith('11:42'))
            time.sleep(60)
            await self.alert_channel.send('Passou 1 minuto')

client = MyClient()

# Utilizar o identificador do bot criado no Discord
client.run('xxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.xxxxxxxxxxx-xxxxxxxxxxxxxxx') # 