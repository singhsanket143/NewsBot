
# from flask import Flask, request
# from pymessenger import Bot
# from util import fetch_reply

# app = Flask(__name__)


# FB_ACCESS_TOKEN = "EAAa8JbBFhm0BAJ4EHGFDpmHXFhpTBKUzUOyMwKNdGfYl4ibCLEgHXzEtuckbZCKW9kuUjkhhseUFIqIJ6IHYkOe5WIm774PRmZCKM7a0w7TsOCyqaZBJtSlFq8ThrMaCajbc358qzvpVwbhgZAIG8ZA3FeqWmJeuZBQbXHoJx8eZAVmvbAZA42mJ"
# bot = Bot(FB_ACCESS_TOKEN)


# @app.route('/', methods=['GET'])
# def verify():
#     if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
#         if not request.args.get("hub.verify_token") == "hello":
#             return "Verification token mismatch", 403
#         return request.args["hub.challenge"], 200
#     return "Hello world", 200


# @app.route('/', methods=['POST'])
# def webhook():
# 	print(request.data)

# 	data = request.get_json()

# 	if data['object'] == "page":
# 		entries = data['entry']

# 		for entry in entries:
# 			messaging = entry['messaging']

# 			for messaging_event in messaging:

# 				sender_id = messaging_event['sender']['id']
# 				recipient_id = messaging_event['recipient']['id']

# 				if messaging_event.get('message'):

# 					if messaging_event['message'].get('text'):

# 						query = messaging_event['message']['text']
# 						# reply = fetch_reply(query, sender_id)

# 						# bot.send_text_message(sender_id, reply['data'])
# 						# bot.send_image_url(sender_id,"http://webneel.com/wallpaper/sites/default/files/images/07-2013/6%20lamborghini%20car%20wallpaper.preview.jpg")
# 						# buttons=[{"type":"web_url",
# 						# 		  "url":"https://www.google.co.in",
# 						# 		  "title":"Visit"}]
# 						# bot.send_button_message(sender_id,"check this out !",buttons)
# 						buttons=[{"type":"postback",
# 								  "payload":"SHOW_HELP",
# 								  "title":"Click to see help"}]
# 						bot.send_button_message(sender_id,"check this out !",buttons)
# 				elif messaging_event.get('postback'):
# 					# print(messaging_event['postback'])
# 					if messaging_event['postback']['payload']== 'SHOW_HELP':
# 						bot.send_text_message(sender_id,"Ok dear")
# 	return "ok", 200

# if __name__ == "__main__":
# 	app.run(port=8000, use_reloader = True)

from flask import Flask, request
from pymessenger import Bot
from util import fetch_reply

app = Flask(__name__)


FB_ACCESS_TOKEN = "EAAa8JbBFhm0BAJ4EHGFDpmHXFhpTBKUzUOyMwKNdGfYl4ibCLEgHXzEtuckbZCKW9kuUjkhhseUFIqIJ6IHYkOe5WIm774PRmZCKM7a0w7TsOCyqaZBJtSlFq8ThrMaCajbc358qzvpVwbhgZAIG8ZA3FeqWmJeuZBQbXHoJx8eZAVmvbAZA42mJ"
bot = Bot(FB_ACCESS_TOKEN)


@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == "hello":
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
	print(request.data)

	data = request.get_json()

	if data['object'] == "page":
		entries = data['entry']

		for entry in entries:
			messaging = entry['messaging']

			for messaging_event in messaging:

				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):

					if messaging_event['message'].get('text'):

						query = messaging_event['message']['text']
						reply = fetch_reply(query, sender_id)

						if reply['type'] == 'news':
							bot.send_generic_message(sender_id, reply['data'])
						else:
							bot.send_text_message(sender_id, reply['data'])					

				elif messaging_event.get('postback'):
					if messaging_event['postback']['payload'] ==  'SHOW_HELP':
						bot.send_text_message(sender_id, "Ok. I will show you help message!")
	return "ok", 200

if __name__ == "__main__":
	app.run(port=8000, use_reloader = True)

"""
buttons = [{"type":"web_url","url":"https://www.facebook.com/Mycodebot-1293905183961696/","title":"Visit our page"}]
						bot.send_button_message(sender_id,PAGE_LINK,buttons)
buttons = [{"type":"postback",
									"payload": "SHOW_HELP",
									"title":"Click here for help!"}]
						bot.send_button_message(sender_id, "Check out this website!",buttons)
"""
