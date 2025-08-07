
import pandas as pd

def generate_daily_plan():
    days = 30
    plan_data = []

    for i in range(1, days + 1):
        day_str = f'Day {i}'
        
        # Vocabulary
        vocab_task = f'學習30-50個新詞 (雅思核心詞彙/主題詞彙) + 複習舊詞 (前1天/3天/7天/15天)'
        
        # Listening
        listening_task = f'精聽1個Section (劍橋雅思真題) + 泛聽英文新聞/播客15分鐘'
        
        # Reading
        reading_task = f'練習1篇雅思閱讀文章 (限時) + 分析長難句/生詞'
        
        # Writing & Speaking (alternating)
        if i % 2 != 0: # Odd days for Writing
            ws_task = f'寫作Task 1或Task 2練習 (交替進行) + 語法/詞彙檢查'
        else: # Even days for Speaking
            ws_task = f'口語練習15-20分鐘 (雅思常見話題) + 錄音回放/模仿跟讀'
            
        plan_data.append({
            '日期': day_str,
            '詞彙': vocab_task,
            '聽力': listening_task,
            '閱讀': reading_task,
            '寫作/口語': ws_task
        })

    df = pd.DataFrame(plan_data)
    df.to_excel('ielts_daily_study_plan.xlsx', index=False)
    df.to_markdown('ielts_daily_study_plan.md', index=False)

if __name__ == '__main__':
    generate_daily_plan()


