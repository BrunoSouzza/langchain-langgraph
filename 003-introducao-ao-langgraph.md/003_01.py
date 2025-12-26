from typing import TypedDict
from langgraph.graph import StateGraph
from rich import print

# Definir um meu estado do meu Graph
class State(TypedDict):
    nodes_path: list[str]
    
# Definir os nodes
def node_a(state: State) -> State:
    output_state = State(nodes_path=["A"])
    print("> node_a", f"{state=}", f"{output_state=}")
    return output_state


def node_b(state: State) -> State:
    output_state = State(nodes_path=["B"])
    print("> node_b", f"{state=}", f"{output_state=}")
    return output_state
    
# Construir o Graph    
builder = StateGraph(State)    

# Adicionar os nodes ao Graph
builder.add_node("A", node_a)
builder.add_node("B", node_b)

# Conectar as edges entre os nodes
builder.add_edge("__start__", "A")
builder.add_edge("A", "B")
builder.add_edge("B", "__end__")

# Compilar o Graph
graph = builder.compile()

# Desenhar o Graph em formato PNG
graph.get_graph().draw_mermaid_png(output_file_path="./003-introducao-ao-langgraph.md/003_01_graph.png")
# Imprimir o Graph em formato Mermaid: https://www.mermaidchart.com/play#pako:eNqrVkrOT0lVslJSqgUAFW4DVg
#print(graph.get_graph().draw_mermaid())

print()
response = graph.invoke(State(nodes_path=[]))
print(f"{response=}")
print()

