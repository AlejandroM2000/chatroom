# ChatRoom project purposes

### For this project I will want to create a chat room like CLI where two users will be able to send messages to each otehr when there is a server in the middle, where the "server" will be my computer

# What do I plan to learn
- HTTP
- TCP/IP
- security protocols

# General Outline
I want to make a server where it will receive messages from all clients that are present in the chatroom
- server will be designated by who is running the app ie localhost: 8080
- for client to connect, they will need to know the port number they are connecting to 
- figure out if this is safe, if not, make it safe


# How does it work?
For a chatroom model to work, we go with the client-server model to initiate this.  For the actual cleints to be actual connect, we must use socket programming to be able to connnect and deliver messages to the other clients. A **Socket** is bound to the port n umber so that the process is identified.  fort he actyual communication to take place, the location of the destination computing node is IDed using the IP address of the node's network.  Followingn this, the physical address of the machine is found using the MAC address. the atual comunication of the is done between the processes

# Socket interface
- AF_INET: address family that is used to designate the type of address that your socket can communicate with (for this, its IPv4), the address format is host and port number.  T his si the one thats used for normal TCP/IP usage
- SOCK_STREAM: used for TCP connection-oriented socket