import requests

cookies = {
    'accountToken': 'JxRnMsObchURUmcgoUuTQhUkARfjPLks',
}

headers = {
    'referer':'https://www.patreon.com/', 
    }

response = requests.get(
    'https://store9.gofile.io/download/direct/6e33bfb9-3eea-42b1-a60e-17b5fa199b1a/VRA_January2025_ArchivePassword.txt',
    cookies=cookies,
    headers=headers,
)

print(response.content.decode("utf-8"))