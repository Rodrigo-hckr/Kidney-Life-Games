# games/trivia.py
import random

questions = [
    {"question": "¿Qué función principal tienen los riñones?", "answer": "Filtrar la sangre"},
    {"question": "¿Cuál es un síntoma común de insuficiencia renal?", "answer": "Fatiga"},
    {"question": "¿Qué alimento es bajo en fósforo?", "answer": "Manzana"},
    {"question": "¿Qué líquido es vital para la salud renal?", "answer": "Agua"},
]

def get_random_question():
    return random.choice(questions)
