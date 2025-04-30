from collections import defaultdict
import random

# En liten träningstext
text = """
En gång i tiden fanns en liten katt. Katten bodde i ett hus. Katten älskade att sova och drömma.
"""

# Förbered texten
words = text.lower().split()

# Skapa trigram-modell: (ord1, ord2) → [ord3, ord3, ...]
model = defaultdict(list)

for i in range(len(words) - 2):
    key = (words[i], words[i + 1])      # Nyckeln är två ord i rad
    next_word = words[i + 2]            # Ordet som kommer efter dem
    model[key].append(next_word)        # Lägg till i modellen

# Generera text
def generate_text(start_words, length=10):
    word1, word2 = start_words
    result = [word1, word2]
    
    for _ in range(length):
        next_words = model.get((word1, word2))
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        word1, word2 = word2, next_word  # Flytta fram två ord

    return ' '.join(result)

# Exempel: vi startar med "katten bodde"
print(generate_text(("katten", "bodde"), length=10))
