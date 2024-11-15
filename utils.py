
import os
import hashlib
import logging

def configurar_logs(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

def buscar_arquivos(diretorio, extensoes):
    arquivos_encontrados = []
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.endswith(tuple(extensoes)):
                arquivos_encontrados.append(os.path.join(root, file))
    return arquivos_encontrados

def extrai_hash(file):
    BUF_SIZE = 65536
    sha1 = hashlib.sha1()
    try:
        with open(file, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                sha1.update(data)
        return sha1.hexdigest()
    except Exception as e:
        logging.error(f"Erro ao processar arquivo {file}: {str(e)}")
        return None
