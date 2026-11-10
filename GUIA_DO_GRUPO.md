# Guia do grupo — Controle de Estoque com Git e GitHub

**Equipe:** Eduardo Fontes · João Otero · Pedro Maia

Este guia diz **quem faz o quê, em que ordem, com quais comandos** e **quais prints tirar**.
O código de cada etapa já está pronto e testado na pasta `codigo/`. O conflito da Etapa 5 foi simulado e acontece exatamente como descrito aqui.

> **Importante:** cada um precisa executar a sua parte **na própria máquina e com a própria conta do GitHub**. O professor avalia o histórico (quem fez cada commit) e pode fazer perguntas individuais. Leiam a seção "O que dizer se o professor perguntar" no final.

---

## Visão geral

| Etapa | Quem | Branch | O que entra |
|---|---|---|---|
| 1 | Eduardo | `main` | Repositório, README, `.gitignore` |
| 2 | Todos | `main` | Versão 1: menu, cadastro, listagem |
| 3–4 | João | `feature/consulta` | Opção 3 – Consultar produto |
| 3–4 | Pedro | `feature/movimentacao` | Opções 3/4 – Entrada e saída |
| 5 | João + Pedro (Eduardo revisa) | `main` | **Conflito** no menu e resolução |
| 6 | Eduardo | `feature/relatorios` | Opção 6 – Relatório |
| 6 | João | `feature/persistencia` | Salvar/carregar `estoque.json` |
| 6 | Pedro | `fix/validacoes` | Valida código, limita nome, lista em ordem |
| Final | Todos | — | Relatório, prints, apresentação |

Repare que os papéis giram: Eduardo cria o repo e depois programa; João e Pedro programam e depois revisam PRs uns dos outros.

---

## Antes de começar (os três)

