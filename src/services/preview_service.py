from src.core.models import RenameTask


def show_preview(tasks: list[RenameTask]):
    """Exibe no terminal uma prévia das renomeações que serão feitas, sem alterar nenhum arquivo."""

    for preview in tasks:
        # Mostra apenas o nome do arquivo (sem o caminho completo) para facilitar a leitura
        print(f"{preview.original_path.name} -> {preview.new_path.name}")