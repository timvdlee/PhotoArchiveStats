import pickle
from inventorize import ImageExifData

def getData():
    with open('SleutelstamFotoArchief.pkl', 'rb') as file:
        return pickle.load(file)