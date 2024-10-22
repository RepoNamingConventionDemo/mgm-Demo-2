import requests
import os
import logging

# Set constants
GITHUB_API_URL = 'https://api.github.com'
GITHUB_TOKEN="gh_tkdsfn4gkhebrkgbekhrgberg"

def is_secret_scanning_enabled(org, repo, pat):
    """Check if secret scanning is enabled for the repository."""
    url = f"{GITHUB_API_URL}/repos/{org}/{repo}"
    headers = {
        'Authorization': f'Bearer {pat}',
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        logging.error(f"Failed to fetch repository data: {response.status_code}, {response.text}")
        return False
    
    repo_info = response.json()
    if 'secret_scanning' in repo_info.get('security_and_analysis', {}):
        status = repo_info['security_and_analysis']['secret_scanning']['status']
        return status == 'enabled'
    else:
        return False

def get_secret_scanning_alerts(org, repo, pat):
    """Fetch all secret scanning alerts for the repository."""
    url = f"{GITHUB_API_URL}/repos/{org}/{repo}/secret-scanning/alerts"
    headers = {
        'Authorization': f'Bearer {pat}',
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        logging.error(f"Failed to fetch secret scanning alerts: {response.status_code}, {response.text}")
        return []
    
    return response.json()

def main():
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)

    # Fetch environment variables
    github_token = os.getenv('GITHUB_TOKEN')
    if not github_token:
        logging.error("Please set the GITHUB_TOKEN environment variable.")
        return
    
    org = input("Enter the organization name: ")
    repo = input("Enter the repository name: ")
    
    # Check if secret scanning is enabled
    if is_secret_scanning_enabled(org, repo, github_token):
        logging.info(f"Secret scanning is enabled for {org}/{repo}.")
        
        # Get secret scanning alerts
        alerts = get_secret_scanning_alerts(org, repo, github_token)
        if alerts:
            logging.info(f"Found {len(alerts)} secret scanning alerts for {org}/{repo}.")
            for alert in alerts:
                print(f"Alert {alert['number']} - Secret Type: {alert['secret_type']}, State: {alert['state']}")
        else:
            logging.info(f"No secret scanning alerts found for {org}/{repo}.")
    else:
        logging.warning(f"Secret scanning is not enabled for {org}/{repo}.")

if __name__ == "__main__":
    main()
