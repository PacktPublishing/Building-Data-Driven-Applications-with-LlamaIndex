import streamlit as st
from slides import Slide, SlideDeck
import json
from openai import OpenAI
from pathlib import Path
from conversation_engine import initialize_chatbot, chat_interface, load_chat_store

def show_training_UI(user_name, study_subject):
    # Load the slide deck
    slide_deck = SlideDeck.load_from_file("cache/slides.json")
    
    # Display title and slide navigation controls
    st.sidebar.markdown("## " + slide_deck.topic)
    current_slide_index = st.sidebar.number_input("Slide Number", min_value=0, max_value=len(slide_deck.slides)-1, value=0, step=1)
    current_slide = slide_deck.slides[current_slide_index]
    if st.sidebar.button("Toggle narration"):
            st.session_state.show_narration = not st.session_state.get('show_narration', False)

    # Displaying slides and narration in the main area
    col1, col2 = st.columns([0.7,0.3],gap="medium")
    with col1:
        st.markdown(current_slide.render(display_narration=st.session_state.get('show_narration', False)), unsafe_allow_html=True)

    # Chatbot integration in the sidebar
    with col2:
        st.header("💬 P.I.T.S. Chatbot")
        st.success(f"Hello {user_name}. I'm here to answer questions about {study_subject}")
        #with st.spinner("Preparing the chatbot..."):
        chat_store = load_chat_store()
        container = st.container(height=600)
        context = current_slide.render(display_narration=False)
        agent = initialize_chatbot(user_name, study_subject, chat_store, container, context)
        chat_interface(agent, chat_store, container)
        
if __name__ == "__main__":
    user_name = "Andrei"  
    study_subject = "ITIL Foundation" 
    show_training_UI(user_name, study_subject)