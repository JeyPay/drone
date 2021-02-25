
from package.socketManagement import ClientSocket


host = 'localhost' #input('Host : ')
port = 1231 #input('Port : ')

# Starting the connection with the drone
Connection = ClientSocket(host, port, connect = True)

def generateSet(Kp, Ki, Kd):
    with open('package/regulation.txt','w') as f:
        f.write(str(Kp)+' '+str(Ki)+' '+str(Kd))

    commandSet = str( { "id":"set", "Kp":Kp, "Ki":Ki, "Kd":Kd } )
    return commandSet

def generateGet():
    commandGet = str( { "id":"get" } )
    return commandGet

def generateEnd():
    commandEnd = str( { "id":"end" } )
    return commandEnd

"""def generateGENERAL_STOP():
    commandEnd = str( { "id":"GENERAL_STOP" } )
    return commandEnd"""


with open('package/regulation.txt','r',encoding='utf-8') as f:
    # We get the last regulation values set (saved in the txt file)
    data = f.readline().split(' ')

    command = generateSet(data[0], data[1], data[2])
    # We send these datas to the drone
    Connection.send(command)


bool_run = True

while bool_run:
    command = input('Command : ')
    cmd_split = command.split(' ')

    if cmd_split[0] == 'set':
        """
        usage : set Kp Ki Kd
        utility : set the Kp, Ki and Kd constants
        """
        command = generateSet(cmd_split[1], cmd_split[2], cmd_split[3])

    elif cmd_split[0] == 'get':
        """
        usage : get
        """
        command = generateGet()

    elif cmd_split[0] == 'end' or len(command) == 0:
        """
        usage : end
        utility : end connection with the drone, cut motors and end all programs
        """
        command = generateEnd()
        bool_run = False

    '''elif cmd_split[0] == 'GENERAL_STOP':
        """
        usage : GENERAL_STOP
        utility : Debug the safety check
        """
        command = generateGENERAL_STOP()'''

    print(command)
    try:
        # Send the generated command to the drone
        Connection.send(command)

    except Exception as e:
        # In case of exception, we display the error without crashing the program
        print(e)