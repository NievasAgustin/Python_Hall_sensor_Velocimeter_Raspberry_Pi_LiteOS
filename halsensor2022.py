def shut_down():
    print("shutting down")
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
while True:
        Funcionamiento_normal=1
        Tiempo_para_apagar=0
        Tiempo_inicio=0
        Tiempo_trabajo=0
        Tiempo_diferencia=1
        Tiempo_diferencia_inicial=0
        Tiempo_diferencia_final=1
        Segundos_unidad=0
        Segundos_decena=0
        Segmento_display_led_a=23
        Segmento_display_led_b=24
        Segmento_display_led_c=8
        Segmento_display_led_d=25
        Segmento_display_led_e=14
        Segmento_display_led_f=15
        Segmento_display_led_g=18
        Segmentos_display_todos=[a,b,c,d,e,f,g]
        Velocidad_total=0
        Velocidad_unidad=8
        Velocidad_decena=8
        Display_velocidad_unidad=1
        Display_velocidad_decena=7
        Display_segundos_unidad=12
        Display_segundos_decena=16
        Radio_rodillo=0.1
        Sensor_hall=20
        Pulsador_control=21
        gpio.setup(Sensor_hall, gpio.IN)
        gpio.setup(Pulsador_control, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.setup(Segmentos_display_todos, gpio.OUT)
        gpio.setup(Display_velocidad_unidad, gpio.OUT)
        gpio.setup(Display_velocidad_decena, gpio.OUT)
        gpio.setup(Display_segundos_unidad, gpio.OUT)
        gpio.setup(Display_segundos_decena, gpio.OUT)
        gpio.add_event_detect(Sensor_hall, gpio.FALLING)
        gpio.add_event_detect(Pulsador_control, gpio.RISING)
        gpio.output(Display_velocidad_unidad, gpio.LOW)
        gpio.output(Display_velocidad_decena, gpio.LOW)
        gpio.output(Display_segundos_unidad, gpio.LOW)
        gpio.output(Display_segundos_decena, gpio.LOW)
        gpio.output(Segmentos_display_todos, gpio.LOW)
        Numero_segmentos_display={
                    0: (gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.LOW)
                    1: (gpio.LOW, gpio.HIGH, gpio.HIGH, gpio.LOW, gpio.LOW, gpio.LOW, gpio.LOW)
                    2: (gpio.HIGH, gpio.HIGH, gpio.LOW, gpio.HIGH, gpio.HIGH, gpio.LOW, gpio.HIGH)
                    3: (gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.LOW, gpio.LOW, gpio.HIGH)
                    4: (gpio.LOW, gpio.HIGH, gpio.HIGH, gpio.LOW, gpio.LOW, gpio.HIGH, gpio.HIGH)
                    5: (gpio.HIGH, gpio.LOW, gpio.HIGH, gpio.HIGH, gpio.LOW, gpio.HIGH, gpio.HIGH)
                    6: (gpio.HIGH, gpio.LOW, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH)
                    7: (gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.LOW, gpio.LOW, gpio.HIGH, gpio.LOW)
                    8: (gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.HIGH)
                    9: (gpio.HIGH, gpio.HIGH, gpio.HIGH, gpio.LOW, gpio.LOW, gpio.HIGH, gpio.HIGH)
                    }
        while Funcionamiento_normal:
                if (gpio.event_detected(Pulsador_control)):
                            gpio.output(Display_velocidad_unidad, gpio.HIGH)
                            gpio.output(Segmentos_display_todos, Numero_segmentos_display[0])
                            time.sleep(0.4)
                            gpio.output(Display_velocidad_unidad, gpio.LOW)
                            gpio.output(Display_velocidad_decena, gpio.HIGH)
                            time.sleep(0.4)
                            gpio.output(Display_velocidad_decena, gpio.LOW)
                            gpio.output(Display_segundos_unidad, gpio.HIGH)
                            time.sleep(0.4)
                            gpio.output(Display_segundos_unidad, gpio.LOW)
                            gpio.output(Display_segundos_decena, gpio.HIGH)
                            time.sleep(0.4)
                            gpio.output(Display_segundos_decena, gpio.LOW)
                            Tiempo_inicio=time.time()
                            Tiempo_diferencia_inicial=time.time()
                            Run=1
                            while Run:
                                    apagando=0
                                    if(gpio.event_detected(Sensor_hall)):
                                                Tiempo_diferencia_final=time.time()
                                                Tiempo_diferencia=Tiempo_diferencia_final-Tiempo_diferencia_inicial
                                                Tiempo_diferencia_inicial=time.time()
                                                beta=(2*3.1415926535*Radio_rodillo)/Tiempo_diferencia
                                                Velocidad_total=beta*3.6/4
                                                Velocidad_total=int(round(Velocidad_total))
                                                Velocidad_unidad=int(Velocidad_total%10)
                                                Velocidad_decena=int((Velocidad_total-Velocidad_unidad)/10)
                                    Tiempo_trabajo=int(round(time.time() - Tiempo_inicio))
                                    if ((time.time()-Tiempo_diferencia_inicial)>20):
                                                Velocidad_total=0
                                    Segundos_unidad=int(Tiempo_trabajo%10)
                                    Segundos_decena=int(((Tiempo_trabajo-Segundos_unidad)/10)%10)
                                    gpio.output(Display_velocidad_unidad, gpio.HIGH)
                                    gpio.output(Segmentos_display_todos, Numero_segmentos_display[Velocidad_unidad])
                                    time.sleep(0.005)
                                    gpio.output(Display_velocidad_unidad, gpio.LOW)
                                    gpio.output(Segmentos_display_todos, Numero_segmentos_display[Velocidad_decena])
                                    gpio.output(Display_velocidad_decena, gpio.HIGH)
                                    time.sleep(0.005)
                                    gpio.output(Display_velocidad_decena, gpio.LOW)
                                    gpio.output(Segmentos_display_todos, Numero_segmentos_display[Segundos_unidad])
                                    gpio.output(Display_segundos_unidad, gpio.HIGH)
                                    time.sleep(0.005)
                                    gpio.output(Display_segundos_unidad, gpio.LOW)
                                    gpio.output(Segmentos_display_todos, Numero_segmentos_display[Segundos_decena])
                                    gpio.output(Display_segundos_decena, gpio.HIGH)
                                    time.sleep(0.005)
                                    gpio.output(Display_segundos_decena, gpio.LOW)
                                    if gpio.input(Pulsador_control)==True:
                                                Run=0
                                                while gpio.input(Pulsador_control)== True:
                                                        Tiempo_para_apagar=Tiempo_para_apagar+0.05
                                                        if Tiempo_para_apagar > 1000:
                                                                shut_down()
                            gpio.output(Display_velocidad_unidad, gpio.HIGH)
                            gpio.output(Segmentos_display_todos, Numero_segmentos_display[Velocidad_unidad])
                            time.sleep(0.005)
                            gpio.output(Display_velocidad_unidad, gpio.LOW)
                            gpio.output(Segmentos_display_todos, Numero_segmentos_display[Velocidad_decena])
                            gpio.output(Display_velocidad_decena, gpio.HIGH)
                            time.sleep(0.005)
                            gpio.output(Display_velocidad_decena, gpio.LOW)
                            gpio.output(Display_segundos_unidad, gpio.HIGH)
                            gpio.output(Segmentos_display_todos, Numero_segmentos_display[Segundos_unidad])
                            time.sleep(0.005)
                            gpio.output(Display_segundos_unidad, gpio.LOW)
                            gpio.output(Segmentos_display_todos, Numero_segmentos_display[Segundos_decena])
                            gpio.output(Display_segundos_decena, gpio.HIGH)
                            time.sleep(0.005)
                            gpio.output(Display_segundos_decena, gpio.LOW)
