from src.cli import parse_args
from src.commands.rename import run_rename_command
from src.commands.undo import run_undo_command


def main():
    # Lê e interpreta os argumentos do terminal
    args = parse_args()

    # Roteia para o comando correto com base no que o usuário digitou
    if args.command == "run":
        run_rename_command(args.extension, args.new_name, args.dir)

    elif args.command == "undo":
        run_undo_command(args.dir)


if __name__ == "__main__":
    main()