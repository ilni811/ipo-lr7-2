#Импорт библиотеки
import json



#Обьявление переменных
file = "dump.json" 
number = str(input("Введите код квалификации для поиска: "))
skills = False


#Открытие файла
#нахождение нужного скилла
#Нахождение нужной специальности
with open(file, "r", encoding="utf-8") as file: 
    data = json.load(file) 
    for skill in data:
        if skill["model"] == "data.skill":
            if skill["fields"]["code"] == number: 
                skill_code = skill["fields"]["code"]
                skill_title = skill["fields"]["title"]
                skills = True
            
              
            for profession in data:
                if profession["model"] == "data.specialty":
                    code_title = profession["fields"]["code"]
                    if code_title in number: 
                        prof_title = profession["fields"]["title"]
                        c_type_title = profession["fields"]["c_type"]
                    
                    

    

if skills:
    print("==========Найдено==========")
    print(f" {code_title} >> Специальность {prof_title} , {c_type_title}")
    print(f" {skill_code} >> Квалификация {skill_title}")
    
else:
    print("==========Не найдено==========")