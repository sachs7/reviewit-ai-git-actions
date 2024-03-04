# ReviewIt-AI GitHub Actions

The code is based on [ReviewIt-AI](https://github.com/sachs7/reviewit-ai) - which is a Streamlit based application.

Making a GitHub action from the above repository made sense to use it for personal projects and also it helped to learn about GitHub actions along with the application. 

## Structure

GitHub Actions need `.github` directory within which we will provide `actions` and `workflows` folder. 
The `actions` folder holds the actions or scripts that can be called multiple times, the `workflows` is where the actual `yml` files reside which will call the actions to be performed on given conditions like reviewing the PRs, commenting on issues etc.

## Things to remember

- Make sure to generate the [PAT token](https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
  - Provide required permissions to it, like either to a specifc repo or all repo and other fine-grained permissions
- Goto your repository where you want to enable the GitHub Actions
- In the repo Settings >> Actions >> provide necessary permissions for the workflows (check 'Workflow permissions' section)
- Add your `PAT token` as well as the `OPENAI_API_KEY` in the repo's secrets
  **Note: In the current repo, the secrets are dummy, so, the GitHub Actions on any new PRs will fail**


## How to Run

- Make sure to follow above steps for your repositories
- Copy the `.github` folder contents to your repositories
- Create a PR and see the action!

## Sample PR Reviews from `ReviewIt-AI`

- Code that can be imporved - [Comment](https://github.com/sachs7/reviewit-ai-git-actions/pull/31#issuecomment-1977448710)

- A more better code - [Comment](https://github.com/sachs7/reviewit-ai-git-actions/pull/32#issuecomment-1977451877)
