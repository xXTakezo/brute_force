# brute_force
Connect to a socket with a given hostname and port and try to find the correct username and password via Brute Force Method. Feel free to edit my code as you wish and need

This code will do:
Establish a socket connection with given hostname and passwort. The correct example syntax to use in the command line is: 

"python hack.py localhost 9090"

After the connection has been established, it will start trying to find the correct username to gain access. For this, it will read from a login file and try out all possible combinations from the usernames given. Feel free to edit the code and use your own login text files as you wish. 

After it finds the correct username, it will try to find the correct password letter by letter. This works by checking the response message from the socket : If the response message contains an exception error, this means that the first letter must be correct. This step is being repeated until the response message signifies a successful connection. 

Please note that in order to work this code for you, small minor changes have to be done. For example, you might want to change the login file or use a password dictionary. 
Therefore, feel free to use and change the code as you wish. 

--Alchemist
