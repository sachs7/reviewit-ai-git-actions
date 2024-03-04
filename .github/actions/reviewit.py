import os
import click
from github import Github

from ai import get_code_review

# Create a GitHub object using an environment variable for the token
g = Github(os.getenv("GITHUB_TOKEN"))


def get_file_contents(repo_name, pr_number):
    try:
        # Get the repository object
        repo = g.get_repo(repo_name)

        # Get the pull request object
        pr = repo.get_pull(pr_number)

        # Initialize an empty dictionary to store file contents
        file_dict = {}

        # Get the commits from the pull request
        commits = pr.get_commits()

        # Get the files from the commits
        for commit in commits:
            files = commit.files

            # Get the contents of each file
            for file in files:
                filename = file.filename
                contents = repo.get_contents(
                    filename, ref=commit.sha
                ).decoded_content.decode("utf-8")

                # Store the contents of the file
                file_dict[filename] = contents.strip()

        # Return the concatenated file contents
        return "\n".join(file_dict.values())
    except Exception as e:
        click.echo(f"An error occurred while reading commits: {e}", err=True)
        return None


@click.command()
@click.option(
    "--repo-name", "-r", type=str, required=True, help="The name of the repository"
)
@click.option(
    "--pr-number", "-p", type=int, required=True, help="The pull request number"
)
def main(repo_name, pr_number):
    pr_contents = get_file_contents(repo_name, pr_number)
    click.echo("# Your Code:\n```\n" + pr_contents + "\n```")
    reviews = get_code_review(pr_contents)
    click.echo("\n--------------------------------\n")
    click.echo("# ReviewIt-AI Opinion:\n" + reviews)


if __name__ == "__main__":
    main()
