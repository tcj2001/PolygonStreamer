# Be sure to pip install websocket-client
# Details: https://pypi.org/project/websocket-client/

import websocket
import websockets 
import json
import asyncio
import logging
import time

#########################################################################################################################
class polygonStream(object):
    def __init__(self, key):
        self.key=key
        self._handlers = {}
        self.ws = websocket.WebSocketApp("wss://alpaca.socket.polygon.io/stocks",
                                                          on_message = self.on_message,
                                                          on_error = self.on_error,
                                                          on_close = self.on_close,
                                                          on_open = self.on_open)

    
    def on_message(self, message):
        msg = json.loads(message)
        channel=msg[0]["ev"]
        for pat, handler in self._handlers.items():
            if pat==channel:
               handler(self, channel, msg)

    def on_error(self, error):
        print(error)

    def on_close(self):
        print("### closed ###")

    def on_open(self):
        self.ws.send(json.dumps({'action': 'auth','params': self.key}))
        self.ws.send(json.dumps({'action': 'subscribe','params': self.channels}))

    def runme(self,channels):
        self.channels=channels
        self.ws = websocket.WebSocketApp("wss://alpaca.socket.polygon.io/stocks",
                                                          on_message = self.on_message,
                                                          on_error = self.on_error,
                                                          on_close = self.on_close,
                                                          on_open = self.on_open)


        while True:
            self.ws.run_forever(ping_interval=70, ping_timeout=None)
            time.sleep( 5)

        
    def on(self,channel_pat):
        def decorator(func):
            self.register(channel_pat, func)
            return func
        return decorator

    def register(self, channel, func):
        self._handlers[channel] = func

    def deregister(self, channel):
        del self._handlers[channel]


#########################################################################################################################

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    
    conn = polygonStream('AKSUG6JSSYD2DP63REQN') #live key

    @conn.on('A')
    def handle_messages(conn,channel,message):
        dosomething=True
        print ('minute',message)
       
    @conn.on('AM')
    def handle_messages(conn,channel,message):
        dosomething=True
        print ('second',message)

    @conn.on('T')
    def handle_messages(conn,channel,message):
        dosomething=True
        print ('Trade',message)
        
    @conn.on('Q')
    def handle_messages(conn,channel,message):
        dosomething=True
        print ('Quote',message)

    conn.runme('Q.*,T.*,A.*,AM.*')
    

