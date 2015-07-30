import logging
import webapp2
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler
from google.appengine.api import mail

class ReplyHandler(InboundMailHandler):
    def receive(self, mail_message):
        logging.info("Received a message from: " + mail_message.sender)

        message = mail.EmailMessage()
        message.sender = "Simple Email GAE <email@your-app.appspotmail.com>"
        message.to = mail_message.sender
        message.subject = "Reply from GAE"
        message.body = "This is reply message from GAE"
       
        message.send()
        

app = webapp2.WSGIApplication([ReplyHandler.mapping()], debug=True)
