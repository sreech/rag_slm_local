from pathlib import Path
from langchain_openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain import hub
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# Define the directory path
mydir = Path('C:/Users/0J0795897/Desktop/cdo_calltranscript.txt')
loader = TextLoader(mydir.absolute(), autodetect_encoding=True)
print("instantiated loader")
data = loader.load()
print("splitting text and embedding using gpt4all embeddings")
data[0].metadata = {'keywords': 'some random metadata'}
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(data)
vectorstore = Chroma.from_documents(documents=splits, embedding=GPT4AllEmbeddings())
print("finished the vectorestore")
# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")
llm = client

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def enter_question():
    print("about to invoke the rag_chain")
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    question = input("Enter your prompt: ")
    for chunk in rag_chain.stream(question):
        print(chunk, end="", flush=True)
    print("just finished invoking the rag_chain")
    # cleanup

while True:
    enter_question()

vectorstore.delete_collection()