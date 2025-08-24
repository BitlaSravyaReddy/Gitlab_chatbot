## File 3: streamlit.py - The Interactive Chat Interface

This file creates the web application that users interact with.


### Streamlit Configuration (MUST be first!)
```
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Part2.llm_integration import setup_api_key, build_qa_chain

import streamlit as st
st.set_page_config("GitLab GenAI Chatbot", page_icon="🤖", layout="wide")
```

**What these lines do:**
- **Line 1**: Imports os for system operations
- **Line 2**: Imports sys to access and modify Python’s runtime environment
- **Line 3**: Ensures Python can find and import modules from the project’s parent folder.
- **Line 4**: Imports setup_api_key and build_qa_chain from the Part2 folder.
- **Line 5**: Imports Streamlit, the web framework
- **Line 6**: Configures the web page title, icon, and layout

**Why this MUST be first:**
- Streamlit requires page configuration before any other Streamlit commands
- If you put this after other st. commands, you'll get an error


### API Key Setup with Security
```python
if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("Google API Key not found. Please add it to Streamlit secrets.")
    st.stop()
```

**What each line does:**
- **Line 1**: Checks if the API key exists in Streamlit's secure secrets
- **Line 2**: If found, sets it as an environment variable for the AI model to use
- **Line 3**: If not found, shows an error message
- **Line 4**: Stops the application from running without the API key

**Why this approach:**
- **Security**: API keys never appear in code that gets shared publicly
- **Flexibility**: Different environments (development, production) can use different keys
- **Error handling**: Clear message if setup is incomplete
