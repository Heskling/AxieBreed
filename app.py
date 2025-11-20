from fastapi import FastAPI, UploadFile
import csv
import random

app = FastAPI()

# Función para leer CSV con genética Axie
def read_axie_csv(file):
    lines = file.decode().splitlines()
    reader = csv.DictReader(lines)
    return list(reader)

# Simulación básica de probabilidades genéticas
def calculate_genetics(axie1, axie2):
    traits = ["Eyes", "Ears", "Back", "Mouth", "Horn", "Tail"]
    result = {}
    
    for trait in traits:
        dominant = random.choice([axie1[trait], axie2[trait]])
        recessive = random.choice([axie1[trait], axie2[trait]])
        
        result[trait] = {
            "Dominant": dominant,
            "Recessive": recessive
        }

    return result

@app.post("/calculate/")
async def calculate(file1: UploadFile, file2: UploadFile):
    axie1 = read_axie_csv(await file1.read())[0]
    axie2 = read_axie_csv(await file2.read())[0]

    result = calculate_genetics(axie1, axie2)

    return {
        "Parents": {
            "Axie 1": axie1,
            "Axie 2": axie2
        },
        "Offspring Prediction": result
    }
