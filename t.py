def get_file_contents(repo_name, pr):
    # Get the repository object
    repo = g.get_repo("sachs7/Flight-Finder")

    # Get the pull request object
    pr = repo.get_pull(2)

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
            contents = repo.get_contents(filename, ref=commit.sha).decoded_content

            # Do something with the contents of the file
            # print(contents)
            file_dict[file] = contents.strip().decode("utf-8")

    # print(file_dict.values())
    return '\n'.join(file_dict.values())


print(get_file_contents("sachs7/Flight-Finder", 2))
