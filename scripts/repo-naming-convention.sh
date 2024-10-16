#!/bin/bash

# GitHub organization name
ORG_NAME="RepoNamingConventionDemo"  # Replace with your organization name
# GitHub token with necessary permissions to list and modify repositories
GIT_TOKEN="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"  # Replace with your GitHub Personal Access Token

# Function to rename the repository by adding 'mgm-' prefix
rename_repo() {
    REPO_NAME=$1
    # Check if the repository name already starts with 'mgm-'
    if [[ $REPO_NAME == mgm-* ]]; then
        echo "Repository '$REPO_NAME' already follows the naming convention."
    else
        NEW_REPO_NAME="mgm-$REPO_NAME"
        echo "Renaming '$REPO_NAME' to '$NEW_REPO_NAME'..."

        # Call GitHub API to rename the repository
        RESPONSE=$(curl -s -X PATCH \
        -H "Authorization: token $GIT_TOKEN" \
        -H "Accept: application/vnd.github.v3+json" \
        -d "{\"name\": \"$NEW_REPO_NAME\"}" \
        "https://api.github.com/repos/$ORG_NAME/$REPO_NAME")

        # Check if the response contains the new repository name
        if echo "$RESPONSE" | grep -q "$NEW_REPO_NAME"; then
            echo "Successfully renamed '$REPO_NAME' to '$NEW_REPO_NAME'."
        else
            echo "Failed to rename '$REPO_NAME'. Response: $RESPONSE"
        fi
    fi
}

# Fetch all repositories from the GitHub organization
REPOS=$(curl -s -H "Authorization: token $GIT_TOKEN" \
"https://api.github.com/orgs/$ORG_NAME/repos" | jq -r '.[].name')

# Loop through each repository and attempt to rename it
for REPO in $REPOS; do
    rename_repo $REPO
done
