import mss
import time
import numpy as np
import cv2
import pyautogui
import os

# Definir la región del segundo monitor (X=2560, Y=0, width=1080, height=1920)
second_monitor = {
    'top': -383,
    'left': 2560,
    'width': 1080,
    'height': 1920
}

# Coordenadas absolutas del pixel de la notificación
pixel_x_absolute = 2615
pixel_y_absolute = 741

# color a buscar
target_color = [238, 62, 67]
target_color_2 = [242, 63, 67]

# mensaje preparado
mensaje = "Yo"

def check_pixel_for_notification():
    with mss.mss() as sct:
        while True:
            # Tomar captura del segundo monitor
            screenshot = sct.grab(second_monitor)
            
            # Convertir la imagen a un array de numpy
            img = np.array(screenshot)

            # Convertir a formato BGR (por defecto es RGBA en mss)
            img_bgr = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

            # Coordenadas relativas del píxel que estamos buscando
            pixel_x_rel = pixel_x_absolute - second_monitor['left']
            pixel_y_rel = pixel_y_absolute - second_monitor['top']

            # Verificar si el píxel está dentro de la región
            if (0 <= pixel_x_rel < screenshot.width) and (0 <= pixel_y_rel < screenshot.height):
                pixel_color = img_bgr[pixel_y_rel, pixel_x_rel]

                # Comprobar si el color del píxel coincide con el color de la notificación
                if np.array_equal(pixel_color, target_color) or np.array_equal(pixel_color, target_color_2):
                    print("¡Notificación encontrada! Realizando clic...")
                    # pyautogui.click(pixel_x_absolute, pixel_y_absolute)
                    # time.sleep(1)
                    pyautogui.click(2749, 1420)
                    time.sleep(0.5)
                    pyautogui.click(2749, 1387)
                    time.sleep(0.5)
                    pyautogui.click(3033, 1436)
                    time.sleep(0.2)
                    # pyautogui.write(mensaje)
                    # pyautogui.press("enter")
                    # print("Mensaje enviado.")
                    break  # Detener el bucle después de hacer clic
                else:
                    print(f"Color del píxel (BGR): {pixel_color}")
            else:
                print("El píxel solicitado está fuera de la región capturada.")
            
            # Esperar un poco antes de la siguiente iteración para no sobrecargar el CPU
            time.sleep(0.2)

# Iniciar la comprobación constante
while True:
    check_pixel_for_notification()