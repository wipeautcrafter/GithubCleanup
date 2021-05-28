# GithubCleanup
Are you tired of leaving old and dusty repositories on your Github profile? Yeah, me too. That is why I created this simple tool to assist me with the pain of going to the options menu of a repository and pressing "delete".

## Installation
```bash
# install pip requirements
pip install -r requirements.txt
```

## Credentials
Make sure to create a `credentials.py` file:
```python
## credentials.py
token = "<YOUR ACCESS TOKEN>"
```

An access token can be created in the Github settings:<br>
`Settings > Developer Settings > Personal Access Tokens`

## Usage
```bash
# run the main module
python index.py
```