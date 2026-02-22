import streamlit as st
from memory.session_memory import initialize_session, add_message, get_history
from services.gemini_service import generate_response

st.set_page_config(page_title="Bioinformatics AI Assistant")

st.title("🧬 Bioinformatics AI Assistant (Gemini Powered)")

initialize_session()

# Display previous messages
for chat in get_history():
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# User input
user_input = st.chat_input("Ask your bioinformatics question...")

if user_input:
    # Show user message
    add_message("user", user_input)
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing your query..."):
            response = generate_response(get_history())
            st.markdown(response)

    add_message("assistant", response)
