import operator
from typing import Annotated, TypedDict
from typing_extensions import Literal
from langgraph.graph import StateGraph, START, END
from dataclasses import dataclass
from rich import print

# Definir um meu estado do meu Graph
@dataclass
class State:
    nodes_path: Annotated[list[str], operator.add]
    current_number: int = 0


# Definir os nodes
def node_a(state: State) -> State:
    output_state = State(nodes_path=["A"], current_number=state.current_number)
    print("> node_a", f"{state=}", f"{output_state=}")
    return output_state


def node_b(state: State) -> State:
    output_state = State(nodes_path=["B"], current_number=state.current_number)
    print("> node_b", f"{state=}", f"{output_state=}")
    return output_state

def node_c(state: State) -> State:
    output_state = State(nodes_path=["C"], current_number=state.current_number)
    print("> node_c", f"{state=}", f"{output_state=}")
    return output_state


# Função condicional para o Graph
def the_condition(state: State) -> Literal["goes_to_b", "goes_to_c"]:
    if state.current_number > 50:
        return "goes_to_c"
    return "goes_to_b"

# Construir o Graph
builder = StateGraph(State)

# Adicionar os nodes ao Graph
builder.add_node("A", node_a)
builder.add_node("B", node_b)
builder.add_node("C", node_c)

# Conectar as edges entre os nodes
builder.add_edge(START, "A")
# builder.add_conditional_edges("A", the_condition, ["B", "C"])
builder.add_conditional_edges("A", the_condition, {
                                                   "goes_to_b": "B", "goes_to_c": "C"})
builder.add_edge("B", END)
builder.add_edge("C", END)

# Compilar o Graph
graph = builder.compile()

# Desenhar o Graph em formato PNG
graph.get_graph().draw_mermaid_png(
    output_file_path="./003-introducao-ao-langgraph.md/003_02_graph.png"
)
# Imprimir o Graph em formato Mermaid: https://www.mermaidchart.com/play#pako:eNqrVkrOT0lVslJSqgUAFW4DVg
# print(graph.get_graph().draw_mermaid())

print()
response = graph.invoke(State(nodes_path=[]))
print(f"{response=}")
print()


print()
response = graph.invoke(State(nodes_path=[], current_number=60))
print(f"{response=}")
print()
