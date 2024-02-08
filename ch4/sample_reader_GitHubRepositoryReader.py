from llama_index import GithubRepositoryReader

github_token = "<your_github_token>" 
owner = "<owner>"
repo = "<repository>"
branch = "main"
documents = GithubRepositoryReader(
    github_token=github_token, 
    owner=owner,
    repo=repo,
    verbose=True,
    ignore_directories=["docs","test"]
).load_data(branch=branch)
