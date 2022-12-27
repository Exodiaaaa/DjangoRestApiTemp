from django.db import models
import telepot, pywhatkit

token = "**************************"
rece_id = "*********"
bot = telepot.Bot(token);
c = 0;

class Dht (models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.temp)

    def save(self , *args , **kwargs) :

        if self.temp > 10:
            bot.sendMessage(rece_id, "High temp!"+ str(self.temp))
            pywhatkit.sendwhatmsg_instantly(f'+***********',"High TEMP "+str(self.temp),10)


        return super().save(*args, **kwargs)