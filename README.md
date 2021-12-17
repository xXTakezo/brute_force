# brute_force
Connect to a socket with a given hostname and port and try to find the correct username and password via Brute Force Method. Feel free to edit my code as you wish and need

This code will do:
Establish a socket connection with given hostname and password. The correct example syntax to use in the command line is: 

"python hack.py localhost 9090"

After the connection has been established, it will start trying to find the correct username to gain access. For this, it will read from a login file and try out all possible combinations from the usernames given. For this, the script will try out all combinations with an empty password. If the username is correct but the password wrong, the response message will tell us that the password is wrong but not the username login. 

After it finds the correct username, it will try to find the correct password letter by letter. This works by checking the response message from the socket : If the response message contains an exception error, this means that the first letter must be correct. This step is being repeated until the response message signifies a successful connection. All input and output data are being handled in JSON format.
If the socket connection you use does not show you an exception error, it might work to count how many seconds the socket needs to respond. If it takes more than 0.1 seconds, this usually means the response is an exception error, even if doesn't tell you that. Think outside the box.

Please note that in order to work this code for you, small minor changes have to be done. For example, you might want to change the login file or use a password dictionary. 
Therefore, feel free to use and change the code as you wish. 

--Alchemist
