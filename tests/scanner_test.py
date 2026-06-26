from pathlib import Path

def find_files(folder_path: str, extension: str) -> list[Path]:
    """
    Busca arquivos dentro de uma pasta que terminem com a extensão informada.
    """
    # 1. Transformamos a string de texto em um objeto de Caminho (Path)
    caminho = Path(folder_path)
    
    # Se o caminho não existir, deveríamos "quebrar a cara" (dar erro).
    # Como verificamos isso? (Dica: o objeto 'caminho' tem um método chamado .exists())
    if not caminho.exists():
        raise ValueError("A pasta informada não existe!")
    
    if not caminho.is_dir():
        raise ValueError("O caminho fornecido não leva a uma pasta!")   

    # Vamos retornar uma lista vazia por enquanto
    return list(caminho.rglob(f"*{extension}"))
