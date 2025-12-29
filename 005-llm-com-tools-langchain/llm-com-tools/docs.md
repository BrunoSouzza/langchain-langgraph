Para rodar o LangGraph Studio localmente em mémoria.

Configure o arquivo 
```langgraph.json```

Instale o pacote abaixo para instalar o langgraph cli:
```uv add "langgraph-cli[inmem]"```

Com isso, você terá acesso ao comando abaixo:
```uv run langgraph --help```

Execute o o cmd abaixo:
```uv run langgraph dev --config 005-llm-com-tools-langchain/llm-com-tools/langgraph.json```


