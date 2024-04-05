FROM nvidia/cuda:12.3.2-cudnn9-runtime-ubuntu22.04
#FROM python:3.8

WORKDIR /code

RUN apt-get update && \
    apt-get install -y python3-pip libzbar0 libgl1-mesa-glx

RUN apt-get update && apt-get install -y ffmpeg

COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cuda120

# Copy main.py and servicewhisper.py to the container
COPY ./main.py /code/main.py
COPY ./servicewhisper.py /code/servicewhisper.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


