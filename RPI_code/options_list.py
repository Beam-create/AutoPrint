def Homing(com):
    print('Homing...')
    code = 'G28\n'
    bytes_code = code.encode('utf-8') 
    output = com.write(bytes_code)
    home = 0
    while home == 0:
        if com.in_waiting > 0:
            line = com.readline()
            try:
                decoded = line.decode('utf_8_sig')
                if decoded == 'ok\n':
                    home = 1
            except UnicodeDecodeError:
                print('failed to decode utf_8_sig')
                
def Linear(com):
    try:
        print('------------------')
        print('Mode mouvement X Y')
        print('------------------')
        print('Pour sortir, faire CTRL-C')
        while True:
        
            X = input('Deplacement en X : ')
            Y = input('Deplacement en Y : ')
    
            initial1 = 'G21\n G91\n M17 X Y\n'
            initial2 = 'G1 F2400\n'
            move_X = 'X' + X
            move_Y = 'Y' + Y
            move = 'G1 ' + move_X + ' ' + move_Y + '\n'
            final = 'M18\n'
            msg = initial1 + initial2 + move + final
    
            msg_send = msg.encode('utf-8')
            com.write(msg_send)
            print('Moving...')
            done = 0
            while done == 0:
                if com.in_waiting > 0:
                    line = com.readline()
                    try:
                        decoded = line.decode('utf_8_sig')
                        if decoded == 'ok\n':
                            done = 1
                    except UnicodeDecodeError:
                        print('failed to decode utf_8_sig')
    except KeyboardInterrupt:
        pass
    
def Vertical(com):
    
    try:
        print('------------------')
        print('Mode mouvement Z')
        print('------------------')
        print('Pour sortir, faire CTRL-C')
        while True:
        
            Z = input('Deplacement en Z : ')
    
            initial1 = 'G21\n G91\n M17 Z\n'
            initial2 = 'G1 F300\n'
            move_Z = 'Z' + Z
            move = 'G1 ' + move_Z + '\n'
            final = 'M18\n'
            msg = initial1 + initial2 + move + final
    
            msg_send = msg.encode('utf-8')
            com.write(msg_send)
            print('Moving...')
            done = 0
            while done == 0:
                if com.in_waiting > 0:
                    line = com.readline()
                    try:
                        decoded = line.decode('utf_8_sig')
                        print(decoded)
                        if decoded == 'ok\n':
                            done = 1
                    except UnicodeDecodeError:
                        print('failed to decode utf_8_sig')
    except KeyboardInterrupt:
        pass