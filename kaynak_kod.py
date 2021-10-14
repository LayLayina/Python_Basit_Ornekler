import urllib.request

site_adress = input("Lütfen Site Adresi Giriniz:")
header = { 
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}

istek = urllib.request.Request(site_adress, headers= header)

html = urllib.request.urlopen(istek)

print(html.read())