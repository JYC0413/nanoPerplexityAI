from llama_index.core.llms import ChatMessage
from llama_index.llms.openai_like import OpenAILike

prompt = [{'role': 'system', 'content': '\n    You are a helpful assistant whose primary goal is to decide if a user\'s query requires a Google search. You should use Google search for mostqueries to find the most accurate and updated information. Follow these conditions:\n\n    - If the query does not require Google search, you must output "no".\n    - If the query requires Google search, you must respond with a reformulated user query for Google search.\n    '}, {'role': 'user', 'content': 'who are you?'}]
client = OpenAILike(model="Mistral-7B-Instruct-v0.3", api_base="http://127.0.0.1:10086/v1", api_key="LLAMAEDGE")
response = client.complete("Tell me about Apple")
print(response)