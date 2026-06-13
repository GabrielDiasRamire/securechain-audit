import os
import json
import hashlib
from blockchain.blockchain import adicionar_bloco

BASE_DIR = os.path.dirname(__file__)
DOC_DIR = os.path.join(BASE_DIR, "documentos")
HASH_FILE = os.path.join(BASE_DIR, "logs", "hashes_documentos.json")


def calcular_hash_arquivo(caminho):
    sha256 = hashlib.sha256()
    with open(caminho, "rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b""):
            sha256.update(bloco)
    return sha256.hexdigest()


def listar_hashes():
    hashes = {}

    for raiz, _, arquivos in os.walk(DOC_DIR):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            caminho_relativo = os.path.relpath(caminho, DOC_DIR)
            hashes[caminho_relativo] = calcular_hash_arquivo(caminho)

    return hashes


def inicializar_hashes():
    hashes = listar_hashes()

    with open(HASH_FILE, "w") as arquivo:
        json.dump(hashes, arquivo, indent=4)

    adicionar_bloco("Hashes iniciais dos documentos cadastrados")
    print("[OK] Hashes iniciais salvos.")


def verificar_integridade():
    if not os.path.exists(HASH_FILE):
        print("Base de hashes não existe. Inicializando...")
        inicializar_hashes()
        return

    with open(HASH_FILE, "r") as arquivo:
        hashes_antigos = json.load(arquivo)

    hashes_atuais = listar_hashes()

    for arquivo in hashes_atuais:
        if arquivo not in hashes_antigos:
            print(f"[ALERTA] Arquivo incluído: {arquivo}")
            adicionar_bloco(f"Arquivo incluído: {arquivo}")

    for arquivo in hashes_antigos:
        if arquivo not in hashes_atuais:
            print(f"[ALERTA] Arquivo excluído: {arquivo}")
            adicionar_bloco(f"Arquivo excluído: {arquivo}")

    for arquivo in hashes_atuais:
        if arquivo in hashes_antigos:
            if hashes_atuais[arquivo] != hashes_antigos[arquivo]:
                print(f"[ALERTA] Arquivo alterado: {arquivo}")
                adicionar_bloco(f"Arquivo alterado: {arquivo}")

    with open(HASH_FILE, "w") as arquivo:
        json.dump(hashes_atuais, arquivo, indent=4)

    print("[OK] Verificação concluída.")


if __name__ == "__main__":
    print("1 - Inicializar hashes")
    print("2 - Verificar integridade")
    opcao = input("Opção: ")

    if opcao == "1":
        inicializar_hashes()
    elif opcao == "2":
        verificar_integridade()
    else:
        print("Opção inválida.")
