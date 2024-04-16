# Criando um script para criar uma criptografia de cifra de cesar
import string

text_cipher = list(input("Digite o texto claro: "))
alphabet = list(string.ascii_lowercase)

def translate_cipher():
  for i in range(len(text_cipher)):
    indice=0
    for j in range(len(alphabet)):
      if alphabet[j] == text_cipher[i]:
        indice = j
      
    if text_cipher[i] == " ":
      continue
    if indice + 3 > len(alphabet):
      count = (indice +3) - len(alphabet)
      text_cipher[i] = alphabet[count]
    else:
      text_cipher[i] = alphabet[indice+3]

translate_cipher()


print("alfabeto::> ", "".join(text_cipher))