1. Instalar **Git**, **Python 3** e **VS Code** (com a extensão Python).
2. Configurar a identidade — isso é o que aparece no histórico:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "email-da-sua-conta-github@exemplo.com"
```

3. Criar uma pasta `evidencias/` no computador para guardar os prints (nomes sugeridos abaixo).

---

## Etapa 1 — Criação do repositório (Eduardo)

1. No GitHub: **New repository** → nome `controle-estoque` → público → marcar *Add a README file* → **Create**.
2. **Settings → Collaborators → Add people**: adicionar João e Pedro (eles aceitam o convite por e-mail).
3. Os três clonam:

```bash
git clone https://github.com/USUARIO-EDUARDO/controle-estoque.git
cd controle-estoque
code .
```

> **Remoto x local:** o repositório no GitHub (`origin`) é a cópia compartilhada. O `git clone` cria uma cópia **local** completa no computador de cada um. Nada que você faça localmente aparece para os colegas até você dar `git push`; nada que eles enviarem aparece para você até você dar `git pull` (ou `fetch` + `merge`).

📸 `01_repositorio_criado.png` (página do repo) · `02_colaboradores.png` (Settings → Collaborators)

---

## Etapa 2 — Primeira versão (todos, direto na `main`)

Divisão sugerida para que **os três tenham commits** já na v1:

| Quem | Faz | Mensagem do commit |
|---|---|---|
| Eduardo | Copia `codigo/etapa2_v1/.gitignore` e `README.md` | `Adiciona README e gitignore do projeto` |
| João | Copia `codigo/etapa2_v1/main.py` (funções de leitura + cadastro) | `Implementa menu e cadastro de produtos` |
| Pedro | Revisa, testa e completa o README (seção Validações, se faltou algo) | `Atualiza instrucoes de execucao` |

Cada um, na sua vez:

```bash
git pull                 # pega o que o colega anterior enviou
# ... copia/edita os arquivos ...
python main.py           # testa
git status
git add .
git commit -m "Mensagem do commit"
git push
```

**Editar os nomes de usuário do GitHub** na tabela de integrantes do README.

Teste mínimo da v1: cadastrar um produto, tentar repetir o código (deve dar erro), digitar letra na quantidade (deve pedir de novo), listar, sair.

📸 `03_v1_funcionando.png` (terminal rodando o menu)

---

## Etapas 3 e 4 — Branches e commits (João e Pedro, ao mesmo tempo)

Os dois partem **da mesma `main`** e trabalham **sem se falar sobre o menu** (é isso que vai gerar o conflito de propósito).

### João — `feature/consulta`

```bash
git switch main
git pull
git switch -c feature/consulta
```

Substitua `main.py` pelo de `codigo/etapa3_joao_feature-consulta/main.py`. O que mudou:

- nova função `consultar_produto()` (busca por código exato ou parte do nome, sem diferenciar maiúsculas);
- linha `print("3 - Consultar produto")` no menu;
- `elif opcao == "3": consultar_produto()` no `main()`.

Dica: para o histórico ficar mais rico, façam **2 commits** — primeiro a função, depois o menu.

```bash
python main.py                         # testar a consulta
git add main.py
git commit -m "Implementa consulta de produtos por codigo ou nome"
git push -u origin feature/consulta
```

### Pedro — `feature/movimentacao`

```bash
git switch main
git pull
git switch -c feature/movimentacao
```

Substitua `main.py` pelo de `codigo/etapa3_pedro_feature-movimentacao/main.py`. O que mudou:

- funções `registrar_entrada()` e `registrar_saida()` (a saída não deixa o estoque ficar negativo);
- linhas `3 - Registrar entrada` e `4 - Registrar saída` no menu;
- `elif` para as opções 3 e 4.

```bash
python main.py
git add main.py
git commit -m "Adiciona entrada e saida de estoque"
git push -u origin feature/movimentacao
```

> **Commit ≠ código correto.** O commit só registra um "retrato" das alterações. Os dois commits acima estão corretos isoladamente, mas vão entrar em conflito quando forem juntados.

📸 `04_branches_github.png` (aba *Branches* do repo mostrando as duas)

---

## Etapa 5 — Conflito e resolução (a mais importante)

### 5.1 Integrar a primeira branch (sem conflito)

João abre o **Pull Request** no GitHub: *Compare & pull request* → base `main` ← `feature/consulta`.
Título: `Adiciona consulta de produtos`. Descrição: o que foi feito e como testar.
**Pedro revisa** (aba *Files changed* → *Review changes* → *Approve*) e o João clica **Merge pull request**.

📸 `05_pr_consulta.png`

### 5.2 Integrar a segunda branch (o conflito aparece)

Pedro abre o PR `feature/movimentacao` → `main`. O GitHub mostra:
**"This branch has conflicts that must be resolved"** — conflito em `main.py`.

📸 `06_pr_com_conflito.png` ← **print obrigatório**

Resolver localmente (mais didático e fácil de mostrar):

```bash
git switch main
git pull                              # main agora já tem a consulta do João
git switch feature/movimentacao
git merge main
# CONFLICT (content): Merge conflict in main.py
git status                            # mostra "both modified: main.py"
```

📸 `07_terminal_conflict.png` (saída do `git merge` + `git status`)

Abrir `main.py` no VS Code. Aparecem **dois blocos de conflito**:

```python
<<<<<<< HEAD
    print("3 - Registrar entrada")
    print("4 - Registrar saída")
=======
    print("3 - Consultar produto")
>>>>>>> main
```

e

```python
        elif opcao == "3":
<<<<<<< HEAD
            registrar_entrada()
        elif opcao == "4":
            registrar_saida()
=======
            consultar_produto()
