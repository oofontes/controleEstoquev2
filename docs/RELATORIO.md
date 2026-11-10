# Relatório — Desenvolvimento Colaborativo com Git e GitHub

**Disciplina:** Design Profissional — Universidade Positivo
**Projeto:** Controle de Estoque (Python)
**Repositório:** https://github.com/USUARIO/controle-estoque  ← *preencher*
**Integrantes:** Eduardo Fontes · João Otero · Pedro Maia

> Rascunho. Trechos entre `[colchetes]` devem ser conferidos/ajustados com o que realmente aconteceu (datas, dificuldades, links e prints).

---

## 1. Sobre o programa

Sistema de terminal para controle de estoque de uma pequena loja. Permite cadastrar, listar e consultar produtos, registrar entradas e saídas (sem permitir estoque negativo), gerar relatório com valor total e itens com estoque baixo, e salvar os dados em `estoque.json` entre execuções.

| Versão | Conteúdo | Data |
|---|---|---|
| 1 | Menu, cadastro, listagem, validações | [dd/mm] |
| 2 | Consulta + entrada/saída (após resolução do conflito) | [dd/mm] |
| 3 | Relatório, persistência em JSON, validações aprimoradas | [dd/mm] |

## 2. Divisão de tarefas

| Etapa | Eduardo Fontes | João Otero | Pedro Maia |
|---|---|---|---|
| 1 – Repositório | Criou o repo, adicionou colaboradores | Clonou e configurou o VS Code | Clonou e configurou o VS Code |
| 2 – Versão 1 | README e `.gitignore` | Menu e cadastro (`main.py`) | Testes e instruções no README |
| 3/4 – Branches | Revisor dos PRs | `feature/consulta` | `feature/movimentacao` |
| 5 – Conflito | Mediou a decisão e revisou | Integrou primeiro (PR aprovado por Pedro); revisou a resolução | Resolveu o conflito localmente e testou |
| 6 – Evolução | `feature/relatorios` + README final | `feature/persistencia` | `fix/validacoes` + teste final integrado |

As responsabilidades foram alternadas: quem criou o repositório também programou depois, e quem programou também revisou o código dos colegas.

## 3. Branches e Pull Requests

| Branch | Autor | PR | Revisor | Conflito? |
|---|---|---|---|---|
| `feature/consulta` | João | #[1] | Pedro | Não |
| `feature/movimentacao` | Pedro | #[2] | João / Eduardo | **Sim — resolvido** |
| `feature/relatorios` | Eduardo | #[3] | João | Não |
| `feature/persistencia` | João | #[4] | Pedro | Não |
| `fix/validacoes` | Pedro | #[5] | Eduardo | Não |

## 4. O conflito e a solução

**Planejamento:** combinamos que João e Pedro partiriam da mesma versão da `main` e cada um adicionaria sua funcionalidade ao menu sem combinar a numeração.

**O que aconteceu:** o PR de `feature/consulta` entrou primeiro. Ao abrir o PR de `feature/movimentacao`, o GitHub indicou conflito em `main.py`. Ao rodar `git merge main` na branch do Pedro, o Git marcou dois trechos:

1. a função `mostrar_menu()` — João adicionou `3 - Consultar produto`; Pedro adicionou `3 - Registrar entrada` e `4 - Registrar saída`;
2. o `if/elif` em `main()` — os dois associaram a opção `"3"` a funções diferentes.

As funções novas (`consultar_produto`, `registrar_entrada`, `registrar_saida`) foram integradas automaticamente, pois ficavam em regiões diferentes do arquivo.

**Causa:** as duas branches alteraram as mesmas linhas a partir do mesmo ponto de origem, e o Git não tem como decidir qual versão é a correta.

**Alternativas analisadas:**

- manter só um lado → perderia uma funcionalidade;
- aceitar os dois lados sem editar → duas opções "3" no menu e um `elif` que nunca seria executado (bug);
- **manter os dois e renumerar** → escolhida.

**Solução adotada:** 3 = Consultar, 4 = Entrada, 5 = Saída. A consulta ficou junto das opções de visualização e a movimentação depois. Removemos manualmente os marcadores `<<<<<<<`, `=======`, `>>>>>>>`, executamos o roteiro de teste (cadastro → entrada → saída inválida → saída válida → consulta → listagem, resultado esperado de 12 unidades) e registramos o commit `Resolve conflito no menu mantendo consulta e movimentacao`. João, autor do outro lado, revisou e aprovou o PR antes do merge.

**Evidências:** (salvas em `docs/evidencias/`)

- `06_pr_com_conflito.png` — aviso de conflito no GitHub
- `07_terminal_conflict.png` — saída de `git merge` e `git status`
- `08_vscode_conflito.png` — trechos conflitantes no VS Code
- `09_teste_pos_resolucao.png` — programa funcionando após a resolução
- `10_pr_resolvido.png` — PR sem conflitos e aprovado
- `11_graph.png` — `git log --oneline --graph --all`

## 5. Dificuldades encontradas

[Ajustar com a experiência real do grupo. Exemplos comuns:]

- [Configurar `user.name`/`user.email` — os primeiros commits apareceram sem vínculo com a conta do GitHub.]
- [Esquecer o `git pull` antes de criar a branch, partindo de uma `main` desatualizada.]
- [Entender quem era "Current" e quem era "Incoming" no VS Code durante o conflito.]
- [Autenticação no push (login pelo navegador / token).]

**Como superamos:** [ex.: criamos a regra "sempre `git switch main` + `git pull` antes de nova branch"; o integrante que já tinha resolvido explicou aos outros.]

## 6. Participação de cada integrante

**Eduardo Fontes** — criou e configurou o repositório, escreveu e manteve o README, implementou o relatório de estoque (`gerar_relatorio`), revisou PRs e conduziu a conversa sobre a solução do conflito.

**João Otero** — implementou o cadastro da versão 1, a consulta de produtos (`consultar_produto`) e a gravação/leitura em JSON (`carregar_dados`, `salvar_dados`); revisou a resolução do conflito.

**Pedro Maia** — implementou entrada e saída de estoque, resolveu o conflito de merge, aprimorou as validações e fez o teste final do programa integrado.

## 7. Conclusão

[2–4 frases do grupo. Ex.:] O trabalho mostrou que o conflito não é um erro de alguém, e sim consequência natural de pessoas mexendo no mesmo código ao mesmo tempo. Usar branches, Pull Requests com revisão e combinar antes quem mexe em cada parte reduziu os problemas na segunda semana, quando três funcionalidades foram integradas sem conflito.
