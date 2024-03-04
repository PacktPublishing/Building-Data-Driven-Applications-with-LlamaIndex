from user_onboarding import user_onboarding
from session_functions import load_session, delete_session, save_session
from logging_functions import reset_log
from quiz_UI import show_quiz
from training_UI import show_training_UI
import streamlit as st

def main():
    st.set_page_config(layout="wide")
    st.sidebar.title('P.I.T.S.')
    st.sidebar.markdown('### Your Personalized Intelligent Tutoring System')

    # Check if the user is returning and has opted to take a quiz
    if 'show_quiz' in st.session_state and st.session_state['show_quiz']:
        show_quiz(st.session_state['study_subject'])  # Show the quiz screen immediately
    elif 'resume_session' in st.session_state and st.session_state['resume_session']:
        # If resuming, clear previous content and show the training UI
        st.session_state['show_quiz'] = False  # Ensure quiz is not shown
        show_training_UI(st.session_state['user_name'], st.session_state['study_subject'])
    elif not load_session(st.session_state):
        user_onboarding()  # Show the onboarding screen for new users
    else:
        # For returning users, display options to resume or start a new session
        st.write(f"Welcome back {st.session_state['user_name']}!")
        col1, col2 = st.columns(2)
        if col1.button(f"Resume your study of {st.session_state['study_subject']}"):
            # Mark the session to be resumed and rerun to clear previous content
            st.session_state['resume_session'] = True
            st.rerun()
        if col2.button('Start a new session'):
            delete_session(st.session_state)
            reset_log()
            # Clear session state and rerun for a fresh start
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()
