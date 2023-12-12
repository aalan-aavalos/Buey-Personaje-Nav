# Import para acceso a red
import network
# Para usar protocolo MQTT
from umqtt.simple import MQTTClient
from machine import Pin, PWM
from time import sleep

# Propiedades para conectar a un cliente
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/jmom/led"
MQTT_PORT = 1883

# Creamos un objeto PWM para manejar tonos del buzzer
buzzer = PWM(Pin(4, Pin.OUT))

# Iniciamos el buzzer
buzzer.init(freq=69, duty=512)
sleep(1)
buzzer.duty(0)

def play(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty(512)
    sleep(duration)
    buzzer.duty(0)

# Función para conectar a WiFi
def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Pixel', 'ninagata1987')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi connected")

# Función encargada de encender un led o reproducir melodía cuando un mensaje lo diga
def llegada_mensaje(topic, msg):
    print(msg)

    if msg == b'0':
        play(261, 0.25)  # DO
        play(261, 0.25)  # DO
        play(329, 0.25)  # MI
        play(349, 0.25)  # FA
        play(349, 0.25)  # FA
        play(329, 0.25)  # MI
        play(293, 0.25)  # RE
        play(261, 0.25)  # DO

        play(392, 0.25)  # SOL
        play(392, 0.25)  # SOL
        play(392, 0.5)   # SOL
        play(392, 0.25)  # SOL
        play(392, 0.25)  # SOL
        play(329, 0.25)  # MI
        play(329, 0.25)  # MI
        play(293, 0.25)  # RE
        
        play(261, 0.25)  # DO
        play(261, 0.25)  # DO
        play(329, 0.25)  # MI
        play(349, 0.25)  # FA
        play(349, 0.25)  # FA
        play(329, 0.25)  # MI
        play(293, 0.25)  # RE
        play(261, 0.25)  # DO

        play(392, 0.25)  # SOL
        play(392, 0.25)  # SOL
        play(392, 0.5)   # SOL
        play(392, 0.25)  # SOL
        play(392, 0.25)  # SOL
        play(329, 0.25)  # MI
        play(329, 0.25)  # MI
        play(293, 0.25)  # RE

    elif msg == b'1':
        play(261, 0.25)  # DO
        play(349, 0.25)  # FA
        play(261, 0.25)  # DO
        play(493, 0.25)  # SI
        play(440, 0.25)  # LA
        play(493, 0.25)  # SI

        play(349, 0.25)  # FA
        play(392, 0.25)  # SOL
        play(440, 0.25)  # LA
        play(440, 0.25)  # LA
        play(440, 0.25)  # LA
        play(440, 0.25)  # LA
        play(440, 0.25)  # LA
        play(493, 0.25)  # SI
        play(440, 0.25)  # LA
        play(392, 0.25)  # SO
        
        play(261, 0.25)  # DO
        play(349, 0.25)  # FA
        play(261, 0.25)  # DO
        play(493, 0.25)  # SI
        play(440, 0.25)  # LA
        play(493, 0.25)  # SI

        play(349, 0.25)  # FA
        play(392, 0.25)  # SOL
        play(440, 0.25)  # LA
        play(440, 0.25)  # LA
        play(440, 0.25)  # LA
        play(440, 0.25)  # LA
        play(440, 0.25)  # LA
        play(493, 0.25)  # SI
        play(440, 0.25)  # LA
        play(392, 0.25)  # SO
    elif msg == b'3':
        leds.value(1)
    elif msg == b'2':
        leds.value(0)

# Función para suscribir al broker, topic
def subscribir():
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, 
     user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectado a %s, en el topico %s" % (MQTT_BROKER, MQTT_TOPIC))
    return client

# Declarar el pin led
leds = Pin(5, Pin.OUT)
leds.value(0)



# Conectar WiFi
conectar_wifi()

# Suscribirse a un broker mqtt
client = subscribir()

# Ciclo infinito
while True:
    client.wait_msg()