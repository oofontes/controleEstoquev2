# Controle de Estoque

Programa em Python, executado no terminal, para controlar o estoque de uma pequena loja.
Trabalho prático de **Design Profissional** — Universidade Positivo.

## Integrantes

| Nome | GitHub |
|---|---|
| Eduardo Fontes | @usuario-eduardo |
| João Otero | @usuario-joao |
| Pedro Maia | @usuario-pedro |

## Como executar

Requisito: Python 3.8 ou superior (não usa bibliotecas externas).

```bash
python main.py
```

## Funcionamento (versão 1)

O programa mostra um menu em laço até o usuário escolher **0 - Sair**.

| Opção | Função |
|---|---|
| 1 | Cadastrar produto (código, nome, quantidade e preço) |
| 2 | Listar produtos cadastrados |
| 0 | Sair |

### Validações

- Campos de texto não podem ficar vazios.
- O código do produto não pode se repetir.
- A quantidade deve ser um número inteiro maior ou igual a zero.
- O preço deve ser um número maior que zero (aceita vírgula ou ponto).
- Opções inexistentes no menu exibem mensagem de erro.
