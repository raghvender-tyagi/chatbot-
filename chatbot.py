from langgraph.graph import StateGraph,START,END
from typing import TypedDict
from langchain_core.messages import HumanMessage,AIMessage
import os
from dotenv import  load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain.utilities import SerpAPIWrapper
# search = SerpAPIWrapper(serpapi_api_key="f9c155ec7e629efd8aae6c187c24bb9040806f8db6a5ff7282738920b870660a")
from langchain_core.output_parsers import StrOutputParser
load_dotenv()  # Load .env file
api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)



class agent_state(TypedDict):
    topic: str
    joke:str
    explain:str





def joke_de(state:agent_state)->agent_state:
    prompt=f'generate a joke on topic {state['topic']}'

    state['joke']=llm.invoke(prompt)
    return state
def explain_kar(state:agent_state)->agent_state:
    prompt=f'explain the given joke {state["joke"]}'

    state["explain"]=llm.invoke(prompt)
    return state
graph=StateGraph(agent_state)
graph.add_node('jokede',joke_de)
graph.add_node('explainkar',explain_kar)
graph.add_edge(START,'jokede')
graph.add_edge('jokede','explainkar')
graph.add_edge('explainkar',END)
checkpointer=InMemorySaver()
grp=graph.compile(checkpointer=checkpointer)
config1={"configurable":{"thread_id":"1"}}
grp.invoke({'topic':'lodu lalit'},config=config1)
print(list(grp.get_state_history(config1)) )
