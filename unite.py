import os, sys, subprocess, time

def unite(dest):
    by_num = {}
    for f in os.listdir('.'):
        if not f.endswith('.pdf'):
            continue
        num = int(f[:6], 10)
        by_num.setdefault(num, []).append(f)

    for n in by_num:
        subprocess.call(
            ['pdfunite'] + sorted(by_num[n]) + [os.path.join(dest, '{:06d}.pdf'.format(n))])

unite('united')
