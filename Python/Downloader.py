import requests

def download_file(url, cookies=None, headers=None):
    response = requests.get(url, cookies=cookies, headers=headers)
    response.raise_for_status()
    return response.text

if __name__ == "__main__":
    url = "https://store9.gofile.io/download/direct/6e33bfb9-3eea-42b1-a60e-17b5fa199b1a/VRA_January2025_ArchivePassword.txt"
    cookies = {
        'accountToken': 'JxRnMsObchURUmcgoUuTQhUkARfjPLks',
    }
    headers = {
        'referer': 'https://www.patreon.com/',
    }

    try:
        content = download_file(url, cookies=cookies, headers=headers)
        print(content)
    except requests.RequestException as e:
        print(f"Download failed: {e}")