import streamlit as st
import os
import tempfile
import time
import PyPDF2
from langchain_groq import ChatGroq
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_objectbox.vectorstores import ObjectBox
from langchain_community.document_loaders import PyPDFDirectoryLoader

from dotenv import load_dotenv
load_dotenv()

## load the Groq And OpenAI Api Key
os.environ['OPEN_API_KEY']=os.getenv("OPENAI_API_KEY")
groq_api_key=os.getenv('GROQ_API_KEY')

st.title("Objectbox VectorstoreDB With Llama3 Demo")

llm=ChatGroq(groq_api_key=groq_api_key,
             model_name="Llama3-8b-8192")

prompt=ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Questions:{input}

    """

)

## Vector Enbedding and Objectbox Vectorstore db
def vector_embedding(pdfloader):

    if "vectors" not in st.session_state:
        st.session_state.embeddings=OpenAIEmbeddings()
        #st.session_state.loader=PyPDFDirectoryLoader("./us_census") ## Data Ingestion
        #st.session_state.docs=st.session_state.loader.load() ## Documents Loading
        st.session_state.docs=pdfloader.load() 
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors=ObjectBox.from_documents(st.session_state.final_documents,st.session_state.embeddings,embedding_dimensions=768)

with st.form("user_inputs"):
    uploaded_files=st.file_uploader("Uplaod a PDF",type="pdf", accept_multiple_files=True)
    #Add Button
    button=st.form_submit_button("Upload document")

    if uploaded_files is not None:
        with st.spinner("loading..."):
            # Create a temporary directory
            with tempfile.TemporaryDirectory() as temp_dir:
                # Save each uploaded file to the temporary directory
                for uploaded_file in uploaded_files:
                    temp_file_path = os.path.join(temp_dir, uploaded_file.name)
                    with open(temp_file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                # Use PyPDFDirectoryLoader to process the temporary directory
                loader = PyPDFDirectoryLoader(temp_dir)
                st.session_state.clear()
                vector_embedding(loader)
                st.write("ObjectBox Database is ready")
                #documents = loader.load()
                #st.write(documents[0])



input_prompt=st.text_input("Enter Your Question From Documents")

if input_prompt:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    start=time.process_time()

    response=retrieval_chain.invoke({'input':input_prompt})

    print("Response time :",time.process_time()-start)
    st.write(response['answer'])

    # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")




