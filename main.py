from esteganografia import encode_message
from esteganografia import decode_message
from esteganografia import limpar_imagens
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import unittest
from test_image import TestImage
import os

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # salva a imagem em algum lugar
    caminho_imagem = os.path.join("image", file.filename)
    with open(caminho_imagem, "wb") as buffer:
        buffer.write(await file.read())
    # retorna o caminho da imagem para o usuário
    return {"filepath": caminho_imagem}


@app.get("/downloadfile/")
async def download_file():
    filename = "image/encoded.bmp"
    return FileResponse(filename)

@app.get("/encoder/{image_path}/{message}")
def codifica_menssagem(image_path, message):
    encode_message(image_path, message)
    return {"Menssagem codificada na imagem"}

@app.get("/decoder/{image_path}")
def decodifica_menssagem(image_path):
    decoded_message = decode_message(image_path)
    return decoded_message

@app.get("/limpar_imagens/{diretorio}")
async def limpar_imagens_api(diretorio: str):
    limpar_imagens(diretorio)
    return {"message": "Arquivos de imagem foram limpos com sucesso."}

@app.get("/test_image")
async def test_image():
    # Instancia a classe de teste
    test_runner = unittest.TextTestRunner()
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestImage)
    
    # Executa os testes e retorna o resultado como JSON
    test_result = test_runner.run(test_suite)
    return {"tests_run": test_result.testsRun,
            "failures": len(test_result.failures),
            "errors": len(test_result.errors)}