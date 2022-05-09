import qrcode

img = qrcode.make("Coloque a URL destino")
type (img) #qrcode.image.pil.pilImage
img.save ("nomedoarquivo.png")