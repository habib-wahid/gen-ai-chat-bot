
import getpass
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your key : ")
model = ChatOpenAI(model="gpt-4o-mini")
messages = [
    SystemMessage("Translate the following from English into Bangla"),
    HumanMessage("hi!"),
]
print(model.invoke(messages))