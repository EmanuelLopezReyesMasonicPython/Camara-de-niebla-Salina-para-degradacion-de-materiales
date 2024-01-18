#SENSOR HUMEDAD Y TEMPERATURA
import dht
from machine import Pin
import utime
dht11 = dht.DHT11(Pin(6))

#pantalla
from machine import Timer, Pin, I2C
from sh1106 import SH1106_I2C
WIDTH  = 128                                           
HEIGHT = 64                                             
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)      
print(i2c.scan())
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) 
print("I2C Configuration: "+str(i2c))                   
oled = SH1106_I2C(WIDTH, HEIGHT, i2c)
oled.rotate(180)

#RELAYS
from machine import Pin
import utime
# Configurar el pin GPIO para el LED
lampara= Pin(2, Pin.OUT)
valvula= Pin(3, Pin.OUT)

#VARIABLES
ciclo = 0
HORA=0
HORA2=0
HORAV=0
HORAV2=0

#............................................................................................................................#
try:
    while True:
        
        HORA= ciclo%18
        HORA2= ciclo%36
        #tiempo encendida la valvula
        HORAV= ciclo%1
        #tiempo apagada la valvula
        HORAV2= ciclo%8
        dht11.measure()
        t = dht11.temperature()
        h = dht11.humidity()
        print()
        utime.sleep_ms(1000)
        
        #RELAY
        
        utime.sleep_ms(1000)
        ciclo= ciclo +1
        
        print ("CICLO NO: " + str(ciclo)+"		TEMPERATURA="+str(t)+" 		HUMEDAD="+str(h)+"						TIEMPO DE DEGRADACION EN HORAS: " + str((ciclo * 2)/3600)+"		TIEMPO DE DEGRADACION EN MINUTOS: " + str((ciclo * 2)/60)+"		TIEMPO DE DEGRADACION EN SEGUNDOS: " + str(ciclo * 2))
    
        
        
        if HORA==0:
            #ENCIENDE LUZ
            lampara.value(1)
        
        if HORA2==0:
            #APAGAR LUZ
            lampara.value(0)
            
        if HORAV==0:
            #ENCIENDE LUZ
            valvula.value(1)
        
        if HORAV2==0:
            #APAGAR LUZ
            valvula.value(0)
        
        
        #PANTALLA
         #pantalla
        oled.fill(0)
        oled.text("CAMARA SALINA ",10, 0)            
        oled.text("TEMPERATURA: ",0, 10)
        oled.text(str(t),100, 10)
        oled.text("HUMEDAD: ",0, 20)
        oled.text(str(h),100, 20)
        oled.text("HORAS",0, 30)
        oled.text(str((ciclo * 2)/3600),80, 30)
        oled.text("MINUTOS:",0, 40)
        oled.text(str((ciclo * 2)/60),80, 40)
        oled.text("SEGUNDOS:",0, 50)
        oled.text(str(ciclo * 2),80, 50)
        oled.text("NOCHE:",0, 80)
        
        oled.show()
        
        
except KeyboardInterrupt:
        #CTRL+C DETECTADO
        print ("Saliendo del lazo WHILE")
