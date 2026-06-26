from src.core.models import RenameTask
from pathlib import Path


def generate_rename_task(file_list: list[Path], new_name: str) -> list[RenameTask]:
    """Gera a lista de tarefas de renomeação a partir dos arquivos encontrados."""

    tasks = []

    # enumerate começa em 1 para que os arquivos fiquem numerados a partir de "1"
    for numero, caminho in enumerate(file_list, start=1):
        extension = caminho.suffix  # Ex: ".jpg"
        texto_nome = f"{new_name}_{numero}{extension}"  # Ex: "foto_1.jpg"
        caminho_final = caminho.with_name(texto_nome)  # Mesmo diretório, nome novo

        tasks.append(RenameTask(original_path=caminho, new_path=caminho_final))

    return tasks


def execute_rename(task: list[RenameTask]):
    """Executa as renomeações físicas no sistema de arquivos."""

    for tarefa in task:
        # Evita sobrescrever um arquivo que já existe com o nome destino
        if tarefa.new_path.exists():
            print(f"Erro: o arquivo '{tarefa.new_path.name}' já existe, pulando.")
            continue

        # Renomeia o arquivo e marca a tarefa como bem-sucedida
        tarefa.original_path.rename(tarefa.new_path)
        tarefa.success = True