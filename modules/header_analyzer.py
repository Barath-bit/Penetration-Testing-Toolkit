import requests

def analyze_headers(url):
    print(f"\n[+] Analyzing headers for {url}")
    response = requests.get(url)

    security_headers = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-XSS-Protection",
        "Strict-Transport-Security"
    ]

    for header in security_headers:
        if header in response.headers:
            print(f"{header} present")
        else:
            print(f"{header} missing")




