class compile:
    file = open("code.py", "w")
    with open("temp.txt") as f:
        lines = f.readlines()

        for line in lines:
            l1 = ""
            c_out = 0
            c_take = 0
            c_colon = 0
            for l in line:
                if l == ":":
                    l1 += "="
                elif l == ";":
                    l1 += ':'
                elif l == '.':
                    l1 += "   "
                elif l == "o":
                    c_out = 1
                elif l == "u" and c_out == 1:
                    c_out += 1
                elif c_out == 1:
                    l1 += "o"
                    l1 += l
                    c_out = 0
                elif l == "t" and c_out == 2:
                    c_out += 1
                elif c_out == 2:
                    l1 += "ou"
                    l1 += l
                    c_out = 0
                elif l == "(" and c_out == 3:
                    l1 += "print"
                    l1 += l
                    c_out = 0
                elif c_out == 3:
                    l1 += "out"
                    l1 += l
                    c_out = 0


                elif l == "t":
                    c_take = 1
                elif l == "a" and c_take == 1:
                    c_take += 1
                elif c_take == 1:
                    l1 += "t"
                    l1 += l
                    c_take = 0
                elif l == "k" and c_take == 2:
                    c_take += 1
                elif c_take == 2:
                    l1 += "ta"
                    l1 += l
                    c_take = 0
                elif l == "e" and c_take == 3:
                    c_take += 1
                elif c_take == 3:
                    l1 += "tak"
                    l1 += l
                    c_take = 0
                elif l == "(" and c_take == 4:
                    l1 += "input"
                    l1 += l
                    c_take = 0
                elif c_take == 4:
                    l1 += "take"
                    l1 += l
                    c_take = 0
                else:
                    l1 += l
            if l1.startswith('else_if'):
                l = l1.replace('else_if', 'elif')
                file.write(l)
                # print(l)
                continue
            # print(l1)
            file.write(l1)


compile()