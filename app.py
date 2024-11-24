import streamlit as st
import time
from src.helper import get_pdf_text, get_text_chunks, get_vectorstore, get_conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chat_history = response["chat_history"]

    for i, message in enumerate(response["chat_history"]):
        if i % 2 == 0:
            st.write("User: " + message.content)
        else:
            st.write("Bot: " + message.content)

def main():
    st.set_page_config("Information Retrieval")
    st.header("GenAI-Information-Retreival- 🤖")

    user_question = st.text_input("Ask a question about your PDF:")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload your PDF", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                time.sleep(2)
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)
                st.success("Done!")

if __name__ == "__main__":
    main()