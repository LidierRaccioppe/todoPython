from reportlab.pdfgen import canvas

frase = "Estas es una bonita frase para ver los distintos tipos de letra."

aux = canvas.Canvas("tiposLetra.pdf")
objTexto = aux.beginText()
objTexto.setTextOrigin(20,500)
objTexto.setFillColor("pink")
espacioCaracteres = 0
objTexto.setFillColorRGB(0.2,0,150)

for tipoLetra in aux.getAvailableFonts():
    objTexto.setCharSpace(espacioCaracteres)
    objTexto.setFont(tipoLetra, 12)
    objTexto.textLine(tipoLetra + ": " + frase)
    objTexto.moveCursor(20, 15)
    espacioCaracteres += 1

objTexto.setFillGray(0.3)
objTexto.setFont("Helvetica",15)
objTexto.setCharSpace(0)
objTexto.setTextOrigin(20,180)
for i in range(10):
    objTexto.setWordSpace(i)
    objTexto.textLine(frase)


aux.drawText(objTexto)
aux.showPage()
aux.save()