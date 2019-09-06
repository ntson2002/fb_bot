from flask import Flask, request, jsonify, Response
import json
from . import routes
import requests
from pprint import pprint
VERIFY_TOKEN = 'kameronkales'
ACCESS_TOKEN = 'EAAh51ZAZCrmYIBAHUqYn8pBlJKvJEkA2sbZBx2oQEUk4uZARv8HDtF3o91z5ZBxeS5n8FChbRZB6WsLKZCb3n3QS6yH9TGSFJIe5UPciCpqVZBmqcZBqj8y7cZCwqr5uljzZAHaVPk5yppxDwiWpX2UyTnjw6LHaq78fWf3HTRT77EIxQZDZD'

# def reply(user_id, msg):	
#     data = {
#         "recipient": {"id": user_id},
#         "message": {"text": msg}
#     }
#     url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(ACCESS_TOKEN)
#     resp = requests.post(url, json=data)
#     # print(resp.content)



def send_message(sender_id, message_text):
    '''
    Sending response back to the user using facebook graph API
    '''
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",

        params={"access_token": ACCESS_TOKEN},

        headers={"Content-Type": "application/json"}, 

        data=json.dumps({
        "recipient": {"id": sender_id},
        "message": {"text": message_text}
    }))


@routes.route("/auth", methods=['POST'])
def handle_incoming_messages():
    data = request.json
    # print("---------------")
    # import json 
    # print(json.dumps(data, indent=4, ensure_ascii=False))
    # print(data)
    # print("---------------")
    
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):        
                    sender = data['entry'][0]['messaging'][0]['sender']['id']
                    query = data['entry'][0]['messaging'][0]['message']['text']                    
                    print("client send: ", message)                    
                    message = "There are at least 109 mountains on Earth with elevations greater than 7,200 metres (23,622 ft) above sea level. The vast majority of these mountains are located on the edge of the Indian and Eurasian continental plates. "
                    send_message(sender, message)
    
    return "ok"