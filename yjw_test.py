import os
from dotenv import load_dotenv

load_dotenv()
test = os.getenv('GITHUB_CLIENT_ID')
print(test)


