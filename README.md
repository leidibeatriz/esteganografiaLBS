# esteganografiaLBS
Este repositório apresenta uma solução capaz de enviar mensagens escondidas utilizando a técnica de esteganografia,  mais precisamente, esteganografia em imagens utilizando o algoritmo LSB(Least Significant Bit).

Este código é uma API construída usando o FastAPI, que oferece quatro rotas para realizar as seguintes ações:

#/uploadfile: recebe uma imagem e a salva em um diretório especificado. A rota utiliza o método POST e o arquivo é recebido como um objeto da classe UploadFile, utilizando a função assíncrona "create_upload_file".
#/downloadfile: permite ao usuário baixar uma imagem previamente codificada em um diretório especificado. A rota utiliza o método GET e a função assíncrona "download_file" retorna um objeto da classe FileResponse.
#/encoder: permite codificar uma mensagem em uma imagem. A rota utiliza o método GET e chama a função "encode_message" que recebe o caminho da imagem e a mensagem a ser codificada.
#/decoder: permite decodificar uma mensagem previamente codificada em uma imagem. A rota utiliza o método GET e chama a função "decode_message" que recebe o caminho da imagem codificada.
#/limpar_imagens: permite excluir todas as imagens de um diretório específico. A rota utiliza o método GET e chama a função "limpar_imagens" que recebe o caminho do diretório.
#/test_image:
Além disso, o código possui uma rota para testar a classe TestImage, que testa as funções encode_message e decode_message, utilizando a biblioteca unittest. A rota utiliza o método GET e chama a função "test_image" que instancia a classe de teste e executa os testes retornando o resultado em formato JSON.

Os parâmetros e retornos de cada rota estão documentados utilizando as funções de anotação de tipo do Python, o que ajuda na verificação de erros e na compreensão do que cada função faz.

Módulo: esteganografia.py

Este módulo contém funções para processamento de imagens.

Funções:

#encode_message(image_path: str, message: str) -> None:

Esta função recebe o caminho de uma imagem e uma mensagem a ser codificada nessa imagem. A função codifica a mensagem na imagem e salva a imagem no em uma pasta denominada image no mesmo diretório com o nome "encoded.bmp".

Argumentos:

image_path (str): caminho da imagem a ser codificada
message (str): mensagem a ser codificada na imagem
Retorno:
Menssagem codificada na imagem

Exceções:
ValueError: se a mensagem for maior do que a capacidade da imagem para armazenamento de bits.

#decode_message(image_path: str) -> str:

Esta função recebe o caminho de uma imagem que contém uma mensagem codificada. A função decodifica a mensagem da imagem e a retorna como uma string.

Argumentos:

image_path (str): caminho da imagem com a mensagem codificada
Retorno:
str: mensagem decodificada

Exceções:

ValueError: se a mensagem não terminar com um ponto.

#limpar_imagens(diretorio: str) -> None:

Esta função recebe o caminho de um diretório e remove todos os arquivos com as extensões ".jpg", ".bmp", ".png" ou ".jpeg" contidos nesse diretório.

Argumentos:
diretorio (str): caminho do diretório contendo os arquivos a serem removidos
Retorno:
Arquivos de imagem foram limpos com sucesso.
