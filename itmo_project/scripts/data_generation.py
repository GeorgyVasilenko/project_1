import pandas as pd
import numpy as np
from datetime import datetime
import random

def generate_mock_data(n=120):
    """Генерация тестовых данных для анализа"""
    themes = ['Любовь', 'Праздник', 'Деньги', 'Дружба', 'Ностальгия', 'Успех']
    moods = ['романтический', 'весёлый', 'грустный', 'агрессивный', 'меланхоличный', 'энергичный']
    artists = ['Тимати', 'Егор Крид', 'Мот', 'Гуф', 'Баста', 'Фараон']
    
    data = []
    for i in range(n):
        # ... (ваш код генерации данных)
    
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    
    month_names = {
        1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель',
        5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
        9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'
    }
    df['month'] = df['date'].dt.month.map(month_names)
    
    # Сохраняем данные
    df.to_csv('../data/rap_videos.csv', index=False)
    return df
