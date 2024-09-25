from machine import Pin, PWM
from time import sleep

# Configuración del buzzer (conectado al pin 15)
buzzer = PWM(Pin(37))

# Notas de la melodía y sus frecuencias en Hz
notes = {
    'B0': 31,
    'C1': 33, 'CS1': 35, 'D1': 37, 'DS1': 39, 'E1': 41, 'F1': 44, 'FS1': 46, 'G1': 49, 'GS1': 52, 'A1': 55, 'AS1': 58, 'B1': 62,
    'C2': 65, 'CS2': 69, 'D2': 73, 'DS2': 78, 'E2': 82, 'F2': 87, 'FS2': 93, 'G2': 98, 'GS2': 104, 'A2': 110, 'AS2': 117, 'B2': 123,
    'C3': 131, 'CS3': 139, 'D3': 147, 'DS3': 156, 'E3': 165, 'F3': 175, 'FS3': 185, 'G3': 196, 'GS3': 208, 'A3': 220, 'AS3': 233, 'B3': 247,
    'C4': 262, 'CS4': 277, 'D4': 294, 'DS4': 311, 'E4': 330, 'F4': 349, 'FS4': 370, 'G4': 392, 'GS4': 415, 'A4': 440, 'AS4': 466, 'B4': 494,
    'C5': 523, 'CS5': 554, 'D5': 587, 'DS5': 622, 'E5': 659, 'F5': 698, 'FS5': 740, 'G5': 784, 'GS5': 831, 'A5': 880, 'AS5': 932, 'B5': 988,
    'C6': 1047, 'CS6': 1109, 'D6': 1175, 'DS6': 1245, 'E6': 1319, 'F6': 1397, 'FS6': 1480, 'G6': 1568, 'GS6': 1661, 'A6': 1760, 'AS6': 1865, 'B6': 1976,
    'C7': 2093, 'CS7': 2217, 'D7': 2349, 'DS7': 2489, 'E7': 2637, 'F7': 2794, 'FS7': 2960, 'G7': 3136, 'GS7': 3322, 'A7': 3520, 'AS7': 3729, 'B7': 3951,
    'C8': 4186, 'CS8': 4435, 'D8': 4699, 'DS8': 4978
}

# Melodía de Star Wars (lista de tuplas: (nota, duración))
melody = [
    ('A4', 500), ('A4', 500), ('F4', 350), ('C5', 150), ('A4', 500), ('F4', 350), ('C5', 150), ('A4', 1000),
    ('E5', 500), ('E5', 500), ('E5', 500), ('F5', 350), ('C5', 150), ('G4', 500), ('F4', 350), ('C5', 150), ('A4', 1000)
]

melody2 = [
    ('E5', 200), ('E5', 200), ('E5', 200), ('C5', 200), ('E5', 200), ('G5', 400),
    ('G4', 400), ('C5', 200), ('G4', 200), ('E4', 400),
    ('A4', 200), ('B4', 200), ('A#4', 200), ('A4', 200),
    ('G4', 200), ('E5', 200), ('G5', 200), ('A5', 400),
    ('F5', 200), ('G5', 200), ('E5', 400), ('C5', 200), ('D5', 200), ('B4', 400)
]

# Función para reproducir la melodía
def play_tone(note, duration):
    if note in notes:
        buzzer.freq(notes[note])
        buzzer.duty(150)  # Ciclo de trabajo al 50%
        sleep(duration / 1000)  # Duración de la nota
        buzzer.duty(0)  # Apagar el sonido
        sleep(0.05)  # Pequeña pausa entre notas

def play_melody(melody):
    for note, duration in melody:
        play_tone(note, duration)

# Reproducir la melodía
play_melody(melody)

# Detener el PWM cuando termine la melodía
buzzer.deinit()
