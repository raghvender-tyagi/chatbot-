from langgraph.graph import StateGraph , START,END
from typing import TypedDict

class state(TypedDict):
    msg:str
    changensg:str

def pehla(state:state)->state:
    state['msg']="are teri maa ka bhosda phat ja ga "
    print(state['msg'])
    return state

def change(state:state)->state:
    state['changensg']="hello bhai "
    return state

def show(state:state)-> state:
    print("sun bete ")
    print(state['changensg'])
    return state

graph=StateGraph(state)

graph.add_node("pehla",pehla)
graph.add_node("change",change)
graph.add_node("show",show)
graph.add_edge(START,'pehla')
graph.add_edge('pehla','change')
graph.add_edge('change','show')
graph.add_edge('show',END)

wwork=graph.compile()
print(wwork.invoke({"msg": "lkjshdlkfholi", "changensg": ""}))