# Etapa 3: Lógica de Renomeação

## O que vamos aprender
- Regras de negócio.
- Validação de conflitos (ex: tentar renomear para um nome que já existe).
- Simulação de operações antes de executá-las de verdade no sistema (Preview).

## Onde entra no sistema
- **Arquivos Alvos:** `src/services/renamer.py` e `src/services/preview_service.py`
- **Responsabilidade:** `renamer.py` é o motor principal. Ele pega os arquivos que o `scanner.py` encontrou, calcula os novos nomes e efetua a renomeação. O `preview_service.py` servirá para mostrar na tela o que vai acontecer, sem alterar nada de fato, para garantir a segurança do usuário.
