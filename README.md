To combine PDFs:

```
pdfunite a b c output
```

To change resolution:

```
gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -sOutputFile=output.pdf 000219.pdf
```

For rotating, pdfshuffler seems best

Splitting:


(note: three-digit page numbers help!)

```
for p in `seq 1 293`; do gs -sSAFER -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dFirstPage=$p -dLastPage=$p  -sOutputFile=pages/$p.pdf combined-rotated.pdf; done
```
