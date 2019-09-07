from flask import Flask, request, jsonify, Response
import json
from . import routes
import requests
from pprint import pprint
VERIFY_TOKEN = 'kameronkales'
ACCESS_TOKEN = 'EAAh51ZAZCrmYIBALZCm3ZBFPpNG68ZBuahi8DAE0Nmhp2ZC9qTr73vsMmkaRueZBIRZCXgtfcxzXEskHiotbdeQKvPHsx5BcPTyvAsySovgt1GzOjEEaFjbqYBTH0kUBK5mc9i5w7pkPXUp2MBhGqqoo7Vy4UPQlrsEaNwLi7qkHZBwZDZD'

# def reply(user_id, msg):	
#     data = {
#         "recipient": {"id": user_id},
#         "message": {"text": msg}
#     }
#     url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(ACCESS_TOKEN)
#     resp = requests.post(url, json=data)
#     # print(resp.content)




def find_answer(q):
    url = "http://zalo-assistant.laban.vn/serve_kiki_app/"

    # payload = "{\n        \"question\": \"Mao Trạch Đông sinh năm bao nhiêu\"\n}"
    payload = {
        "question": q
    }
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "fed98921-b60a-4391-9e12-f00d6fd4d35d"
        }

    response = requests.request("GET", url, data=json.dumps(payload), headers=headers)
    return json.loads(response.text)
    


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
#     print(r.content)


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
                    print("question: ", query)                    
                    message = "There are at least 109 mountains on Earth with elevations greater than 7,200 metres"
#                     message = find_answer(query)
                    print("answer", message)
                    send_message(sender, message)
    
    return "ok"
