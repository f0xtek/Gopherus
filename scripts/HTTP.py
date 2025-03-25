import urllib.parse
import re


def build_http_request(url_parts, method, headers, body):
    """Builds the HTTP request string."""
    return f"""{method} {url_parts.path or ''} HTTP/1.1
Host: {url_parts.netloc}
{'\r\n'.join(f"{key}: {val}" for key, val in headers.items())}
{'\r\n'+body if body else None}"""


def encode_gopher_payload(domain, port, http_req):
    """Encodes the HTTP request as a Gopher payload."""
    payload = urllib.parse.quote(http_req, safe="/")
    return f"gopher://{domain}:{port}/_{payload}"


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

        url_parts = urllib.parse.urlparse(url)
        domain = url_parts.netloc
        port = 443 if url_parts.scheme == "https" else 80
        http_req = build_http_request(url_parts, method, headers, body)
        gopher_url = encode_gopher_payload(domain, port, http_req)

        print("\033[93m\nYour gopher link is ready to send HTTP request:\n\033[0m")
        print("\033[04m" + gopher_url + "\033[0m")
        print("\033[93m\nNote: if you are sending this payload as part of another HTTP request, e.g. inside of another HTTP POST request, you need to URL encode the entire gopher payload once more.\n\033[0m")

    except Exception as e:
        print(f"\033[91m[ERROR] {e}\033[0m")