>>>>>>> main
```

(`HEAD` = o que está na branch atual, a do Pedro; o outro lado = o que veio da `main`, do João. A ordem pode aparecer invertida se vocês fizerem o merge no sentido oposto.)

📸 `08_vscode_conflito.png` ← **print obrigatório** (com as cores verde/azul e os botões *Accept Current / Incoming / Both*)

### 5.3 Por que o conflito aconteceu

Os dois partiram da mesma versão e **alteraram as mesmas linhas** do menu: os dois escolheram o número **3** para a sua nova opção. O Git consegue juntar sozinho mudanças em lugares diferentes (as funções novas de cada um entraram sem problema), mas quando as **mesmas linhas** mudaram nos dois lados ele não tem como saber qual é a certa e pede uma decisão humana.

### 5.4 Decisão da equipe (conversar antes de mexer!)

Opções consideradas:

| Opção | Resultado | Decisão |
|---|---|---|
| *Accept Current* (só Pedro) | Perde a consulta do João | ❌ |
| *Accept Incoming* (só João) | Perde entrada/saída do Pedro | ❌ |
| *Accept Both* sem editar | Duas opções "3" no menu e dois `elif opcao == "3"` — o segundo nunca executa | ❌ bug |
| **Manter as duas e renumerar** | 3 = Consultar, 4 = Entrada, 5 = Saída | ✅ |

Justificativa: preserva todas as funcionalidades; a consulta fica junto das opções de visualização (1–3) e a movimentação vem depois (4–5).

### 5.5 Resolver manualmente

Apagar **todas** as linhas `<<<<<<<`, `=======`, `>>>>>>>` e deixar assim:

```python
def mostrar_menu():
    print("\n===== CONTROLE DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Consultar produto")
    print("4 - Registrar entrada")
    print("5 - Registrar saída")
    print("0 - Sair")
```

```python
        elif opcao == "3":
            consultar_produto()
        elif opcao == "4":
            registrar_entrada()
        elif opcao == "5":
            registrar_saida()
