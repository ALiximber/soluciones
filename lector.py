import nfc

def conectar():
    clf = nfc.ContactlessFrontend('usb')
    clf.connect(rdwr={'on-connect': lambda tag: print(tag.ndef.message)} )

conectar()
