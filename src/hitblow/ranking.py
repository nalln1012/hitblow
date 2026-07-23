import csv
import os

def save_and_show_ranking(name, tries, diff, filename="ranking.csv"):
    """
    スコア（試行回数）を保存し、指定された難易度（diff）の上位5名を表示する関数
    
    :param name: プレイヤー名
    :param tries: 試行回数
    :param diff: 難易度（1〜9の整数）
    :param filename: 保存先CSVファイル名
    """
    # 1. 記録を保存する（難易度 diff を最後に追加）
    with open(filename, mode='a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, tries, diff])
    
    # 2. 過去の記録を読み込む
    records = []
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                # 列数が3つあり、かつ指定された難易度(diff)と一致する行のみを抽出
                if len(row) == 3 and int(row[2]) == diff:
                    records.append((row[0], int(row[1])))
    
    # 3. 試行回数（tries）が少ない順に並び替える
    records.sort(key=lambda x: x[1])
    
    # 4. 指定難易度の上位5名（名前とスコア）を出力する
    print(f"\n👑 === \033[1;36m難易度 {diff} のランキングトップ5 👑\033[0m=== ")
    for i, (r_name, r_tries) in enumerate(records[:5], 1):
        print(f" {i}位 : {r_name} さん （{r_tries} 回）")
    print("==========================================")
