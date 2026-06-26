# Exceções personalizadas do sistema.
# Usar exceções próprias deixa o código mais expressivo e fácil de depurar,
# pois cada erro tem um nome que descreve exatamente o que aconteceu.


class DirectoryNotFound(Exception):
    """Lançada quando a pasta informada pelo usuário não existe ou não é um diretório."""
    pass


class InvalidExtension(Exception):
    """Lançada quando a extensão informada não começa com ponto (ex: jpg em vez de .jpg)."""
    pass


class HistoryNotFound(Exception):
    """Lançada quando o usuário tenta desfazer uma operação, mas nenhum histórico foi encontrado."""
    pass