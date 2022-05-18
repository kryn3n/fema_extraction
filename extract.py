import requests
import config as cfg


def get_latest_data(state):
    url = cfg.FEMA_REQUEST_URL
    state_code = cfg.STATE_FIPS_CODES[state]
    data = cfg.FEMA_REQUEST_DATA
    data["selstate"] = state_code

    response = requests.post(
                url=url,
                data=data
                )

    data = response.json()
    latest_data = data["EFFECTIVE"]["NFHL_STATE_DATA"][0]["product_FILE_PATH"]
    
    return latest_data


def download_latest_data(filename):
    url = cfg.FEMA_DOWNLOAD_URL.format(filename)
    print(f"Downloading {filename} from {url}...")
    requests.get(url)


def main():
    state = "FL"
    latest_data = get_latest_data(state)
    download_latest_data(latest_data)


main()


