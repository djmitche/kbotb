To combine PDFs:

```
pdfunite a b c output
```

To change resolution:

```
gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -sOutputFile=output.pdf 000219.pdf
```
