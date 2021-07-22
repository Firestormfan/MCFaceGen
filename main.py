import requests

def main():
    ask_3d_or_2d = input("1で2Dの画像\n2で3Dの画像を生成します ")
    if ask_3d_or_2d == "1":
        file_name = "_2d"
        crafatar_api_url = "https://crafatar.com/avatars/{}"
    elif ask_3d_or_2d == "2":
        file_name = "_3d"
        crafatar_api_url = "https://crafatar.com/renders/head/{}"
    name = input("Minecraftのユーザーネームを入力してください ")
    request_mojang_api = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
    check_valid_user = request_mojang_api.get("id",None)
    if check_valid_user == None:
        print(f"ユーザー'{name}'は存在していません。")
    else:
        request_crafatar_api = requests.get(crafatar_api_url.format(request_mojang_api["id"]),stream=True)
        if request_crafatar_api.status_code == 200:
            with open(f"images\{name}{file_name}.png","wb") as f:
                f.write(request_crafatar_api.content)

if __name__ == "__main__":
    main()