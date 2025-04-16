
import time
from collections import Counter

def frequency_analysis(ciphertext):
    frequency = Counter(ciphertext.replace(" ", "").upper())
    return frequency.most_common()

def decrypt_monoalphabetic(ciphertext):
    frequency_order = frequency_analysis(ciphertext)
    alphabet = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    most_common = [char for char, _ in frequency_order]
    
    key = {most_common[i]: alphabet[i] for i in range(len(most_common))}
    
    decrypted_text = ''
    for char in ciphertext:
        if char.upper() in key:
            decrypted_char = key[char.upper()]
            decrypted_text += decrypted_char if char.isupper() else decrypted_char.lower()
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = ""

start_time = time.time()
decrypted_text = decrypt_monoalphabetic(ciphertext)
end_time = time.time()

print(f'Ciphertext: {ciphertext}')
print(f'Decrypted text: {decrypted_text}')
print(f'Time taken: {end_time - start_time:.6f} seconds')
