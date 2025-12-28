from rich import print
from rich.markdown import Markdown
from typing import Annotated, Sequence, TypedDict
from langgraph.graph import StateGraph, START, END, add_messages
from langchain.chat_models import init_chat_model
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

llm = init_chat_model("google_genai:gemini-2.5-flash")


# 1. Definir um meu estado do meu Graph
class Estado(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


# 2. Definir os nodes
def call_llm(state: Estado) -> Estado:
    llm_result = llm.invoke(state["messages"])
    return {"messages": state["messages"] + [llm_result]}


# 3. Construir o Graph
builder = StateGraph(
    Estado, context_schema=None, input_schema=Estado, output_schema=Estado
)

# 4. Adicionar os nodes ao Graph
builder.add_node("call_llm", call_llm)
builder.add_edge(START, "call_llm")
builder.add_edge("call_llm", END)

# 5. Compilar o Graph
graph = builder.compile()

# 6. Usar o Graph
if __name__ == "__main__":
    current_messages: Sequence[BaseMessage] = []
    while True:
        user_input = input("Digite sua mensagem: ")
        print(Markdown("---"))

        if user_input.lower() in {"sair", "exit", "quit"}:
            print("Encerrando o chat. Até mais!")
            print(Markdown("---"))
            break

        human_message = HumanMessage(user_input)
        current_messages += [human_message]
        result = graph.invoke({"messages": current_messages})
        print(Markdown(str(result["messages"][-1].content)))
        print(Markdown("---"))
