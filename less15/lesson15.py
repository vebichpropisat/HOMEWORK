import requests


def download(q: str, p: str):
    header = {
        "Authorization": "563492ad6f91700001000001099828c0ba3542f387bfed34ff2fd31f"
    }
    i = 1
    while i <= int(p):
        url = f"https://api.pexels.com/v1/search?query={q}&per_page=1&page={i}"
        r = requests.get(url, headers=header)
        if r.status_code == 200:
            _r = r.json()
            print(_r)
            for item in _r.get("photos"):
                print(item.get("url"))
        else:
            print(r.text)
        i += 1


def main() -> None:
    q = input("Query ")
    p = input("Count page ")
    download(q, p)


main()
