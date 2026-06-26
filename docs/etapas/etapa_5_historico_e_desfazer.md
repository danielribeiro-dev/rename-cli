# Etapa 5: Histórico e Desfazer (Undo)

## O que vamos aprender
- Leitura e escrita de arquivos JSON.
- Persistência de dados simples.
- Reversão de ações executadas no sistema.

## Onde entra no sistema
- **Arquivos Alvos:** `src/services/history_service.py` e `src/commands/undo.py`
- **Responsabilidade:** Toda vez que uma renomeação for executada com sucesso, o `history_service.py` salvará um registro (ex: "IMG001.jpg virou foto1.jpg"). O comando `undo` usará esse registro para fazer exatamente o caminho inverso, renomeando "foto1.jpg" de volta para "IMG001.jpg".
