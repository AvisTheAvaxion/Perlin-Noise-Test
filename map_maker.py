def arr_to_map(arr, w, h):
    s = ""
    for i in range(w):
        for i1 in range(h):
            print(arr[i][i1])
            s = s + str(arr[i][i1])
            if arr[i][i1] == 1 or arr[i][i1] == 2:
                s = s + "🟦"
                print("1/2")

            elif arr[i][i1] == 3 or arr[i][i1] == 4:
                s = s + "🟨"
                print("3/4")

            elif arr[i][i1] == 5 or arr[i][i1] == 6:
                s = s + "🟩"
                print("5/6")

            elif arr[i][i1] == 7 or arr[i][i1] == 8:
                s = s + "⬜"
                print("7/8")

            elif arr[i][i1] == 9 or arr[i][i1] == 10:
                s = s + "⬜"
                print("9/10")

            else:
                s = s + "⁉"
                print("!?")

        s = s + "\n."

    return s


'''
1-2🟦
3-4🟨
5-6🟩
7-8⬜
9-10⬜
⬛🟦🟨🟩⬜
'''
