#!/bin/bash

# GitHub organization name
ORG_NAME="RepoNamingConventionDemo"  # Provide organization name


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
RESPONSE=$(curl -s -H "Authorization: token $GIT_TOKEN" \
"https://api.github.com/orgs/$ORG_NAME/repos")

# Check if the response is valid JSON
if echo "$RESPONSE" | jq -e . > /dev/null 2>&1; then
    # If it's valid JSON Response, parse repository names
    REPOS=$(echo "$RESPONSE" | jq -r '.[].name')
else
    echo "Error: Failed to fetch repositories. Response: $RESPONSE"
    exit 1 
fi

# Loop through each repository and rename it with mgm- prefix
for REPO in $REPOS; do
    rename_repo "$REPO"
done
