import re

def is_pure_kannada(text):
    # Check if text contains Kannada Unicode range (0C80-0CFF)
    kannada_pattern = re.compile(r'[\u0C80-\u0CFF]')
    latin_pattern = re.compile(r'[a-zA-Z]')
    
    # Text should contain Kannada characters
    has_kannada = bool(kannada_pattern.search(text))
    # Text should not contain Latin characters
    has_latin = bool(latin_pattern.search(text))
    
    # Return True if text has Kannada and no Latin
    return has_kannada and not has_latin
