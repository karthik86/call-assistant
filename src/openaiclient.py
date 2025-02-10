from openai import OpenAI 

class OpenAIClient:

    def __init__(self, token):
        self.client = OpenAI(api_key=token)
    
    def analyse_conversation(self, file_path):
        audio_file = open(file_path, "rb")
        response = self.client.audio.transcriptions.create(model="whisper-1", file=audio_file, response_format='verbose_json')
        response_dict = response.model_dump()
        return {
            "conversation_text_fmt":response_dict["text"],
            "conversation_timestamp_fmt": response_dict["segments"]
        }
    
    def chat(self, input_text, user_message):
        response = self.client.chat.completions.create(model="gpt-4",
                                                        messages=[
            {"role":"system", "content":"You are an assistant"},
            {"role":"user", "content":f"There is a conversation script:\n\n{input_text}\n\n.{user_message}"}
            ],
            temperature=0.5)
        return response