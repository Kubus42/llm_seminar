#%% 
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(
    dotenv_path="config.txt",
    override=True
)

#%% 
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")    
)

response = client.embeddings.create(
    input=["Text to be embedded!"],
    model="text-embedding-3-small"
)