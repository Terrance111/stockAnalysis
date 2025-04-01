import requests

def check_api_status(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print("API is running.")
        else:
            print(f"API returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"API is not reachable: {e}")

# 示例用法
check_api_status("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=6ZI495EUNAXCLI7T")