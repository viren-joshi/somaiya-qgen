from gradio_client import Client

client = Client("https://devashishbhake-question-generation.hf.space/")
result = client.predict("Ping Request. Pls dont shut down.", api_name="/predict")
print(result)
