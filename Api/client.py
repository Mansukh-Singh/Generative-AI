import requests

def get_openai_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json = {
        'input' : {
            'topic': input_text
        }
    }
    )
    print(response.json()['output'])

input_text = "singer"
get_openai_response(input_text)
