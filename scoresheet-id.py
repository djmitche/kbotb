import os, sys, subprocess, time

def pdfs():
    for dir in os.listdir('.'):
        if os.path.isdir(dir) and dir[0] != '.':
            for f in os.listdir(dir):
                if f[0] != '.':
                    yield os.path.join(dir, f)

def rename(pdf):
    print("processing " + pdf)
    proc = subprocess.Popen(['gs', '-dBATCH', '-dSAFER', pdf],
        stdin=subprocess.PIPE, stdout=open('/dev/null'))
    number = input("number: ")
    proc.stdin.write(b'\n')
    proc.stdin.close()
    if not number:
        return
    number = int(number)
    for i in range(1, 100):
        filename = "{:06d}-{}.pdf".format(number, i)
        if not os.path.exists(filename):
            break
    os.rename(pdf, filename)

def view():
    views = []
    while True:
        n = int(input("number: "))
        for proc in views:
            proc.stdin.write(b'\n')
            proc.stdin.close()
        views = []
        n = "{:06d}".format(n)
        for f in os.listdir('.'):
            if f.startswith(n) and f.endswith('.pdf'):
                proc = subprocess.Popen(['gs', '-dBATCH', '-dSAFER', f],
                    stdin=subprocess.PIPE, stdout=open('/dev/null'))
                views.append(proc)

view()


#for pdf in pdfs():
#    rename(pdf)
