from openai import OpenAI  # Import the OpenAI-compatible client used to send chat requests.
from dotenv import load_dotenv  # Import the helper that loads variables from a local .env file.
import os  # Import operating-system utilities, including environment-variable access.

# Load configuration values from the .env file into the process environment.
load_dotenv()  # Make BASE_URL, API_KEY, and MODEL available through os.getenv().

# Create a client configured to communicate with the Ollama OpenAI-compatible API.
client = OpenAI(
    base_url=os.getenv("BASE_URL"),  # Read the API endpoint URL from the environment.
    api_key=os.getenv("API_KEY")  # Read the API key expected by the client from the environment.
)

# Send a chat-completion request containing a question for the configured model.
response = client.chat.completions.create(
    model=os.getenv("MODEL"),  # Select the model name configured in the environment.
    messages=[
        {
            "role": "user",  # Identify this message as coming from the user.
            "content": "What is Artificial Intelligence?"  # Provide the question for the model to answer.
        }
    ]
)

# Display the text content of the first response choice.
print(response.choices[0].message.content)  # Print the model's answer to the console.