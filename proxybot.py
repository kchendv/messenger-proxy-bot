from fbchat import log, Client
from fbchat.models import Message
from dotenv import dotenv_values
from response import gen_response
from time import sleep

WHITELIST = ["100080013373577","100003903958977"]
BLACKLIST = ["100003903958977"]
# Read credentials from environment
config = dotenv_values(".env")

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {} by {}".format(message_object, thread_id, thread_type.name, author_id))

        # If you're not the author, echo
        # if author_id != self.uid:
        #     self.send(message_object, thread_id=thread_id, thread_type=thread_type)

        # Call response engine
        # if author_id != self.uid:
        if author_id in WHITELIST:
            response_chunk = gen_response(message_object.text)
            for r in response_chunk:
                self.send(Message(text = r), thread_id = thread_id, thread_type = thread_type)
                sleep(0.1)

client = EchoBot(config["EMAIL"], config["PASSWORD"])
client.listen()