from flask import Flask, request
import requests
# from utils import send_message


app = Flask('hi')

@app.route("/", methods=['POST'])
def home():
    
    data = request.json  # 여기서 request 는 서버로서 우리가 받은 요청  (Server)
    input_message = data['message']['text']
    sender_id = data['message']['from']['id']
    
    if input_message == '안녕':
        send_message('안녕하세요', sender_id)


#   requests.get(url)  # 여기 requests 는 우리가 보내는 요청 (Client)
    return 'Hello Server!'


@app.route('/test')
def test():
    return 'OK'
