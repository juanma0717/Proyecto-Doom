from machine import SPI, Pin
import random
import time
import ST7735
from sysfont import sysfont


# Inicialización de la pantalla ST7735
spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(7), mosi=Pin(11), miso=Pin(9)) # ESP32 Mini
tft = ST7735.TFT(spi, 16, 17, 18)
tft.initr()
tft.rgb(True)

# Tamaño de la pantalla
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 160
GRID_SIZE = 8  # Tamaño de cada celda de la cuadrícula


# Colores
WHITE = tft.color(255, 255, 255)
BLACK = tft.color(0, 0, 0)
BLUE = tft.color(0, 0, 255)
RED = tft.color(255, 0, 0)
GREEN = tft.color(0, 255, 0)

# Botones para navegación
button_select = Pin(5, Pin.IN, pull=Pin.PULL_DOWN)  # Botón de selección
button_up = Pin(33, Pin.IN, pull=Pin.PULL_DOWN)      # Botón arriba
button_down = Pin(34, Pin.IN, pull=Pin.PULL_DOWN)    # Botón abajo

# Opciones del menú
menu_options = ["Snake", "Pong"]
current_option = 0  # Opción seleccionada actualmente

# Función para mostrar el menú de selección de juegos
def display_menu(selected_option):
    tft.fill(BLACK)  # Limpiar pantalla
    for i, option in enumerate(menu_options):
        color = RED if i == selected_option else WHITE
        # Especificar todos los argumentos necesarios, incluido el tamaño y el color de fondo
        tft.text((30, 50 + i * 30), option, color, sysfont, 2)  # El último "2" es el tamaño del texto
# Función para navegar por el menú
def navigate_menu():
    global current_option
    if button_up.value():
        current_option = (current_option - 1) % len(menu_options)
        time.sleep(0.2)  # Evitar múltiple detección del botón
    elif button_down.value():
        current_option = (current_option + 1) % len(menu_options)
        time.sleep(0.2)  # Evitar múltiple detección del botón

# Función para seleccionar una opción del menú
def select_option():
    if button_select.value():
        return menu_options[current_option]
    return None

# Función principal de la interfaz de selección de juegos
def game_selector():
    while True:
        display_menu(current_option)
        navigate_menu()
        game = select_option()
        if game:
            return game
        time.sleep(0.1)

# Función para iniciar el juego Snake
def snake_game():
    tft.fill(BLACK)

    button_up = Pin(36, Pin.IN, pull=Pin.PULL_DOWN)
    button_down = Pin(35, Pin.IN, pull=Pin.PULL_DOWN)
    button_left = Pin(33, Pin.IN, pull=Pin.PULL_DOWN)
    button_right = Pin(34, Pin.IN, pull=Pin.PULL_DOWN)

    # Función para dibujar un rectángulo (cuadrado de la serpiente o comida)
    def draw_rect(x, y, color):
        tft.fillrect((x, y), (GRID_SIZE, GRID_SIZE), color)

    # Función para generar comida en una posición aleatoria
    def generate_food():
        food_x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        food_y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        return (food_x, food_y)

    # Posición inicial de la serpiente
    snake = [(64, 80), (56, 80), (48, 80)]  # Lista de segmentos de la serpiente (x, y)
    direction = (GRID_SIZE, 0)  # La serpiente empieza moviéndose a la derecha

    # Generar la primera comida
    food = generate_food()

    # Variables de control
    game_over = False

    # Función para verificar colisiones
    def check_collision(new_head):
        x, y = new_head
        # Colisión con los bordes
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            return True
        # Colisión con el cuerpo
        if new_head in snake:
            return True
        return False

    # Bucle principal del juego
    while not game_over:
        # Borra la pantalla
        tft.fill(BLACK)

        # Dibuja la serpiente
        for segment in snake:
            draw_rect(segment[0], segment[1], GREEN)

        # Dibuja la comida
        draw_rect(food[0], food[1], RED)

        # Mueve la serpiente
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        # Verificar colisiones
        if check_collision(new_head):
            game_over = True
            break

        # Añadir nueva cabeza
        snake = [new_head] + snake

        # Verificar si ha comido comida
        if new_head == food:
            food = generate_food()  # Generar nueva comida
        else:
            snake.pop()  # Eliminar la cola si no ha comido
            
        # Lectura de botones para cambiar dirección
        if button_up.value() and direction != (0, GRID_SIZE):  # Evitar que la serpiente se mueva hacia atrás
            direction = (0, -GRID_SIZE)
        elif button_down.value() and direction != (0, -GRID_SIZE):
            direction = (0, GRID_SIZE)
        elif button_left.value() and direction != (GRID_SIZE, 0):
            direction = (-GRID_SIZE, 0)
        elif button_right.value() and direction != (-GRID_SIZE, 0):
            direction = (GRID_SIZE, 0)

        # Pequeño retraso
        time.sleep(0.1)

        # Aquí puedes agregar controles para cambiar la dirección (ejemplo con botones o potenciómetros)
        # Por ejemplo: si se presiona un botón, puedes cambiar la variable `direction`

    # Mostrar mensaje de fin de juego
    tft.fill(BLACK)
    tft.text((10, 70), "GAME OVER", RED, None, 2)

