def get_player_name():
    """プレイヤーの名前を入力させる関数"""
    name = input("あなたの名前を入力してください > ").strip()
    # 未入力の場合は「名無し」にする
    return name if name else "名無し"