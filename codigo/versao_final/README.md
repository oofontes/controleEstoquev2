# Controle de Estoque

Programa em Python, executado no terminal, para controlar o estoque de uma pequena loja:
cadastro de produtos, consulta, entradas e saídas, relatório e gravação dos dados em arquivo.

Trabalho prático de **Design Profissional** — Universidade Positivo — desenvolvido em equipe com Git e GitHub.

## Integrantes

| Nome | GitHub | Principais contribuições |
|---|---|---|
| Eduardo Fontes | @usuario-eduardo | Criação do repositório, README, relatórios de estoque |
| João Otero | @usuario-joao | Consulta de produtos, gravação dos dados em JSON |
| Pedro Maia | @usuario-pedro | Entrada/saída de estoque, melhorias de validação |

## Como executar

Requisito: Python 3.8 ou superior (não usa bibliotecas externas).

```bash
git clone https://github.com/USUARIO/controle-estoque.git
cd controle-estoque
python main.py
```

Os dados são salvos no arquivo `estoque.json` ao sair pela opção **0**, e carregados automaticamente na próxima execução. Esse arquivo está no `.gitignore` porque contém dados locais, não código.

## Funcionalidades

| Opção | Função | Branch de origem |
|---|---|---|
| 1 | Cadastrar produto | `main` (versão 1) |
| 2 | Listar produtos (ordem alfabética) | `main` / `fix/validacoes` |
| 3 | Consultar produto por código ou parte do nome | `feature/consulta` |
| 4 | Registrar entrada de estoque | `feature/movimentacao` |
| 5 | Registrar saída de estoque | `feature/movimentacao` |
| 6 | Relatório: totais, valor do estoque e itens com estoque baixo | `feature/relatorios` |
| 0 | Sair e salvar dados | `feature/persistencia` |

### Validações

- Campos de texto não podem ficar vazios.
- Código: apenas letras e números, até 10 caracteres, sem repetição.
- Quantidade inteira e não negativa; entrada/saída de no mínimo 1 unidade.
- Saída maior que o estoque disponível é recusada.
- Preço maior que zero, aceitando vírgula ou ponto.
- Arquivo de dados corrompido não derruba o programa (inicia vazio com aviso).

## Fluxo de trabalho da equipe

- `main` contém sempre uma versão funcionando.
- Cada funcionalidade é feita em uma branch própria (`feature/...` ou `fix/...`).
- A integração é feita por **Pull Request**, revisado por outro integrante antes do merge.
- Mensagens de commit no imperativo, descrevendo a mudança (ex.: `Adiciona consulta de produtos`).

## Conflito de merge resolvido

Na Etapa 5, `feature/consulta` e `feature/movimentacao` alteraram o mesmo trecho do menu (ambas usaram a opção 3).
A equipe manteve as duas funcionalidades e renumerou o menu: 3 = Consultar, 4 = Entrada, 5 = Saída.
Detalhes e capturas de tela em [`docs/RELATORIO.md`](docs/RELATORIO.md).
