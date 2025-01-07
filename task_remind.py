import schedule
import time
from config.setting import SLACK_API_TOKEN,SLACK_CHANNEL_ID,TASK_API_URL
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import datetime

#Slack APIのトークンを設定
client = WebClient(token = SLACK_API_TOKEN)

#送信するチャンネルIDを設定
channel_id = SLACK_CHANNEL_ID

#URLを設定
task_url = TASL_API_URL

#task送信関数
def send_task():
    try:
        blocks = [
            {
                "type":"section",
                "text":{
                    "type":"mrkdwn",
                    "text":"月末タスク:\n- タスク１：経費申請\n- タスク２：打刻エラー修正"
                }
            },
            {
                "type":"actions",
                "elements":[
                    {
                        "type":"button",
                        "text":{
                            "type":"plain_text",
                            "text":"taskURL"
                        },
                        "url":task_url,
                        "style":"primary",
                        "value":"task_details_button"
                    }
                ]
            }
        ]
        
        #チャンネルに送信
        response = client.chat_PostMessage(
            channel=channel_id
            text="月末タスク一覧",
            blocks=blocks
        )
        print("タスクが送信されました",response["message"]["text"])
    except SlackApiError as e:
        print(f"Error sending message:{e.response['error']}")

#月末にタスクを送信するスケジュールを設定
def job():
    today = datetime.date.today()
    #次の日の１日を取得
    next_month = today.replace(day=28) + datetime.timedelta(day=4)
    next_month_first_day = next_month.replace(day=1)
    
    #月末の日を取得
    month_end = next_month_first_day - datetime.timedelta(day=1)
    
    #月末かどうか確認
    if today == month_end:
        send_task()
        
#スケジュールの設定
schedule.every().day.at("10:00").do(job)

#実行
while True:
    schedule.run_pending()
    time.sleep(60)