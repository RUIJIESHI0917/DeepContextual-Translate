from openai import OpenAI
import os 

class TranslateGPTModel:
    def __init__(self):
        self.model = "gpt-4o-mini"
        self.api_key = os.getenv("API_KEY")
        print(self.api_key)
        self.temperature = 0.4

        self.client = OpenAI(api_key=self.api_key)
    
    def describe(self, text):
        """
        Generate several adjectives to describe the style of the given text.
        :param text: str, the text to analyze.
        :return: strs, adjectives describing the text.
        """
        response = self.client.chat.completions.create(
            model = self.model,
            temperature = self.temperature,
            messages = [
                {"role": "system", "content": "You are an assistant that can describe the given text by using some adjectives."},
                {"role": "user", "content": f"Use as many as possible adjectives to describe for this text: {text}.  Please just give me the styles and no other words. Each adjectives must be seperated with the word 'and'."},
            ],
        )
        style = response.choices[0].message.content
        return style
    
    def translate(self, text, adjectives, language):
        """
        Translate the given text based on some adjectives list to the certain language
        :param text: str, the text to translate
        :param adjectives: strs, a serial of adjectives that represents the text
        :param language: strs, the language the user wants to translate the text to
        :return: strs, the translation for this text
        """
        response = self.client.chat.completions.create(
            model = self.model,
            temperature = self.temperature,
            messages = [
                {"role": "system", "content": "You are a professional translator that can translate text based on some descriptions. Remeber, Please just give me the tranlation and no other things. No prefix please. "},
                {"role": "user", "content": f"Y. Please firstly understand the given text: {text} and how it can be related to these given descriptions: {adjectives}. Then, you may rewrite the text based on based on these given descriptions and your own understanding, finally translate the text into {language}"},
            ]
        )
        translation = response.choices[0].message.content
        return translation
    
    def generate(self, adjectives, language):
        """
        Generate a sample text based on some adjectives
        :param adjectives: strs, some adjectives to describe the text
        :param language: str, the target language of the generated text
        :return: strs, the generated text
        """
        response = self.client.chat.completions.create(
            model = self.model,
            temperature = self.temperature,
            messages = [
                {"role": "system", "content": "You are a writer that can write contents based on some descriptions. Remember, just give me the text you write and no other things. No prefix please."},
                {"role": "user", "content": f"Please based on the following adjectives and styles {adjectives} to generate a text in {language}. "},
            ]
        )

        generate = response.choices[0].message.content
        return generate

