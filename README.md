<div align="center">

#  Rename CLI

**Renomeação inteligente de arquivos em lote via linha de comando**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Estável-brightgreen?style=for-the-badge)]()

</div>

---

##  Sobre o projeto

O **Rename CLI** é uma ferramenta de linha de comando desenvolvida em Python que permite renomear arquivos em lote de forma rápida, segura e organizada.

Você aponta uma pasta, informa a extensão e o novo nome base — a ferramenta cuida do resto: ela mostra uma **prévia das alterações**, pede sua **confirmação** antes de qualquer mudança e ainda permite **desfazer** a operação caso você mude de ideia.

###  Funcionalidades

-  **Busca recursiva** — localiza arquivos em pastas e subpastas automaticamente
-  **Preview antes de agir** — exibe todas as renomeações antes de executar
-  **Confirmação obrigatória** — nenhum arquivo é alterado sem sua aprovação
-  **Desfazer (undo)** — reverte a última operação com um único comando
-  **Tratamento de erros** — alertas claros para pasta inexistente, extensão inválida e conflitos de nome
-  **Sem dependências externas** — funciona apenas com a biblioteca padrão do Python

---

##  Demonstração

```
user:~$ rename .jpg foto -d ./minhas-fotos/

--- Preview das alterações ---
IMG001.jpg → foto_1.jpg
IMG002.jpg → foto_2.jpg
IMG003.jpg → foto_3.jpg
------------------------------

Deseja continuar com as alterações? (Y/N) Y

Sucesso! 3 arquivos renomeados.
```

---

##  Instalação

### Pré-requisitos

- **Python 3.10** ou superior
- **pip** (gerenciador de pacotes do Python)
- **Git** (para clonar o repositório)

---

###  Linux

#### 1. Verifique se o Python está instalado

```bash
python3 --version
```

Caso não tenha o Python, instale via apt (Ubuntu/Debian):

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

#### 2. Clone o repositório

```bash
git clone https://github.com/seu-usuario/rename-cli.git
cd rename-cli
```

#### 3. (Opcional) Crie um ambiente virtual

Recomendado para isolar as dependências do projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 4. Instale o projeto

```bash
pip install -e .
```

#### 5. Confirme a instalação

```bash
rename --help
```

Se o comando for reconhecido, a instalação foi bem-sucedida! 

---

###  Windows

#### 1. Instale o Python

