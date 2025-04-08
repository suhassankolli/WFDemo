from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain_community.utilities import SerpAPIWrapper


from dotenv import load_dotenv
import os
load_dotenv()

### 