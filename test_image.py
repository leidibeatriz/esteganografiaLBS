import unittest
from esteganografia import encode_message, decode_message
from PIL import Image

class TestImage(unittest.TestCase):

    def test_encode_message(self):
        # Cria uma imagem vazia para testar
        img = Image.new('RGB', (100, 100), color='white')
        img_path = 'image/test_encode.bmp'
        img.save(img_path)

        # Codifica uma mensagem na imagem e verifica se a imagem resultante é igual à esperada
        message = 'Testando a codificação de mensagem.'
        encode_message(img_path, message)
        encoded_img = Image.open('image/encoded.bmp')
        self.assertEqual(img.size, encoded_img.size)

    def test_decode_message(self):
        # Decodifica uma mensagem de uma imagem previamente codificada e verifica se a mensagem é igual à esperada
        img_path = 'image/encoded.bmp'
        expected_message = 'Testando a codificação de mensagem.'
        message = decode_message(img_path)
        self.assertEqual(message, expected_message)


if __name__ == '__main__':
    unittest.main()
