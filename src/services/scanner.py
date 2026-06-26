from pathlib import Path
from src.core.exceptions import DirectoryNotFound, InvalidExtension


def find_files(folder_path: str, extension: str) -> list[Path]:
    """Localiza todos os arquivos com a extensão informada dentro da pasta."""

    caminho = Path(folder_path)

    # A extensão deve começar com ponto para ser válida (ex: .jpg, .png)
    if not extension.startswith("."):
        raise InvalidExtension("A extensão deve começar com um ponto (.)")

    # Verifica se o caminho existe no sistema de arquivos
    if not caminho.exists():
        raise DirectoryNotFound("A pasta informada não existe!")

    # Verifica se o caminho aponta para uma pasta (e não para um arquivo)
    if not caminho.is_dir():
        raise DirectoryNotFound("O caminho informado não leva a uma pasta!")

    # rglob percorre a pasta e todas as subpastas recursivamente
    return list(caminho.rglob(f"*{extension}"))
