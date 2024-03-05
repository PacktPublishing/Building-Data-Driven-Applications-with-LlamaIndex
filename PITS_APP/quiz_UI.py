import streamlit as st
import pandas as pd
from global_settings import QUIZ_FILE

def show_quiz(topic):
    st.markdown(f"### Let's test your knowledge on {topic} with a quiz:")
    df = pd.read_csv(QUIZ_FILE)
    answers = {}
    for index, row in df.iterrows():
        question = row["Question_text"]
        options = [row["Option1"], row["Option2"], row["Option3"], row["Option4"]]
        answers[row["Question_no"]] = st.radio(question, options, index=None, key=row["Question_no"])

    all_answered = all(answer is not None for answer in answers.values())
    if all_answered:
        if st.button("SUBMIT ANSWERS"):
            score = 0
            for q_no in answers:
                user_answer_text = answers[q_no]
                correct_answer_text = df.loc[df['Question_no'] == q_no, "Correct_answer"].iloc[0]
                if user_answer_text == correct_answer_text:
                    score += 1
            
            max_score = len(df)
            third_of_max = max_score / 3
            level = ""
            if score <= third_of_max:
                level = "Beginner"
            elif third_of_max < score <= 2 * third_of_max:
                level = "Intermediate"
            else:
                level = "Advanced"

            st.write(f"Your score is: {score}/{max_score}")
            st.write(f"Your level of knowledge: {level}")
            return level, score
