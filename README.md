# PolygonStreamer
This is a temporary replacement to get streaming data form polygon api, while streamconn get fixed.

Define or Import the class provided in the source
usage:


if __name__ == "__main__":
    conn = polygonStream('pass_Your_key_here') 

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

################################################################################################    
This also automatically recovers from connection closed error as shown below

Quote [{'ev': 'Q', 'sym': 'GLPG', 'c': 1, 'bx': 12, 'ax': 12, 'bp': 171.82, 'ap': 172.05, 'bs': 2, 'as': 3, 't': 1565958503394, 'z': 3}]
Quote [{'ev': 'Q', 'sym': 'GLPG', 'c': 1, 'bx': 12, 'ax': 12, 'bp': 171.82, 'ap': 172.04, 'bs': 2, 'as': 1, 't': 1565958503401, 'z': 3}]
[WinError 10054] An existing connection was forcibly closed by the remote host
### closed ###
[Errno 11001] getaddrinfo failed
### closed ###
[Errno 11001] getaddrinfo failed
### closed ###
[Errno 11001] getaddrinfo failed
### closed ###
Quote [{'ev': 'Q', 'sym': 'GLPG', 'c': 1, 'bx': 12, 'ax': 12, 'bp': 171.82, 'ap': 172.04, 'bs': 2, 'as': 1, 't': 1565958503401, 'z': 3}]
Quote [{'ev': 'Q', 'sym': 'GLPG', 'c': 1, 'bx': 12, 'ax': 12, 'bp': 171.82, 'ap': 172.04, 'bs': 2, 'as': 1, 't': 1565958503401, 'z': 3}]
