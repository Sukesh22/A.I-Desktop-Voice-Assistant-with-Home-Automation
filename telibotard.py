import telepot,time
import serial
ser = serial.Serial('COM3',9600)

def telebotard(msg):
    
    userName = msg['from']['first_name']+" "+msg['from']['last_name']
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if(content_type == 'text'):
        command = msg['text']
        print('Got Command: %s' % command)
        
        if 'hello' in command:
            bot.sendMessage(chat_id, "Hello, this is telebot for Arduino UNO how can i help you?")
        if 'help' in command:
            bot.sendMessage(chat_id, "Hello %s, how can i help you?" %userName)
        if 'on light' in command:
            ser.write(b'Y')
        if 'off light' in command:
            ser.write(b'N')        
            
            
bot = telepot.Bot('5987771914:AAEPWdJLvCDLekEwL5viK93uP1Gtoo9hJKU') 

bot.message_loop(telebotard)

while 1:
    time.sleep(20)
               
            