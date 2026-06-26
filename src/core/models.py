from dataclasses import dataclass
from pathlib import Path


# RenameTask representa uma única tarefa de renomeação.
# Guarda o caminho original do arquivo, o caminho novo e se a operação teve sucesso.
@dataclass
class RenameTask:
    original_path: Path  # Caminho completo do arquivo antes da renomeação
    new_path: Path       # Caminho completo do arquivo depois da renomeação
    success: bool = False  # Marcado como True após a renomeação ser executada com sucesso