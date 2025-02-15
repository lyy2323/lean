def make_album(tape, sing, sings=None):
    d_make_album = {"z_tape":tape, "s_sing" : sing}
    if sings:
        d_make_album["sings"] = sings
    return d_make_album
l_make_album = make_album("青花瓷", '布拉格广场')
print(l_make_album)
l_make_album = make_album("只想一生跟你走", "马路杀手", "12")
print(l_make_album)

def favorite_album(tepe, sing):
    fav_album = f"{f_tepe} {f_sing}"
    return fav_album.title()

while True:
    print("你喜欢的歌手和歌曲？")
    print("(输入q退出）")

    f_tepe = input("歌手：")
    if f_tepe == "q":
        break
    f_sing = input("歌曲：")
    if f_sing == "q":
        break
    f_favorite_ablum = favorite_album(f_tepe, f_sing)
    print(f"\n你喜欢的是：{f_favorite_ablum}")