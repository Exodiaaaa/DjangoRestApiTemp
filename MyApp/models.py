from django.db import models
import telepot, pywhatkit


def sendtelegram(temp, chat_id):
    token = "5608409696:AAEjXiPn91L8yVzonMAcAIedSA0mPGK1b90"
    rece_id = chat_id
    bot = telepot.Bot(token)
    bot.sendMessage(rece_id, "High temp!" + str(temp) + "°C 🌡️")


def sendwhatsapp(temp):
    pywhatkit.sendwhatmsg_instantly(f'+212604009383', "High TEMP " + str(temp)+"°C 🌡️", 10)

def sendtogroup(temp):
    contact = ['604009383', '762969835', '697239084']
    for tel in contact:
        pywhatkit.sendwhatmsg_instantly(f'+212'+tel, "High TEMP " + str(temp)+"°C 🌡️", 20)


class Dht (models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)
    c = 0

    def __str__(self):
        return str(self.temp)

    def save(self, *args, **kwargs):
        if self.temp > 10:
            sendtelegram(self.temp, "5465569016")
            Dht.c += 1
        else:
            Dht.c = 0

        if Dht.c > 2:
            sendtelegram(self.temp, "5465569016")
            sendtelegram(self.temp, "5418445446")

        return super().save(*args, **kwargs)