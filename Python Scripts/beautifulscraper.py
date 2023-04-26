

from bs4 import BeautifulSoup
from requests import Session


LNs = ['CHP1']


def main() -> None:
    session = Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'})
    login(session)
    for ln in LNs:
        fetch_csv(session, ln)


def login(session: Session) -> None:
    URL='https://cancer.sanger.ac.uk/cosmic'
    LOGIN_ROUTE= '/login'
    login_payload= {
        'email': 'reuben.kuruvilla@student.manchester.ac.uk',
        'pass': 'jynKuf-pamfed-1vinbu',
        'r_url': 'https://cancer.sanger.ac.uk/cosmic',
        'd': '0'
    }
    login_req = session.post(URL + LOGIN_ROUTE, data=login_payload)
    assert login_req.status_code == 200, RuntimeError("Not able to login")


def fetch_csv(session: Session, ln: str) -> None:
    response = session.get(f'https://cancer.sanger.ac.uk/cosmic/gene/analysis?ln={ln}')
    soup = BeautifulSoup(response.text, features="html.parser")
    element = soup.select('[type="hidden"][name="id"]')
    id = element[0]['value']
    download_csv(session, id, ln)


def download_csv(session: Session, id: str, ln: str) -> None:
    response = session.get(f'https://cancer.sanger.ac.uk/cosmic/gene/mutations?id={id};export=csv')
    with open(f"{ln}.csv", "w") as f:
        f.write(response.content.decode("utf-8"))


if __name__ == '__main__':
    main()



