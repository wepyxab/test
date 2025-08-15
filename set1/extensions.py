def main():
    print(get_extension(input('File name: ')))

def get_extension(name):
    name = name.lower().replace(' ', '')
    if '.gif' in name: return('image/gif')
    elif '.jpg' in name or '.jpeg' in name: return('image/jpeg')
    elif '.png' in name: return('image/png')
    elif '.pdf' in name: return('document/pdf')
    elif '.txt' in name: return('text/txt')
    elif '.zip' in name: return('archive/zip')
    else: return('application/octet-stream')

main()
