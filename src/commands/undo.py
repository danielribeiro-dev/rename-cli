from pathlib import Path
from src.services.history_service import load_history


def run_undo_command(directory: str):
    """Desfaz a última renomeação executada na pasta informada.

    Lê o arquivo .rename_history.json, reverte cada arquivo ao nome original
    e apaga o histórico ao final para evitar desfazer a mesma operação duas vezes.
    """

    caminho = Path(directory)

    # Carrega o histórico da pasta — retorna lista vazia se não houver nada
    history_data = load_history(caminho)

    if not history_data:
        print("Nenhum histórico encontrado nesta pasta. Nada para desfazer.")
        return

    print("Desfazendo alterações...")

    for item in history_data:
        nome_atual = item["name"]      # Como o arquivo está agora (ex: foto_1.jpg)
        nome_antigo = item["original"] # Como o arquivo era antes (ex: IMG001.jpg)

        arquivo_atual = caminho / nome_atual
        arquivo_antigo = caminho / nome_antigo

        if arquivo_atual.exists():
            # Renomeia de volta ao nome original
            arquivo_atual.rename(arquivo_antigo)
            print(f"Desfeito: {nome_atual} -> {nome_antigo}")
        else:
            # O arquivo pode ter sido movido ou apagado manualmente
            print(f"Arquivo não encontrado, pulando: {nome_atual}")

    # Remove o histórico após o undo para evitar que seja executado duas vezes
    history_file = caminho / ".rename_history.json"
    if history_file.exists():
        history_file.unlink()

    print("\nDesfazer concluído com sucesso!")