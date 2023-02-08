import json
import os

import openai
from dotenv import load_dotenv

class Copilot:

    def clean_text(self,text):
        a = text.replace('\n',' ')
        b = a.split()
        c = ' '.join(b)

        return c

    def get_answer(self,question):
        prompt = question

        load_dotenv()

        openai.api_key = os.getenv('KEY_OPENAI')

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=512,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )

        json_object = response

        json_string = json.dumps(json_object)

        parsed_json = json.loads(json_string)

        text = parsed_json['choices'][0]['text']
        cleared_text = self.clean_text(text)

        return cleared_text