from src.services.scanner import find_files
from src.services.preview_service import show_preview
from src.services.renamer import execute_rename, generate_rename_task
from src.services.history_service import save_history
from src.core.exceptions import DirectoryNotFound, InvalidExtension
from pathlib import Path


def run_rename_command(extension: str, new_name: str, directory: str):
    """Executa o fluxo completo de renomeação em lote:
    1. Busca os arquivos
    2. Gera as tarefas
    3. Exibe preview
    4. Pede confirmação
    5. Executa e salva histórico
    """

    # Tenta localizar os arquivos — captura erros de pasta ou extensão inválida
    try:
        arquivos_encontrados = find_files(directory, extension)
    except DirectoryNotFound as e:
        print(f"Erro: {e}")
        return
    except InvalidExtension as e:
        print(f"Erro: {e}")
        return

    # Informa o usuário caso nenhum arquivo seja encontrado com a extensão dada
    if not arquivos_encontrados:
        print(f"Nenhum arquivo '{extension}' encontrado em '{directory}'.")
        return

    # Gera as tarefas de renomeação com os novos nomes
    tarefas = generate_rename_task(arquivos_encontrados, new_name)

    # Exibe o preview antes de qualquer alteração real
    print("\n--- Preview das alterações ---")
    show_preview(tarefas)
    print("------------------------------\n")

    # Pede confirmação explícita antes de modificar os arquivos
    confirmacao = input("Deseja continuar com as alterações? (Y/N) ")
    if confirmacao.strip().lower() != "y":
        print("Operação cancelada pelo usuário.")
        return

    # Executa as renomeações no sistema de arquivos
    execute_rename(tarefas)
    print(f"\nSucesso! {len(tarefas)} arquivos renomeados.")

    # Salva o histórico para permitir o undo posterior
    caminho = Path(directory)
    save_history(caminho, tarefas)
