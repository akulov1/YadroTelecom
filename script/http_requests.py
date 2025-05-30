import logging
import requests
import sys

HTTPSTAT_URL = "https://httpstat.us"


def setup_logging():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(handler)
    

def check_status_codes(status_codes):
    for code in status_codes:
        url = f"{HTTPSTAT_URL}/{code}"
        try:
            response = requests.get(url, timeout=5, allow_redirects=False)
            status = response.status_code
            if 100 <= status < 400:
                logging.info(f"Запрос к {url} — статус: {status}, тело: {response.text}")
            elif 400 <= status < 600:
                raise requests.HTTPError(f"Ошибка: получен статус {status} — {response.text}")
        except requests.RequestException as exc:
            logging.error(f"Исключение при запросе к {url}: {exc}")


def main() -> None:
    setup_logging()
    status_codes = [101, 200, 301, 404, 500]
    check_status_codes(status_codes)


if __name__ == "__main__":
    main()
