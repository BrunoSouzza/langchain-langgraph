## 1. Inicializar o projeto Python com `uv`

```bash
uv init
```

Isso cria automaticamente:
* `.python-version`
* `pyproject.toml`
* Estrutura básica do projeto

Exemplo de estrutura:
```
meu-projeto/
├── pyproject.toml
├── .python-version
└── README.md
```

---

## 2. Criar e usar o ambiente virtual

O `uv` gerencia o virtualenv para você.

```bash
uv venv
```

Ativar o ambiente:
### Windows

```powershell
.venv\Scripts\activate
```

---

## 3. Instalar dependências

### Instalar e registrar no `pyproject.toml`

```bash
uv add fastapi uvicorn
```

### Dependências de desenvolvimento

```bash
uv add --dev pytest black ruff
```

O `uv`:

* Resolve dependências rapidamente
* Atualiza o `pyproject.toml`
* Mantém o lock consistente

---

## 6. Executar scripts ou aplicações

Exemplo com FastAPI:

```bash
uv run uvicorn app.main:app --reload
```

Ou rodar qualquer comando dentro do ambiente:

```bash
uv run python main.py
```

---

## 7. Estrutura recomendada (exemplo FastAPI)

```
meu-projeto/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
├── pyproject.toml
└── .venv/
```

---

## 8. Principais comandos do `uv`

| Comando           | Descrição               |
| ----------------- | ----------------------- |
| `uv init`         | Inicializa o projeto    |
| `uv venv`         | Cria virtualenv         |
| `uv add <pkg>`    | Adiciona dependência    |
| `uv remove <pkg>` | Remove dependência      |
| `uv run <cmd>`    | Executa comando no venv |
| `uv pip install`  | Compatível com pip      |

---

## Quando usar `uv`

* Projetos FastAPI
* Containers Docker
* Ambientes CI/CD
* Substituir `pip`, `pip-tools`, `poetry` ou `virtualenv`

Se quiser, posso:

* Montar um **template completo FastAPI + uv**
* Criar um **Dockerfile otimizado com uv**
* Comparar **uv vs poetry vs pip-tools** para seu cenário DevOps
