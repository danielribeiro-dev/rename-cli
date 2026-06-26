import sys
import argparse


def parse_args():
    # Verifica se o primeiro argumento passado é o subcomando "undo"
    if len(sys.argv) > 1 and sys.argv[1] == "undo":

        # Parser específico para o comando undo (não precisa de extension/new_name)
        parser = argparse.ArgumentParser(
            description="Rename CLI - Desfaz a última renomeação"
        )
        parser.add_argument("command")  # Captura a palavra "undo" no namespace
        parser.add_argument(
            "-d", "--dir",
            help="Pasta onde o undo será executado (padrão: pasta atual)",
            default="./"
        )
        return parser.parse_args()

    # Caso contrário, trata como o comando padrão de renomeação
    parser = argparse.ArgumentParser(
        description="Rename CLI - Renomeador de arquivos por diretório",
        usage="rename <extensão> <novo_nome> [-d <diretório>]"
    )
    parser.add_argument("extension", help="Extensão dos arquivos a renomear (ex: .jpg)")
    parser.add_argument("new_name", help="Novo nome base para os arquivos (ex: foto)")
    parser.add_argument(
        "-d", "--dir",
        help="Pasta onde a renomeação será executada (padrão: pasta atual)",
        default="./"
    )

    args = parser.parse_args()

    # Adicionamos o campo command manualmente para o main.py saber qual fluxo executar
    args.command = "run"

    return args