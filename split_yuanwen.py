from nltk.tokenize import sent_tokenize

def check_text(text):
    while True:
        while text.startswith(" "):
            text = text[1:]
        while text.startswith("\t"):
            text = text[1:]
        if text[0] not in [" ", "\t"]:
            break
    return text

file = open("yuanwen.txt", mode="r", encoding="utf-8")
lines = file.readlines()
file.close()
file = open("yuanwen_new.txt", mode="w", encoding="utf-8")
for i in range(len(lines)):
    text = lines[i]
    while text.endswith("\n"):
        text = text[:-1]
    if len(text) == 0:
        continue
    text = check_text(text)
    if len(text) == 0:
        continue
    if len(text) <= 300:
        new_text = text
        file.write(new_text)
        file.write("\n\n")
        continue
    sentences = sent_tokenize(text)
    new_text = ""
    for n in range(len(sentences)):
        sentence = sentences[n]
        if n == 0:
            new_text = sentence
            continue
        if len(new_text + " " + sentence) > 300:
            file.write(new_text)
            file.write("\n\n")
            new_text = sentence
        else:
            new_text = new_text + " " + sentence
    file.write(new_text)
    file.write("\n\n")
file.close()
