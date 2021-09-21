#Версия модуля "Rp команды" от @roki_crazy
from .. import loader, utils

@loader.tds
class myRPMod(loader.Module):
    """Модуль Rp команды"""
    strings = {'name': 'RP команды|by @roki_crazy'}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("Rpcomands", "status", True)

    async def rpvcmd(self, message):
        """Используй: .rpv чтобы включить/выключить RP режим."""
        status = self.db.get("myRPMod", "status")
        if status is not False:
            self.db.set("myRPMod", "status", False)
            await message.edit("<b>RP Режим <code>выключен</code></b>")
        else:
            self.db.set("myRPMod", "status", True)
            await message.edit("<b>RP Режим <code>включен</code></b>")

    async def rplcmd(self, message):
        """Используй: .rpl чтобы посмотреть список рп команд."""
        await message.edit("<b>• покормить\n• поцеловать\n• пожелать\n• цьмок\n• укусить\n• предложить\n• няшиться\n• выстрелить\n• домогаться \n• похвалить\n• забрать\n• лечь"
                           "\n• поблагодарить\n• секрет\n• убить\n• признаться\n• похоронить\n• обнять\n• почка\n• наказать\n• выпить\n• привет"
                           "\n•застрял\n• попросить\n• привязать\n• по жопе\n• раком\n• извиниться\n• чапалах\n• потрогать в\n• потрогать г\n• потрогать к\n• потрогать с\n• потрогать ш\n• потрогать п\n• потрогать ж\n• куни\n• соси!\n• нежно\n• жестко\n• кончил\n• приехать\n• играть\n• читать\n• как дела\n• коды\n• мозги</b>")

    async def watcher(self, message):
        try:
            status = self.db.get("myRPMod", "status")
            reply = await message.get_reply_message()
            user = await message.client.get_entity(reply.sender_id)
            me = (await message.client.get_me())
            if status is not False:
                if message.sender_id == me.id:
                   if message.text.lower() == "покормить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> покормил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "цьмок":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> цьмокнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "укусить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> укусил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "предложить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> предложил(-а) заняться сексом <a href=tg://user?id={user.id}>{user.first_name}</a> 🔞")
                   if message.text.lower() == "няшиться":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> няшиться с <a href=tg://user?id={user.id}>{user.first_name}</a> 🥰❤")
                   if message.text.lower() == "выстрелить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> выстрелил(-а) в <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "домогаться":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> домогаеться до <a href=tg://user?id={user.id}>{user.first_name}</a> 🥵")
                   if message.text.lower() == "похвалить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> похвалил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "забрать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> забрал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a> к себе")
                   if message.text.lower() == "лечь":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> лег(-ла) в кроватку <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "поблагодарить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поблагодарил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "секрет":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> рассказал(-а) секретик <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "убить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> убил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "признаться":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> признался(-ась) в любви <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "похоронить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> похоронил(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "обнять":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> крепко обнял(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "почка":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> продал(-а) почку <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "наказать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> наказал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "выпить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> бахнул(-а) пивка с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "привет":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поздоровался(-ась) с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "застрял":
                       await message.edit(f"<a href=tg://user?id={user.id}>{user.first_name}</a> застрял(-а) в стиральной машинке")
                   if message.text.lower() == "нежно":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> нежно трахнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>🥵")
                   if message.text.lower() == "жестко":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> жестко трахнул(-а) <a href=tg://user?id={user.id}>{user.first_name}</a>🥵")
                   if message.text.lower() == "кончил":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> кончил в киску <a href=tg://user?id={user.id}>{user.first_name}</a> 💦💦")
                   if message.text.lower() == "по жопе":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-а) по жопе <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "куни":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a>  сделал(-а) куни <a href=tg://user?id={user.id}>{user.first_name}</a> 💦")
                   if message.text.lower() == "соси!":
                        await message.edit(f"<a href=tg://user?id={user.id}>{user.first_name}</a> сосет у <a href=tg://user?id={me.id}>{me.first_name}</a>")
                   if message.text.lower() == "привязать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a>  привязал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a> к кроватке")
                   if message.text.lower() == "попросить":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a>  попросил <a href=tg://user?id={user.id}>{user.first_name}</a> отсосать ему 🍌💦")
                   if message.text.lower() == "раком":
                        await message.edit(f"<a href=tg://user?id={user.id}>{user.first_name}</a> стала раком")
                   if message.text.lower() == "потрогать в":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> потрогал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a> за волосы💆‍♀️")
                   if message.text.lower() == "потрогать г":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> потрогал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a> за грудь‍🍒")
                   if message.text.lower() == "потрогать к":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> потрогал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a> за киску🐱")
                   if message.text.lower() == "потрогать с":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> потрогал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a> за соски😋")
                   if message.text.lower() == "потрогать ш":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> потрогал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a> за шею🥵")
                   if message.text.lower() == "потрогать п":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> потрогал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a> за попу🍑")
                   if message.text.lower() == "потрогать ж":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> потрогал(-а) <a href=tg://user?id={user.id}>{user.first_name}</a> за животик🥰")
                   if message.text.lower() == "приехать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> приехал(-а) в гости к <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "читать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> читает книгу с <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "играть":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> сказал <a href=tg://user?id={user.id}>{user.first_name}</a> пошли играть в Pubg Mobile ")
                   if message.text.lower() == "как дела":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> спросил(-ла) как дела у <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "коды":
                        await message.edit(f"<a href=tg://user?id={user.id}>{user.first_name}</a> говорит что кодирует новый модуль, а ты?")
                   if message.text.lower() == "мозги":
                        await message.edit(f"<a href=tg://user?id={user.id}>{user.first_name}</a> потерял мозги🧠 в канавке")
                   if message.text.lower() == "извиниться":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> извинился(-лась) перед <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "пожелать":
                         await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> пожелал(-ла) удачки <a href=tg://user?id={user.id}>{user.first_name}</a>")
                   if message.text.lower() == "чапалах":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> дал(-ла) смачного чапалаха <a href=tg://user?id={user.id}>{user.first_name}</a> со скоростью света ")
                   if message.text.lower() == "поцеловать":
                        await message.edit(f"<a href=tg://user?id={me.id}>{me.first_name}</a> поцеловал(а)🥺😘❤️ <a href=tg://user?id={user.id}>{user.first_name}</a> ")
        except: pass
