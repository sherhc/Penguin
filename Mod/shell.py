#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE,STDOUT

def run(exe):
	message = Popen(exe,stdout=PIPE,stderr=STDOUT,shell=True)
	# message.kill()
	return message.stdout.read()