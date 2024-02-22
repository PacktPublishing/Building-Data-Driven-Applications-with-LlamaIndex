from llama_index.readers.github import GithubRepositoryReader

documents = GithubRepositoryReader(
    github_token="<your_github_token>" , 
    owner= "<owner>",
    repo="<repository>",
    branch = "main",
    verbose=True,
    ignore_directories=["docs","test"]
).load_data(branch=branch)
