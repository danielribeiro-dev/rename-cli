import json
from pathlib import Path
from src.core.models import RenameTask


def save_history(directory: Path, tasks: list[RenameTask]):
    """Salva um registro JSON das renomeações bem-sucedidas na pasta alvo.

    O arquivo gerado é oculto (.rename_history.json) e sobrescreve qualquer
    histórico anterior, garantindo que o undo sempre se refira à última operação.
    """

    history_file = directory / ".rename_history.json"

    history_data = []

    for task in tasks:
        # Só registramos as tarefas que foram realmente executadas com sucesso
        if task.success:
            task_dict = {
                "original": task.original_path.name,  # Nome antes da renomeação
                "name": task.new_path.name,            # Nome depois da renomeação
            }
            history_data.append(task_dict)

    # Grava a lista de dicionários no arquivo JSON com indentação para leitura humana
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(history_data, f, indent=4)


def load_history(directory: Path) -> list[dict]:
    """Lê e retorna o histórico salvo na pasta informada.

    Retorna uma lista vazia se o arquivo não existir ou estiver corrompido,
    evitando que o programa quebre em casos de erro.
    """

    history_file = directory / ".rename_history.json"

    # Se não há histórico salvo, retorna lista vazia (nada para desfazer)
    if not history_file.exists():
        return []

    try:
        content = history_file.read_text(encoding="utf-8")
        return json.loads(content)  # Converte a string JSON em lista de dicionários
    except json.JSONDecodeError:
        # Arquivo existe mas está corrompido — tratamos como se não houvesse histórico
        return []