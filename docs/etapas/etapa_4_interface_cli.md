# Etapa 4: Interface CLI (Command Line Interface)

## O que vamos aprender
- Interação do usuário via terminal.
- Captura de argumentos passados via linha de comando.
- Orquestração: como fazer os nossos serviços (`scanner.py` e `renamer.py`) conversarem entre si baseados no que o usuário digitou.

## Onde entra no sistema
- **Arquivos Alvos:** `src/cli.py`, `src/commands/rename.py` e `src/main.py`
- **Responsabilidade:** `main.py` será a porta de entrada. `cli.py` interpretará os comandos (ex: `rename .jpg foto ./Downloads`) e `commands/rename.py` ditará a ordem das coisas: 1. Busca arquivos, 2. Mostra preview, 3. Pede confirmação, 4. Renomeia.
