FROM python:3.9 

WORKDIR /app 

COPY requirements.txt . 
RUN apt-get update
RUN pip install --no-cache-dir -r requirements.txt 
RUN apt-get install -y libgl1-mesa-dev

COPY . . 

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]