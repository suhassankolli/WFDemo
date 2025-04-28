from dotenv import load_dotenv
import os
load_dotenv("../../../.env")

myVar = os.getenv("GOOGLE_API_KEY")
print(myVar)