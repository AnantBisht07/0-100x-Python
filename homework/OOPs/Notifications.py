class SMSNotifications:
    def send(self, message):
        print(f"{message}: Message sent using SMSNotifications")

class EmailNotifications:
    def send(self, message):
        print(f"{message}: Message sent using EmailNotifications")

class PushNotifications:
    def send(self, message):
        print(f"{message}: Message sent using PushNotifications")

# Homework: Interface function
def notify(notification, message):
    notification.send(message)

class WhatsupNotifications:
     def send(self, message):
        print(f"{message}: Message sent using WhatsupNotifications")

message = "Hello Sangeeta, order is shipped"
notify(SMSNotifications(), message)
notify(EmailNotifications(), message)
notify(PushNotifications(), message)
notify(WhatsupNotifications(), message)