Baixe o instalador em [python.org/downloads](https://www.python.org/downloads/).

> ⚠️ **Importante:** Durante a instalação, marque a opção **"Add Python to PATH"** antes de clicar em _Install Now_.

Após instalar, abra o **Prompt de Comando (cmd)** ou o **PowerShell** e verifique:

```powershell
python --version
```

#### 2. Clone o repositório

```powershell
git clone https://github.com/seu-usuario/rename-cli.git
cd rename-cli
```

> Caso não tenha o Git, baixe em [git-scm.com](https://git-scm.com/download/win).

#### 3. (Opcional) Crie um ambiente virtual

```powershell
python -m venv .venv
.venv\Scripts\activate
```

#### 4. Instale o projeto

```powershell
pip install -e .
```

#### 5. Confirme a instalação

```powershell
rename --help
```

> ⚠️ **Atenção no Windows:** O Windows possui um comando nativo chamado `rename` (ou `ren`). Caso haja conflito, prefira executar via `python -m src.main` ou utilize o ambiente virtual ativado.

---

##  Como usar

### Comando principal — renomear arquivos

```bash
rename <extensão> <novo_nome> [-d <diretório>]
```

| Argumento       | Descrição                                              | Obrigatório |
|-----------------|--------------------------------------------------------|-------------|
| `<extensão>`    | Extensão dos arquivos a renomear (ex: `.jpg`, `.png`) | ✅ Sim      |
| `<novo_nome>`   | Nome base para os arquivos renomeados (ex: `foto`)    | ✅ Sim      |
| `-d <diretório>`| Pasta onde a operação será executada                   | ❌ Não (padrão: pasta atual) |

---

### Exemplos práticos

#### Renomear imagens JPG na pasta atual

```bash
rename .jpg foto
```

**Resultado:**
```
IMG001.jpg → foto_1.jpg
IMG002.jpg → foto_2.jpg
IMG003.jpg → foto_3.jpg
```

---

#### Renomear documentos PDF em uma pasta específica

```bash
rename .pdf contrato -d ./documentos/
```

**Resultado:**
```
arquivo_antigo.pdf   → contrato_1.pdf
relatorio_2023.pdf   → contrato_2.pdf
```

---

#### Renomear arquivos de áudio em caminho absoluto

```bash
rename .mp3 musica -d /home/usuario/Musicas/
```

---

### Comando undo — desfazer a última renomeação

```bash
rename undo [-d <diretório>]
```

Reverte **a última operação** executada na pasta informada.

```bash
# Desfaz na pasta atual
rename undo

# Desfaz em uma pasta específica
rename undo -d ./documentos/
```

**Resultado:**
```
Desfazendo alterações...
Desfeito: contrato_1.pdf → arquivo_antigo.pdf
Desfeito: contrato_2.pdf → relatorio_2023.pdf

Desfazer concluído com sucesso!
```

> ⚠️ **Atenção:** O undo só pode ser executado **uma vez** por operação. Após desfazer, o histórico é apagado automaticamente.

---

##  Estrutura do projeto

```
rename-cli/
│
├── src/
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── cli.py               # Interpretação dos argumentos do terminal
│   │
│   ├── commands/
│   │   ├── rename.py        # Fluxo completo de renomeação
│   │   └── undo.py          # Fluxo de desfazer operações
│   │
│   ├── services/
│   │   ├── scanner.py       # Localização de arquivos por extensão
│   │   ├── renamer.py       # Geração e execução das renomeações
│   │   ├── preview_service.py  # Exibição da prévia das alterações
│   │   └── history_service.py  # Salvamento e leitura do histórico
│   │
│   └── core/
│       ├── models.py        # Estruturas de dados (dataclasses)
│       ├── exceptions.py    # Exceções personalizadas
│       └── constants.py     # Constantes globais
│
├── tests/                   # Testes automatizados
├── docs/                    # Documentação e contexto do projeto
├── logs/                    # Registros de operações
├── pyproject.toml           # Configuração e metadados do projeto
└── requirements.txt         # Dependências externas
```

---

##  Arquitetura

O projeto segue um fluxo unidirecional de responsabilidades:

```
CLI (cli.py)
    ↓
Commands (rename.py / undo.py)
    ↓
Services (scanner / renamer / history / preview)
    ↓
Filesystem
```

Cada camada tem uma responsabilidade bem definida e não depende das camadas acima.

---

## ⚠️ Tratamento de erros

| Situação                              | Comportamento                                     |
|---------------------------------------|---------------------------------------------------|
| Pasta inexistente                     | Mensagem de erro clara, operação cancelada        |
| Extensão sem ponto (ex: `jpg`)        | Erro informando que a extensão deve começar com `.` |
| Arquivo de destino já existe          | O arquivo é pulado, os demais continuam           |
| Nenhum arquivo encontrado             | Aviso ao usuário, sem alterações                  |
| Undo sem histórico disponível         | Mensagem informativa, sem erros críticos          |

---

##  Desenvolvimento local

Para contribuir ou explorar o código, siga os passos de instalação e depois rode os testes:

```bash
# Rodar testes (quando disponíveis)
python -m pytest tests/
```

---

##  Tecnologias utilizadas

- **Python 3.10+** — linguagem principal
- **pathlib** — manipulação de caminhos e arquivos
- **argparse** — interpretação de argumentos do terminal
- **json** — persistência do histórico de operações
- **dataclasses** — modelagem de dados (RenameTask)

---

##  Roadmap

- [x] Busca recursiva de arquivos por extensão
- [x] Preview de alterações antes de executar
- [x] Confirmação obrigatória pelo usuário
- [x] Execução em lote com numeração sequencial
- [x] Salvamento de histórico em JSON
- [x] Comando undo para reverter a última operação
- [ ] Suporte a múltiplas extensões em um único comando
- [ ] Filtro por data de modificação
- [ ] Modo `--dry-run` (preview sem necessidade de confirmação)
- [ ] Logs detalhados de operações
- [ ] Integração como plugin do projeto ORION

---

##  Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

Desenvolvido por **[danielribeiro-dev](https://github.com/seu-usuario)** como projeto de portfólio e estudo de Python.

---

<div align="center">
  <sub>Feito com ☕ e muito <code>pathlib</code></sub>
</div>
