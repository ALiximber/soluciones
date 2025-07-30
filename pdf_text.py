import PyPDF2

def pdf_a_texto(ruta_pdf):
    with open(ruta_pdf, 'rb') as f:
        lector = PyPDF2.PdfReader(f)
        texto = ""
        for pagina in lector.pages:
            texto += pagina.extract_text()
    return texto

if __name__ == '__main__':
    ruta = input("PDF a convertir: ")
    print(pdf_a_texto(ruta))
