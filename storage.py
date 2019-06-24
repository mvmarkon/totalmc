from __future__ import print_function
import json
import os
from os.path import expanduser
import sys
from config import Config as cfg

def is_empty(something):
    if something:
        return False
    else:
        return True

def get_content(rootdir):
	dir = {}
	rootdir = rootdir.rstrip(os.sep)
	start = rootdir.rfind(os.sep) + 1
	for path, dirs, files in os.walk(rootdir):
			folders = path[start:].split(os.sep)
			subdir = dict.fromkeys(files)
			print(subdir)
			parent = reduce(dict.get, folders[:-1], dir)
			parent[folders[-1]] = subdir
	return dir
# def get_content(dir, tree):
# 	#print('GET CONTENT', file=sys.stdout)
# 	tree['basepath']=dir
# #	tree['subdirs'] = []
# 	tree['files'] = []
# 	# print(dir)
# 	for path,subdirs,files in os.walk(dir):
# #		for dirname in subdirs:
# #			dr={}
# #			dr['dirname'] = dirname
# #			dr['dirpath'] = os.path.join(dir, dirname)
# #			dr['type'] = 'directory'
# ##			dr['childs'] = get_content( os.path.join(dir, dirname), tree)
# #			print(dr['dirpath'])
# #			# print(dirname)
# #			# print(tree['subdirs'])
# #			tree['subdirs'].append(dr)
# #			#print(get_content(os.path.join(dir, dirname), tree))
# 		for filename in files:
# 			# print(filename)
# 			fl = {}
# 			fl['name'] = filename
# 			fl['filepath'] = os.path.join(path,filename)
# 			fl['type'] = 'file'
# 			# print(tree['files'])
# 			tree['files'].append(fl)
# 					
# 
# 	return tree

def connect():
	tree = get_content(cfg.basedir)
	print(tree)
	return tree

def ifnotexistcreate(dir):
	print('IF NO EXIST CREATE', file=sys.stdout)
	if not os.path.exists(dir):
		os.makedirs(dir)
	

def __init__(self):
	home = expanduser("~")
	with open('totalmc.json') as json_file:  
		data = json.load(json_file)
		directory = home + data.get('path')
		self.ifnotexistcreate(directory)
		print('error' + directory, file=sys.stderr)
		print('standard ' + directory, file=sys.stdout)
		self.ifnotexistcreate(directory+'/audio')
		self.ifnotexistcreate(directory+'/video')