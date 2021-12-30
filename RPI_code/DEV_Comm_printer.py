import serial
import RPi.GPIO as GPIO
import time
import options_list as l1

class Menu():
    def __init__(self):
        
        self.ServoPin = 13
        self.ON = 3
        self.OFF = 10
        self.Status = False
        #self.ButtonPin = 13
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ServoPin, GPIO.OUT, initial=0)
        #GPIO.setup(self.ButtonPin, GPIO.IN)
        
    def Connection(self, USB):
        
        #USB = input('# du port USB (0 ou 1):')
        Port = '/dev/ttyUSB'+ str(USB)

        try:
            self.ser = serial.Serial(Port, 115200, timeout = 1)
            self.ser.flush()
            print('--------------------------')
            print('Connected to ' + Port)
            print('--------------------------')
            return self.ser
        except serial.SerialException:
            print('Connection failed')
    
    def Printer_Switch(self,switch):
        
        if switch == 'on':
            print("entrain d'allumer")
            pwm= GPIO.PWM(self.ServoPin,50)
            pwm.start(self.ON)
            time.sleep(0.5)
            pwm.stop()
            time.sleep(0.2)
            self.Status = True
            
        elif switch == 'off':
            pwm= GPIO.PWM(self.ServoPin,50)
            pwm.start(self.OFF)
            time.sleep(0.5)
            pwm.stop()
            time.sleep(0.2)
            self.Status = False
        else:
            pass
        
    
    def Auto_Status(self):
        Com_port = -1
        for USB in range(3):
            try:
                Port = '/dev/ttyUSB'+str(USB)
                ser = serial.Serial(Port, 115200, timeout = 1)
                ser.flush()
                Com_port = USB
            
                ser.close()
            except serial.SerialException:   
                pass
    
        return Com_port
        
            
try:
    Status = False
    menu = Menu()
    Com_port = menu.Auto_Status()
    if Com_port > -1:
        Status = True
        com= menu.Connection(Com_port)
    else:
        Status = False
    print('Bonjour Maitre')
    while True:
        
        while Status == False:
            Choix = 0
            print('Ender 3 est presentement ferme')            
            Choix= int(input('Allumer Ender 3? (1 : Oui / 2 : Sortir):'))
            if Choix == 1 :
                menu.Printer_Switch('on')
                time.sleep(5)
                Com_port = menu.Auto_Status()
                if Com_port > -1:
                    Status = True
                    com= menu.Connection(Com_port)
                else:
                    Status = False
            elif Choix == 2 :
                quit()
                
        while Status == True:
            Choix = 0
            print('Ender 3 est presentement allume')
            print('------------------------------------')
            print('Menu:')
            print('1 : Fermer Ender 3')
            print('2 : Mode "Fermer apres le print"')
            print('3 : Homing')
            print('4 : Bouger X et Y')
            print('5 : Bouger Z')
            print('------------------------------------')
            try:
                Choix= int(input('Choix :'))
            except ValueError:
                print('Erreur: Entrer un entier')
            if Choix == 1:
                menu.Printer_Switch('off')
                time.sleep(5)
                Com_port = menu.Auto_Status()
                if Com_port > -1:
                    Status = True
                    menu.Connection()
                else:
                    Status = False
                Status = False
                break
            if Choix == 2:
                print("L'imprimante se fermera a la fin du print.")
                print('Pour annuler le mode, faire CTRL-C.')
                try:
                    while True:
                        if com.in_waiting > 0:
                            line = com.readline()
                            print(line)
#                             print(type(line))
                            try:
                                decoded = line.decode('utf_8_sig') #.decode('utf-8').rstrip()
                                if decoded == 'Done printing file\n':
                                    print('Print termine, fermeture...')
                                    menu.Printer_Switch('off')
                                    time.sleep(5)
                                    Com_port = menu.Auto_Status()
                                    if Com_port > -1:
                                        Status = True
                                    else:
                                        Status = False
                                    break
                            except UnicodeDecodeError:
                                print('failed to decode utf_8_sig')
                except KeyboardInterrupt:
                    pass

            if Choix == 3:
                l1.Homing(com)
                
            if Choix == 4:
                l1.Linear(com)
                
            if Choix == 5:
                l1.Vertical(com)
                
except KeyboardInterrupt:
    print('Fermeture du programme...')
    
finally:
    GPIO.cleanup()  