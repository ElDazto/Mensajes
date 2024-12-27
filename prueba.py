import mss
import numpy as np
import cv2

# Definir la región del segundo monitor, asegúrate que las coordenadas estén correctas
second_monitor = {
    'top': 0,  # Y inicial
    'left': 2560,  # X inicial, que corresponde a la posición del segundo monitor
    'width': 1080,  # El ancho del segundo monitor
    'height': 1920  # La altura del segundo monitor
}

# Coordenadas absolutas del pixel que quieres analizar
pixel_x_absolute = 2615
pixel_y_absolute = 964

def check_pixel_for_notification():
    with mss.mss() as sct:
        # Tomar captura del segundo monitor
        screenshot = sct.grab(second_monitor)
        
        # Comprobar que la captura no esté vacía
        if screenshot.width == 0 or screenshot.height == 0:
            print("Error: la captura de pantalla tiene un tamaño inválido.")
            return
        
        # Convertir la imagen a un array de numpy
        img = np.array(screenshot)
        
        # Comprobar que la imagen convertida tenga un tamaño válido
        if img.size == 0:
            print("Error: la imagen convertida tiene un tamaño inválido.")
            return
        
        # Convertir a formato BGR (por defecto es RGBA en mss)
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)

        # Mostrar solo la región específica del monitor que estamos analizando
        roi = img_bgr  # Aquí ya estamos capturando toda la región, no necesitamos recortar más

        # Obtener el color del píxel donde se espera la notificación
        pixel_x_rel = pixel_x_absolute - second_monitor['left']
        pixel_y_rel = pixel_y_absolute - second_monitor['top']
        
        # Verificar si el píxel está dentro de la región
        if (0 <= pixel_x_rel < screenshot.width) and (0 <= pixel_y_rel < screenshot.height):
            pixel_color = img_bgr[pixel_y_rel, pixel_x_rel]
            print(f"Color del píxel (BGR): {pixel_color}")
        else:
            print("El píxel solicitado está fuera de la región capturada.")

        # Mostrar solo el píxel que estamos verificando
        cv2.imshow("Captured Pixel", img_bgr[pixel_y_rel-5:pixel_y_rel+5, pixel_x_rel-5:pixel_x_rel+5])  # Mostramos una pequeña región alrededor del píxel

        # Esperar a que se cierre la ventana
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Comprobar el píxel una vez
check_pixel_for_notification()
