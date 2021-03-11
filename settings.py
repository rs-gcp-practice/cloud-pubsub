import io
import os

from google.oauth2 import service_account
import environ


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# start[load env file]
env = environ.Env()

# env_file path
env_file = os.path.join(BASE_DIR, ".env")
# check if `.env` file exists, then load it
if os.path.isfile(env_file):
    env.read_env(env_file)
# end[load env]

# start[project settings and auth]
# secret key
SECRET_KEY = env("SECRET_KEY")
# google auth and project_id
PROJECT_ID = env("PROJECT_ID")
GOOGLE_APPLICATION_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, env("GOOGLE_APPLICATION_CREDENTIALS_FILE"))
)
# end[project settings and auth]