#!/usr/bin/ python
# coding:utf8
import random

colors = ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'lblue', 'white']

text = 'GOOD!'
a = '1'
b = '31'
nmb = [a,b]
print(nmb)
ncode = ';'.join(nmb)

code = '\x1b['+str(ncode)+'m'+str(text)+'\x1b[0m'
print(code)

def c_dic(text): # Словарь с цветовым форматированием 
	dic_color = {
	'black':'\x1b[40m'+str(text)+'\x1b[0m',
	'red':'\x1b[41m'+str(text)+'\x1b[0m',
	'green':'\x1b[42m'+str(text)+'\x1b[0m',
	'yellow':'\x1b[44m'+str(text)+'\x1b[0m',
	'blue':'\x1b[44m'+str(text)+'\x1b[0m',
	'purple':'\x1b[45m'+str(text)+'\x1b[0m',
	'lblue':'\x1b[46m'+str(text)+'\x1b[0m',
	'white':'\x1b[47m'+str(text)+'\x1b[0m',
	}
	return dic_color

def crandom(text): # Случайный цвет
	r = random.choice(colors)
	out = c_dic(text)[r]
	return out

def different(text, minus='no'): # Разные цвета для каждого символа v1 с выбором исключений некоторых цветов
	sel_color = colors
	for j in minus:
		if j == 'bk': sel_color.remove('black')
		if j == 'r': sel_color.remove('red')
		if j == 'g': sel_color.remove('green')
		if j == 'y': sel_color.remove('yellow')
		if j == 'be': sel_color.remove('blue')
		if j == 'p': sel_color.remove('purple')
		if j == 'l': sel_color.remove('lblue')
		if j == 'w': sel_color.remove('white')
	out_list = []
	for i in text:
		r = random.choice(colors)
		out_one = c_dic(i)[r]
		out_list.append(out_one)
		out = ''.join(out_list)
	return out

# Функция выбора цвета v2

def color(text,clr='no'):
	t = c_dic(text)
	if clr == 'bk': out = t['black'] 
	if clr == 'r': out = t['red']
	if clr == 'g': out = t['green']
	if clr == 'y': out = t['yellow']
	if clr == 'be': out = t['blue']
	if clr == 'p': out = t['purple']
	if clr == 'l': out = t['lblue']
	if clr == 'w': out = t['white']
	return out

# Набор функций установки цвета v1f
def black(text): # Чёрный
	out = '\x1b[40m'+str(text)+'\x1b[0m'
	return out

def red(text): # Красный
	out = '\x1b[41m'+str(text)+'\x1b[0m'
	return out

def green(text): # Зелёный
	out = '\x1b[42m'+str(text)+'\x1b[0m'
	return out	

def yellow(text): # Жёлтый
	out = '\x1b[43m'+str(text)+'\x1b[0m'
	return out	

def blue(text): # Синий
	out = '\x1b[44m'+str(text)+'\x1b[0m'
	return out			

def purple(text): # Пурпурный
	out = '\x1b[45m'+str(text)+'\x1b[0m'
	return out	

def lblue(text): # Голубой
	out = '\x1b[46m'+str(text)+'\x1b[0m'
	return out

def white(text): # Белый
	out = '\x1b[47m'+str(text)+'\x1b[0m'
	return out		


