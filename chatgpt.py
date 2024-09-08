import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

class ChatGPT:
    def __init__(self, debug=False):
        self.client = OpenAI(
            organization=os.getenv('ORGANIZATION_ID'),
            project=os.getenv('PROJECT_ID'),
            api_key=os.getenv('API_KEY')
        )
        self.debug = debug

    def get_response(self, system_content, user_content):

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ]
        )
        if(self.debug):
            print(response)
        return response.choices[0].message.content
