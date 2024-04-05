import whisper
import torch
import time 
import base64
import tempfile
import os 

class WhisperClass:

    def __init__(self, file, use_gpu=False):
        self.file = file
        self.use_gpu = use_gpu and torch.cuda.is_available()
        #self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = "cpu"

    def main(self):

        model = whisper.load_model("base", device=self.device)
        start_time = time.time()
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            with open(tmp_file.name, "wb") as temp_file:
                temp_file.write(self.file.file.read())
            
            result = model.transcribe(tmp_file.name)
            end_time = time.time() 
            process_time = end_time - start_time
            os.remove(tmp_file.name)
            
            return {
                'text': result["text"],
                'filename': self.file.filename,
                'process': process_time
            }