```

Arquivo completo de referência: `codigo/etapa5_resolucao_conflito/main.py`.

### 5.6 Testar, registrar e enviar

```bash
python main.py
```

Roteiro de teste (fazer todas as opções): cadastrar `A1 / Caneta / 10 / 2,50` → opção 4 entrada de 5 → opção 5 saída de 20 (deve recusar) → saída de 3 → opção 3 consultar "can" → deve mostrar **12 unidades** → opção 2 listar → 0 sair.

📸 `09_teste_pos_resolucao.png`

```bash
git add main.py
git commit -m "Resolve conflito no menu mantendo consulta e movimentacao"
git push
```

Agora o PR no GitHub mostra **"This branch has no conflicts"**. **João revisa e aprova** (o código dele foi mexido!), Eduardo também comenta, e Pedro faz o merge.

📸 `10_pr_resolvido.png` · `11_graph.png` → saída de `git log --oneline --graph --all`

> Alternativa pelo GitHub: botão **Resolve conflicts** no próprio PR abre um editor web. Funciona igual, mas tirem os prints do mesmo jeito.

---

## Etapa 6 — Evolução (semana seguinte, os três em paralelo)

**Planejamento (registrar no relatório):** reunião rápida para combinar quem mexe onde e evitar outro conflito acidental. Todos partem da `main` atualizada:

```bash
git switch main
git pull
git switch -c NOME-DA-BRANCH
```

| Quem | Branch | Arquivo de referência | O que muda | Commit |
|---|---|---|---|---|
| Eduardo | `feature/relatorios` | `etapa6_eduardo_feature-relatorios/main.py` | Função `gerar_relatorio()` + opção 6 | `Adiciona relatorio de estoque baixo e valor total` |
| João | `feature/persistencia` | `etapa6_joao_feature-persistencia/main.py` | `import json/os`, `carregar_dados()` no início, `salvar_dados()` ao sair | `Salva e carrega produtos em arquivo JSON` |
| Pedro | `fix/validacoes` | `etapa6_pedro_fix-validacoes/main.py` | Código só letras/números (máx. 10), nome até 25 caracteres, listagem em ordem alfabética | `Corrige validacao do codigo e ordena listagem` |

Cada um: testa → `add` → `commit` → `push -u origin ...` → abre PR → **outro integrante revisa** → merge.
Foi testado: integrando nessa ordem (relatórios → persistência → validações) **não há conflito**, porque cada um mexeu em uma região diferente do arquivo. Se o GitHub acusar conflito mesmo assim, resolvam seguindo a Etapa 5.

Depois dos três merges:

1. Um integrante (sugestão: Pedro) faz `git pull`, roda o roteiro de teste completo e confere que o programa final é igual a `codigo/versao_final/main.py`.
2. Eduardo substitui o README pelo de `codigo/versao_final/README.md` → commit `Atualiza README com funcionalidades da versao 3`.
3. Opcional: criar uma *release/tag* `v1.0` no GitHub.

📸 `12_prs_fechados.png` (aba *Pull requests → Closed*) · `13_insights_contributors.png` (*Insights → Contributors*) · `14_programa_final.png`

---

## Entrega final — checklist

- [ ] Link do repositório
- [ ] Código final funcionando (`main.py`)
- [ ] README com descrição, integrantes, execução e funcionalidades
- [ ] Histórico com commits dos **três** (`git log --oneline --graph --all`)
- [ ] Branches: `feature/consulta`, `feature/movimentacao`, `feature/relatorios`, `feature/persistencia`, `fix/validacoes` (não apaguem as branches depois do merge)
- [ ] Pull Requests com revisão de outro integrante
- [ ] Prints do conflito (06, 07, 08) e da resolução (09, 10, 11) → salvar em `docs/evidencias/` no repo
- [ ] `docs/RELATORIO.md` preenchido (rascunho pronto em `docs/`)
- [ ] Apresentação (roteiro em `docs/APRESENTACAO.md`)

---

## Comandos — VS Code x terminal (o que cada um faz)

| Operação | VS Code | Comando | O que faz de verdade |
|---|---|---|---|
| Clonar | Paleta → *Git: Clone* | `git clone URL` | Baixa o repositório inteiro, com histórico, e liga ao remoto `origin` |
| Ver alterações | Painel *Source Control* | `git status` | Mostra arquivos modificados, preparados e a branch atual |
| Criar branch | Seletor de branch (canto inferior) | `git switch -c nome` | Cria uma linha de desenvolvimento nova a partir de onde você está |
| Preparar | Botão **+** | `git add .` | Escolhe o que vai entrar no próximo commit (*staging*) |
| Commit | Mensagem + **Commit** | `git commit -m "..."` | Grava um retrato das alterações preparadas no histórico **local** |
| Buscar remoto | *Fetch* | `git fetch` | Baixa novidades do GitHub **sem** mexer nos seus arquivos |
| Enviar | *Push / Sync* | `git push` | Manda seus commits locais para o GitHub |
| Trocar de branch | Seletor de branch | `git switch nome` | Troca os arquivos da pasta para a versão daquela branch |
| Integrar | Merge / Pull Request | `git merge nome` | Junta o histórico da outra branch na atual |
| Histórico | *Timeline* / Git Graph | `git log --oneline` | Lista os commits |
| Atualizar | *Pull* | `git pull` | `fetch` + `merge` de uma vez |

---

## O que dizer se o professor perguntar

- **Diferença entre commit e push?** Commit grava no histórico local; push envia esses commits para o GitHub.
- **Fetch x pull?** Fetch só baixa as informações do remoto; pull baixa e já integra na branch atual.
- **Para que serve branch?** Desenvolver e testar uma mudança isolada sem quebrar a `main`, que deve sempre funcionar.
- **Por que deu conflito?** As duas branches mudaram as mesmas linhas do menu (as duas usaram a opção 3). O Git não sabe escolher sozinho.
- **Por que não clicaram em "Accept Both"?** Teria duas opções "3" e um `elif` que nunca executa — o programa ficaria com bug. Renumeramos para manter as duas funções.
- **Como sabem que a resolução funcionou?** Rodamos o roteiro de teste completo antes do commit e o colega dono do outro código revisou o PR.
- **Por que `estoque.json` está no `.gitignore`?** É dado gerado na máquina de cada um, não código; versionar causaria conflitos inúteis.
- **Cada um deve saber explicar a própria função** (abrir o código e explicar linha a linha): João → `consultar_produto` e `carregar/salvar_dados`; Pedro → `registrar_entrada/saida` e validações; Eduardo → `gerar_relatorio` e organização do repositório.