# Función para iniciar el juego Pong
def pong_game():
    # Dimensiones del juego
    PADDLE_WIDTH = 4
    PADDLE_HEIGHT = 20
    BALL_SIZE = 5

    # Posiciones iniciales
    paddle1_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
    paddle2_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
    ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2

    # Velocidades iniciales
    ball_speed_x = 10
    ball_speed_y = 10
    paddle_speed = 8

    button_p1_up = Pin(33, Pin.IN, pull=Pin.PULL_DOWN)
    button_p1_down = Pin(35, Pin.IN, pull=Pin.PULL_DOWN)
    button_p2_up = Pin(34, Pin.IN, pull=Pin.PULL_DOWN)
    button_p2_down = Pin(36, Pin.IN, pull=Pin.PULL_DOWN)

    # Bucle principal del juego Pong
    while True:
        tft.fill(BLACK)
        tft.fillrect((2, paddle1_y), (PADDLE_WIDTH, PADDLE_HEIGHT), WHITE)
        tft.fillrect((SCREEN_WIDTH - PADDLE_WIDTH - 2, paddle2_y), (PADDLE_WIDTH, PADDLE_HEIGHT), WHITE)
        tft.fillrect((ball_x, ball_y), (BALL_SIZE, BALL_SIZE), WHITE)

        ball_x += ball_speed_x
        ball_y += ball_speed_y

        if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
            ball_speed_y *= -1

        if ball_x <= PADDLE_WIDTH + 2 and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT:
            ball_speed_x *= -1
        elif ball_x >= SCREEN_WIDTH - PADDLE_WIDTH - BALL_SIZE - 2 and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT:
            ball_speed_x *= -1

        if ball_x <= 0 or ball_x >= SCREEN_WIDTH - BALL_SIZE:
            ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_speed_x = random.choice([-10, 10])
            ball_speed_y = random.choice([-10, 10])

        if button_p1_up.value() and paddle1_y > 0:
            paddle1_y -= paddle_speed
        elif button_p1_down.value() and paddle1_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
            paddle1_y += paddle_speed

        if button_p2_up.value() and paddle2_y > 0:
            paddle2_y -= paddle_speed
        elif button_p2_down.value() and paddle2_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
            paddle2_y += paddle_speed

        time.sleep(0.05)

# Bucle principal que llama al selector y ejecuta el juego
while True:
    selected_game = game_selector()
    if selected_game == "Snake":
        snake_game()  # Inicia Snake
    elif selected_game == "Pong":
        pong_game()  # Inicia Pong
