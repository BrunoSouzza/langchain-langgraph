from rich import print
from pydantic import ValidationError
from langchain.tools import tool, BaseTool
from langchain.chat_models import init_chat_model
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    AIMessage,
    SystemMessage,
    ToolMessage,
)

@tool
def multiply(a: float, b: float) -> float:
    """Multiply a * b and returns the result.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        the resulting float of the equation a * b.
    """

    return a * b

llm = init_chat_model("google_genai:gemini-2.5-flash")

system_message = SystemMessage(
    "You are a helpful assistant."
    "You have access to tools."
    "When the user asks for something that requires a tool, use the tool."
)
human_message = HumanMessage("What is the result of multiplying 6 by 7?")
messages: list[BaseMessage] = [system_message, human_message]
tools: list[BaseTool] = [multiply]
tools_by_name = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools)

llm_response = llm_with_tools.invoke(messages)
messages.append(llm_response)

if isinstance(llm_response, AIMessage) and getattr(llm_response, "tool_calls", None):
    call = llm_response.tool_calls[-1]
    name, args, id_ = call["name"], call["args"], call["id"]

    try:
        content = tools_by_name[name].invoke(args)
        status = "success"
    except (KeyError, IndexError, TypeError, ValidationError, ValueError) as ex:
        content = f"Please, fix the error: {ex}"
        status = "error"

    tool_response_message = ToolMessage(
        content=content, tool_call_id=id_, status=status
    )
    messages.append(tool_response_message)

    llm_response = llm_with_tools.invoke(messages)
    messages.append(llm_response)

print(messages)
