# frontend code 
# 


from agent_graph.graph import create_graph, compile_workflow 
server ='ollama'
model ="llama2"
endpoint = None 

iterations = 20

print("Creating graph and compiling workflow")
graph = create_graph(srever=server, model = model , endpoint = endpoint )
workflow = compile_workflow(graph)
print("Workflow compiled and Graph created ")


if __name__ == '__main__':
    verbose = False   





