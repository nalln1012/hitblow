# ranking_feature.py
import csv
import os

def save_and_show_ranking(name, tries, filename="ranking.csv"):
    """スコア（試行回数）を保存し、上位5名のランキングを表示する関数"""
    # 1. 記録を保存する
    with open(filename, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, tries])
    
    # 2. 過去の記録を読み込む
    records = []
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    records.append((row[0], int(row[1])))
    
    # 3. 試行回数（tries）が少ない順に並び替える（数値として比較）
    records.sort(key=lambda x: x[1])
    
    # 4. 上位5名を表示する
    print("\n👑 === 歴代ランキングトップ5 === 👑")
    for i, (r_name, r_tries) in enumerate(records[:5], 1):
        print(f" {i}位 : {r_name} さん （{r_tries} 回）")
    print("================================")