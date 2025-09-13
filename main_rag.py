from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from embeddedvectors import retriver

model=OllamaLLM(

    model="gemma3:1b",
    temperature=0.7,  
    num_predict=1000,  
    base_url="http://localhost:11434",
)

template ="""
you are a professor of political science and
an expert in answering questions about political science
or polity ,here is the context: {context}
here is the Question : {query} answer this
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 
while True:
    query=input("Ask something ( Give e to exit)")
    if query=='e':
        break
    else:
        context=retriver.invoke(query)
        result = chain.invoke({
         "context" : context,
         "query"   : query
        })
        print(result)