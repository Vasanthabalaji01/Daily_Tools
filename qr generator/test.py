import requests
import subprocess

# Define your access token
ACCESS_TOKEN = "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"

# Define the correct GitHub API endpoint for listing repositories of the authenticated user
GITHUB_ENDPOINT = "https://api.github.com/user/repos"

# Set up headers with the access token for authentication
headers = {
    "Authorization": f"token {ACCESS_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Make a request to the GitHub API to get the repositories
response = requests.get(GITHUB_ENDPOINT, headers=headers)

# Print the status code and response content for debugging
print(f"Status Code: {response.status_code}")
print("Response Content:")
print(response.content)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    repos = response.json()
    # Print the repositories for debugging
    print("Repositories:")
    print(repos)
    # Iterate over each repository
    for repo in repos:
        repo_name = repo['name']
        clone_url = repo['clone_url']
        print(f"Cloning {repo_name} from {clone_url}")
        # Run git clone command
        subprocess.run(["git", "clone", clone_url])
else:
    print(f"Failed to retrieve repositories: {response.status_code}")
    print(response.json())