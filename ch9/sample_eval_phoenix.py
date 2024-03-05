from llama_index.core import (
    SimpleDirectoryReader, 
    VectorStoreIndex, 
    set_global_handler
)
import phoenix as px

px.launch_app()
set_global_handler("arize_phoenix")

documents = SimpleDirectoryReader('files').load_data()
index = VectorStoreIndex.from_documents(documents)
qe = index.as_query_engine()
response1 = qe.query("Tell me about ancient Rome")
response2 = qe.query("Where is the Colosseum?")
print(str(response1)+"\n"+str(response2))

# EVALUATION PART 
# adapted from the examples available on the official Phoenix documentation: https://docs.arize.com/phoenix/

from phoenix.session.evaluation import (
    get_qa_with_reference, 
    get_retrieved_documents
)
from phoenix.trace import DocumentEvaluations, SpanEvaluations
from phoenix.experimental.evals import (
    HallucinationEvaluator,
    QAEvaluator,
    RelevanceEvaluator,
    OpenAIModel,
    run_evals
)
model = OpenAIModel(model="gpt-4-turbo-preview")

retrieved_documents_df = get_retrieved_documents(px.Client())
queries_df = get_qa_with_reference(px.Client())

hallucination_evaluator = HallucinationEvaluator(model)
qa_correctness_evaluator = QAEvaluator(model)
relevance_evaluator = RelevanceEvaluator(model)

hallucination_eval_df, qa_correctness_eval_df = run_evals(
    dataframe=queries_df,
    evaluators=[hallucination_evaluator, qa_correctness_evaluator],
    provide_explanation=True,
)
relevance_eval_df = run_evals(
    dataframe=retrieved_documents_df,
    evaluators=[relevance_evaluator],
    provide_explanation=True,
)[0]

px.Client().log_evaluations(
    SpanEvaluations(
        eval_name="Hallucination", 
        dataframe=hallucination_eval_df),
    SpanEvaluations(
        eval_name="QA Correctness", 
        dataframe=qa_correctness_eval_df),
    DocumentEvaluations(
        eval_name="Relevance", 
        dataframe=relevance_eval_df),
)

input("Press <ENTER> to exit...")
