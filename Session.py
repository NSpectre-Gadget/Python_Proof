import requests


def create_session():
    s = requests.Session()
    s.headers.update(
        {"X-Shopify-Accccess-Token": creds.token, "Content-Type": "application/json"}
    )
    return s


def main():
    sess = create_session()
    resp = sess.get(creds.url + "/admin/api/2021-07/products.json?limit=10")
    print(resp.json())
    owner1 = Person()
    owner1.ID_print()


create_session()
main()
# if _name_ == "_main_":
#    Person()
