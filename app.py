from classes import Estudiante
from dotenv import load_dotenv

def main():
    estudiante = Estudiante("oscar","garcia","97814966")
    estudiante.save()

    estudiante.update()
    
if __name__ == "__main__":
    load_dotenv()
    main()
