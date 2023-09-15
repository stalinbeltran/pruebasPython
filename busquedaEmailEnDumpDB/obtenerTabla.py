import re

def obtenerTabla(sentence):
    # Extract the dynamic text between "[dbo].[" and "]"
    match = re.search(r'\[dbo\]\.\[([^]]+)\]', sentence)

    return match.group(1)

