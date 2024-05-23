import requests

# Replace these with your SSO provider's specific URLs and credentials
sso_login_url = 'https://756359609882.signin.aws.amazon.com/console'
client_id = 'AKIA3AGULXYNKPA3BR6V'
client_secret = '8INIn2KhnJ7TJNV7aRDSL5a4l7KaiDTze/AqyCTR'
grant_type = 'client_credentials'

def get_access_token():
    # Prepare the payload for the token request
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': grant_type
    }

    # Make the request to the SSO server
    response = requests.post(sso_login_url, data=payload)

    # Check for successful response
    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info['access_token']
        return access_token
    else:
        raise Exception(f"Failed to obtain access token: {response.status_code} {response.text}")

def access_protected_resource(access_token):
    # Replace this URL with the protected resource URL you want to access
    protected_resource_url = 'https://api.example.com/protected/resource'

    # Set up the headers with the access token
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Make the request to the protected resource
    response = requests.get(protected_resource_url, headers=headers)

    # Check for successful response
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to access protected resource: {response.status_code} {response.text}")

if __name__ == '__main__':
    try:
        # Get the access token
        token = get_access_token()
        print(f"Access Token: {token}")

        # Access the protected resource
        protected_data = access_protected_resource(token)
        print(f"Protected Resource Data: {protected_data}")
    except Exception as e:
        print(f"An error occurred: {e}")
