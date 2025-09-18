f = open('gen.txt', 'w')

#declaring constants
for i in range(1, 10):
    for j in range(1, 10):
        for n in range(1, 10):
            f.write("(declare-const P_" + str(j) + "_" + str(i) + "_" + str(n) + " Bool)\n")


for i in range(1, 10):
    for n in range(1, 10):
        write = "(assert (or"
        for j in range(1, 10):
            write += " P_" + str(j) + "_" + str(i) + "_" + str(n)
        write += "))\n"
        f.write(write)


for j in range(1, 10):
    for n in range(1, 10):
        write = "(assert (or"
        for i in range(1, 10):
            write += " P_" + str(j) + "_" + str(i) + "_" + str(n)
        write += "))\n"
        f.write(write)


for l in range(3):
    for m in range(3):
        for n in range(1, 10):
            write = "(assert (or"
            for o in range(1, 4):
                for p in range(1, 4):
                    write+= f" P_{m*3 + p}_{l*3 + o}_{n}"
            write += "))\n"
            f.write(write)

#big assert statements
for i in range(1, 10):
    for j in range(1, 10):
        for n1 in range(1, 10):
            write = f"(assert (or (not P_{j}_{i}_{n1}) (not (or"
            for n2 in range(1, 10):
                if n1 != n2:
                    write += f" P_{j}_{i}_{n2}"
            write += "))))\n"
            f.write(write)

f.write('(check-sat)\n(get-model)\n')
f.close()
