
import os

def history(query):
    files = os.listdir("temp")
    files = [f.lower() for f  in files]
    results = []
    for word in query.split():
        for file in files:
            if word in file:
                results.append(file)
    return results
