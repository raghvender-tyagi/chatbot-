from langgraph.graph import StateGraph,START,END
from typing import TypedDict



class bmistate(TypedDict):
    w:float
    h:int
    bmi:float
    cat:str

def calbmi(state:bmistate)->bmistate:
    w=state['w']
    h=state['h']
    bmi=w/(h*h)


def lable(state:bmistate)->bmistate:
    if

graph=StateGraph(bmistate)
graph.add_node("calbmi",calbmi) #at the end eveyr node is just a pythin function
graph.add_node("lable",lable)
graph.add_edge(START,"calbmi")
graph.add_edge("calbmi",END)

workflow=graph.compile()
result = workflow.invoke({"w": 70, "h": 1.75, "bmi": 0})
print(result)