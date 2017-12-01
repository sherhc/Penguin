#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tg # 导入token,id
import telepot,requests
import pprint # debug
import os

token = tg.token	# token='nnnnnnnnn:nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
known_ids = [tg.id]	# known_ids=['nnnnnnnnn']

def checkchat_id(chat_id):
	return len(known_ids) == 0 or str(chat_id) in known_ids
	
def split_string(n, st):
	lst = ['']
	for i in str(st):
		l = len(lst) - 1
		if len(lst[l]) < n:
			lst[l] += i
		else:
			lst += [i]
	return lst
	
def send_message(bot, chat_id, message):
	try:
		pprint.pprint(bot.sendMessage(chat_id, message))
	except Exception as err:
		print "[!] Error sending message: %s" % str(err)
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
		print(content_type)
		# pprint.pprint(msg)
		if content_type == 'text':
			received_command = msg['text']
		elif content_type == 'document':
			file_id = msg['document']['file_id']
			file_name = msg['document']['file_name']
			get_file(bot,file_id,file_name)
			response = 'File saved as ' + file_name
		if response != '':
			responses = split_string(4096, response)
			for resp in responses:
				send_message(bot,chat_id,resp)
bot = telepot.Bot(token)
bot.message_loop(handle)
while True:
	time.sleep(10)