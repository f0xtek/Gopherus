import urllib.parse
import re


def build_http_request(url, method, headers, body):
    """Builds the HTTP request string."""
    url_parts = urllib.parse.urlparse(url)
    domain = url_parts.netloc

    port = 443 if url_parts.scheme == "https" else 80

    http_req = f"{method} {url_parts.path or '/'} HTTP/1.1\r\n"
    http_req += f"Host: {domain}\r\n"
    http_req += f"Content-Length: {len(body.encode('utf-8'))}\r\n"

    for key, val in headers.items():
        http_req += f"{key}: {val}\r\n"

    http_req += f"\r\n{body}"

    return domain, port, http_req


def encode_gopher_payload(http_req, domain, port):
    """Encodes the HTTP request as a Gopher payload."""
    payload = "%0D%0A".join(http_req.split("\r\n"))

    final_payload = urllib.parse.quote_plus(payload).replace("+", "%20")
    gopher_url = urllib.parse.quote_plus(f"gopher://{domain}:{port}/_{final_payload}")
    return gopher_url


def Http():
    try:
        url = input("Please provide the target URL: ").strip()
        if not re.match(r"^https?://", url):
            raise ValueError("Invalid URL. Must start with http:// or https://")

        method = input("Please provide HTTP method (GET, PUT, POST): ").strip().upper()
        if method not in {"GET", "PUT", "POST"}:
            raise ValueError("Invalid HTTP method. Choose from GET, PUT, POST.")

        body = input("Please add the HTTP body (leave empty for none): ").strip()

        headers = {}
        print(
            "Please provide any headers in key=value format, or press enter to continue."
        )
        while True:
            header_input = input("Header: ").strip()
            if not header_input:
                break
            if "=" not in header_input:
                print("Invalid header format. Use key=value.")
                continue
            key, value = map(str.strip, header_input.split("=", 1))
            headers[key] = value

        domain, port, http_req = build_http_request(url, method, headers, body)
        gopher_url = encode_gopher_payload(http_req, domain, port)

        print("\033[93m\nYour gopher link is ready to send HTTP request:\n\033[0m")
        print("\033[04m" + gopher_url + "\033[0m")

    except Exception as e:
        print(f"\033[91m[ERROR] {e}\033[0m")
