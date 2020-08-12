

# Получаем текст истории из файла 'Text_story'

file = open('Text_story','r', encoding= 'utf-8')
text_story = file.read()
#==================================================================================
# 1) методами строк очистить текст от знаков препинания;

#Удаляем каждый знак
text_story_task_1 = text_story
text_story_task_1 = text_story_task_1.replace("."," ")
text_story_task_1 = text_story_task_1.replace(","," ")
text_story_task_1 = text_story_task_1.replace("!"," ")
text_story_task_1 = text_story_task_1.replace("?"," ")
text_story_task_1 = text_story_task_1.replace("—"," ")
text_story_task_1 = text_story_task_1.replace("«"," ")
text_story_task_1 = text_story_task_1.replace("»"," ")
text_story_task_1 = text_story_task_1.replace("("," ")
text_story_task_1 = text_story_task_1.replace(")"," ")
text_story_task_1 = text_story_task_1.replace(";"," ")
text_story_task_1 = text_story_task_1.replace(":"," ")
print(text_story_task_1)
# Удаляем в цикле
text_story_task_1 = text_story
znaki = (".",",","!","—","«","»","(",")",";",":")
for znak in znaki:
    text_story_task_1 = text_story_task_1.replace(znak," ")
print(text_story_task_1)
#==================================================================================
# 2) сформировать list со словами (split);

text_story_task_2 = text_story
list_text = text_story_task_2.split()
print(list_text)
#==================================================================================
# 3) привести все слова к нижнему регистру (map);


# функциями строк
text_story_task_3 = text_story
text_story_task_3 = text_story_task_3.lower()
print(text_story_task_3)
# С Использованием map

text_story_task_3 = text_story


list_story_task_3 = list(map(lambda story_text: story_text.lower(), list_text ))

#==================================================================================
# (5) Дополнительное задание - выполняем лимитизацию

import pymorphy2
pymorphy = pymorphy2.MorphAnalyzer()

morphy_list = []

for elem in list_story_task_3:
    morphy_list.append(pymorphy.parse(elem)[0].normal_form)

text_collect = ' '.join(morphy_list)
print(text_collect)

# text_collect = ''
# for elem in  list_story_task_3:
#     text_collect = text_collect + elem
# print(text_collect)



# - получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;

dict_story_text = {}
for elem in list_story_task_3:
    counter = dict_story_text.get(elem,0)
    dict_story_text[elem] = counter + 1
print(dict_story_text)

#==================================================================================
# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set);

list_story_text_elem_dict = list(dict_story_text.items()) # делаем из словаря список, элементом списка будет пара ключ, значение словаря
list_story_text_elem_dict.sort(key=lambda a: a[1]) # сортируем по значению словаря в элементе списка
list_story_text_elem_dict.reverse()
print(list_story_text_elem_dict[:5])






