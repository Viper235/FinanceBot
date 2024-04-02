import json
from datetime import datetime
 


def save_data(
        user_id: int,
        category: str,
        amount: str,
        operation: str
    ):
    user_id = str(user_id)
    amount = int(amount)

#Словарь с данными транзакции 
    transaction = {
        'operation': operation,
        'amount': amount,
        'category':category
    }

    

    current_day = datetime.now().strftime('%d.%m.%Y')

    #Открываем нашу базу
    data: dict = json.load(
        open('data.json')
    )
#Пользователя нет в базе
    if user_id not in data:
        data[user_id] = {
            current_day:[
                transaction
            ]
        }
        #Записываем словарь в .json
        
    else:
        if current_day in data[user_id]:
        #Если есть записи на текущий день добавляем к ним новую транзакцию
            data[user_id][current_day].append(transaction)
        else:
            #Если нет такого дня 
            data[user_id][current_day] = [transaction]
    json.dump(
            data,
            open(
                file='data.json',
                mode='w',
                encoding= 'utf-8',
            ),
            indent=4,
            ensure_ascii=False
        )

def load_data(user_id):
    user_id = str(user_id)
    data: dict = json.load(
        open('data.json')
    )

    if user_id not in data: raise KeyError

    current_day = datetime.now().strftime('%d.%m.%Y')
    transactions = data[user_id][current_day]

    #Заработали
    earned: int = 0
    #Потратили
    spent: int = 0
    for transaction in transactions:
        if transaction['operation'] == '+':
            earned += transaction['amount']
        else:
            spent += transaction['amount']

    return earned,spent

    

     

#Это сработает только если мы выполняем файл utils.py напрямую
if __name__=='__main__':
    save_data(user_id=1, category='выпечка', amount= '50', operation='+')
