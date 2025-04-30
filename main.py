from collections import defaultdict
import random

# text = """
# En gång i tiden fanns en liten katt. Katten bodde i ett hus. Katten älskade att sova och drömma.
# """

""" 
    Skickas "katten": 
        - katten bodde i ett hus. katten bodde i tiden fanns en
        
        1. Tar den första katten och skriver ut följande ord
        2. Stöter sedan på katten igen och börjar då om på första ankomsten i stället för nästa.
        3. Stöter på order "i" och går då tillbaka i texten och hittar den första träffen av det ordet och följer sedan orden därpå
        
        - katten älskade att sova och drömma. SLUT PÅ ORD.
        
        
"""

text = """
    I de västsvenska skogarna finns ett rikt fågelliv som lockar både naturälskare och fågelskådare. Bland de vanligaste arterna hittar vi talgoxen, som med sitt karakteristiska gula bröst och svarta huvud ofta syns vid fågelbordet. Bofinken är en annan välkänd gäst, vars sång hörs tidigt på våren när hanarna markerar sina revir.
    Bland barrträden trivs också den lilla kungsfågeln, Sveriges minsta fågel, som snabbt rör sig mellan grenarna på jakt efter insekter. Koltrasten, med sin mörka fjäderdräkt och vackra sång, är en annan uppskattad invånare i skogarna. Hackspetten, särskilt större hackspett, hörs ofta när den trummar på trädstammar i jakt på insekter.
    Under sommaren kan man även få syn på rödhaken, vars orangeröda bröst gör den lätt att känna igen. I skogsbrynen och längs stigar hoppar ofta nötväckan omkring, och den är känd för sin förmåga att klättra både upp och ner längs trädstammar.
    Dessa fåglar bidrar till den levande och varierade naturupplevelsen som de västsvenska skogarna erbjuder året runt.
"""

words = text.lower().split()


model = defaultdict(list)

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    model[word].append(next_word)

def generate_text(start_word, length=10):
    word = start_word
    result = [word]
    for _ in range(length):
        next_words = model.get(word)
        if not next_words:
            break
        word = random.choice(next_words)
        result.append(word)
    return ' '.join(result)

print(generate_text("fåglar", length=10))