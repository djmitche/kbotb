import os, sys, subprocess, time


def pdfs():
    for f in os.listdir("pages"):
        if f[0] != ".":
            yield os.path.join("pages", f)


previous = None


def rename(pdf):
    global previous
    print("processing " + pdf)
    proc = subprocess.Popen(
        ["gs", "-dBATCH", "-dSAFER", pdf],
        stdin=subprocess.PIPE,
        stdout=open("/dev/null"),
    )
    sys.stdout.write("number: ")
    number = sys.stdin.readline().strip()
    proc.stdin.write(b"\n")
    proc.stdin.close()
    if not number:
        print("using previous: %s" % previous)
        if previous:
            number = previous
        else:
            return
    previous = number
    number = int(number.strip())

    for i in range(1, 100):
        filename = "{:06d}-{}.pdf".format(number, i)
        if not os.path.exists(filename):
            break
    print("renaming to %s" % filename)
    os.rename(pdf, filename)


def view():
    views = []
    while True:
        n = int(input("number: "))
        for proc in views:
            proc.stdin.write(b"\n")
            proc.stdin.close()
        views = []
        n = "{:06d}".format(n)
        for f in os.listdir("."):
            if f.startswith(n) and f.endswith(".pdf"):
                proc = subprocess.Popen(
                    ["gs", "-dBATCH", "-dSAFER", f],
                    stdin=subprocess.PIPE,
                    stdout=open("/dev/null"),
                )
                views.append(proc)


# view()


for pdf in sorted(pdfs()):
    rename(pdf)
