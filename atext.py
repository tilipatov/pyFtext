#!/usr/bin/ python
# coding:utf8
"""#d = input('Введите текст: ')
print('\t\t\x1b[0mОбычный\x1b[0m\v')
print('\t\t\x1b[1mЖирный\x1b[0m\v')
print('\t\t\x1b[2mМутный\x1b[0m\v')
print('\t\t\x1b[3mКурсив\x1b[0m\v')
print('\t\t\x1b[4mПодчёркиание\x1b[0m\v')
print('\t\t\x1b[7mИнвентирование\x1b[0m\v')
print('\t\t\x1b[8mНевидимый\x1b[0m\v')
print('\t\t\x1b[9mЗачёркнутый\x1b[0m\v')
"""
def b(text): # Жирный
	out = '\x1b[1m'+str(text)+'\x1b[0m'
	return out

def i(text): # Наклонный
	out = '\x1b[3m'+str(text)+'\x1b[0m'
	return out

def ins(text): # Подъчёркнутый
	out = '\x1b[4m'+str(text)+'\x1b[0m'
	return out	

def invert(text): # Инвертирование цветов
	out = '\x1b[7m'+str(text)+'\x1b[0m'
	return out	

def dlt(text): # Зачёркнутый
	out = '\x1b[9m'+str(text)+'\x1b[0m'
	return out			