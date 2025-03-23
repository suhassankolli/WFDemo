Environment setup:
conda create -p venvWFDemo python=3.10
conda activate venvWFDemo/
python -m pip install --upgrade pip
Install packages:
pip install -r requirements.txt


Create a .env file at the root (under WFDemo) and add the following in the file
GOOGLE_API_KEY="your Google Gemini 1.5 pro API key"
