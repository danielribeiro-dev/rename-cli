from tests.scanner_test import find_files

print(">> Iniciando o teste do scanner...")

# Vamos testar com um caminho que não existe primeiro!
arquivos = find_files("./pasta_teste", ".jpg")

print(f">> Arquivos encontrados: {arquivos}")
