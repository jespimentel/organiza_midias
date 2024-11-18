import os
import json
import shutil
import logging
from utils import buscar_arquivos, extrai_hash, configurar_logs

# Carregando configurações
with open("config.json", encoding="utf-8") as config_file:
    config = json.load(config_file)

configurar_logs(config["log_file"])

contador = 0

with open(config["arquivo_json"], encoding="utf-8") as file:
    arquivos_unicos = json.load(file)

print("Aguarde...")

arquivos = buscar_arquivos(config["diretorio_a_examinar_2"], config["extensoes"])

for arquivo in arquivos:
    contador += 1
    hash = extrai_hash(arquivo)
    if hash is None or hash in arquivos_unicos:
        continue

    destino = f"{config['diretorio_destino_novas']}/{contador}_{os.path.basename(arquivo)}"
    try:
        shutil.copy(arquivo, destino)
    except Exception as e:
        logging.error(f"Erro ao copiar arquivo {arquivo} para {destino}: {str(e)}")