from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from rich import print

llm = init_chat_model("google_genai:gemini-2.5-flash")

system_prompt = SystemMessage(
    "Você é um assistente que responde no TOM do Faustão Silva"
    "Seja gentil e use expressões como: 'Ô loco bicho!', 'Misericórdia!', 'Tá pegando fogo, bicho!'"
    "Use gírias e expressões populares brasileiras.")

human_message = HumanMessage("Olá, tudo bem?")

messages = [system_prompt, human_message]

response = llm.invoke(messages)

print(response)