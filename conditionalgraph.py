from langgraph.graph import StateGraph, START,END
from typing import TypedDict

class pehlistate(TypedDict):
    number1: int
    operation: str
    number2: int
    ans:int

def adder(state:pehlistate)->pehlistate:
    state['ans']= state['number1']+state['number2']
    return state
def sub(state:pehlistate)->pehlistate:
    state['ans']= state['number1']-state['number2']
    return state
def decide_nextnode(state:pehlistate)->pehlistate:

     if state["operation"]=="+":
         return "addkarde"
     if state["operation"]=="-":
         return "subkarde"


graph=StateGraph(pehlistate)
graph.add_node("add",adder)
graph.add_node("sub",sub)
graph.add_node("router",lambda pehlistate:pehlistate)

graph.add_edge(START,"router")
graph.add_conditional_edges("router",decide_nextnode,
                            {
                                "addkarde":"add",
                                "subkarde":"sub"
                            })
graph.add_edge("add",END)
graph.add_edge("sub",END)
x=graph.compile()
print(x.invoke(pehlistate(number1=3,operation="+", number2=5,ans=0))
      )

