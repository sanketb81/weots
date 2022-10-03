import schedule
import requests

def main():
    print("sanket")
    requests.get("https://api.telegram.org/bot5713949784:AAFvrR9GKA-ZFiwTbqt4H71jorAmSYC1xLU/sendMessage?chat_id=1095354695&text="+"False")

schedule.every(10).seconds.do(main)
while 1:
    schedule.run_pending()
    time.sleep(1)
