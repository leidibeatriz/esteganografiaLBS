from PIL import Image
import os 

def encode_message(image_path, message):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    message += "." # Adiciona um ponto no final da mensagem
    binary_message = ''.join(format(ord(i), '08b') for i in message) # Converte a mensagem em uma string binária
    if len(binary_message) > width * height: # Verifica se a mensagem cabe na imagem
        raise ValueError("Mensagem é muito grande para a imagem")
    binary_message += '0' * (width * height - len(binary_message)) # Preenche o restante da imagem com zeros
    index = 0
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            if index < len(binary_message):
                pixels[i, j] = (r & 0b11111110 | int(binary_message[index]), g, b)
                index += 1
    img.save('image/encoded.bmp')

def decode_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    binary_message = ""
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            binary_message += str(r & 1)
            if len(binary_message) % 8 == 0 and binary_message[-8:] == '00000000': # Verifica se chegou ao fim da mensagem
                message = "".join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message)-8, 8)]) # Converte a string binária em uma string de caracteres
                if message[-1] == ".": # Verifica se a mensagem termina com um ponto
                    return message[:-1] # Retorna a mensagem sem o ponto final
                else:
                    raise ValueError("Mensagem não termina com um ponto")
                return message
    raise ValueError("Não foi possível recuperar a mensagem")


def limpar_imagens(diretorio: str):
    for arquivo in os.listdir(diretorio):
        extensao = os.path.splitext(arquivo)[1]
        if extensao.lower() in ('.jpg', '.bmp', '.png', '.jpeg'):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            os.remove(caminho_arquivo)