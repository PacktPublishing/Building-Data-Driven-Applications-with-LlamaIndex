# prepares quizz questions based on the uploaded files

from llama_index.core import load_index_from_storage, StorageContext
from llama_index.program.evaporate.df import DFRowsProgram
from llama_index.program.openai import OpenAIPydanticProgram
from global_settings import INDEX_STORAGE, QUIZ_SIZE, QUIZ_FILE
import pandas as pd

def build_quiz(topic):
    df = pd.DataFrame(
        {
            "Question_no": pd.Series(dtype="int"),
            "Question_text": pd.Series(dtype="str"),
            "Option1": pd.Series(dtype="str"),
            "Option2": pd.Series(dtype="str"),
            "Option3": pd.Series(dtype="str"),
            "Option4": pd.Series(dtype="str"),
            "Correct_answer": pd.Series(dtype="str"),
            "Rationale": pd.Series(dtype="str"),
        }
    )
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_STORAGE)
    vector_index = load_index_from_storage(
        storage_context, index_id="vector"
    )
    df_rows_program = DFRowsProgram.from_defaults(
        pydantic_program_cls=OpenAIPydanticProgram, df=df
    )
    query_engine = vector_index.as_query_engine()
    response = query_engine.query(
        f"Create {QUIZ_SIZE} different quiz questions relevant for testing a candidate's knowledge about {topic}. Each question will have 4 answer options. Questions must be general topic-related, not specific to the provided text. For each question, provide also the correct answer and the answer rationale. The rationale must not make any reference to the provided context, any exams or the topic name. Only one answer option should be correct."
    )
    result_obj = df_rows_program(input_str=response)
    new_df=result_obj.to_df(existing_df=df)
    new_df.to_csv(QUIZ_FILE, index=False)
    return new_df

