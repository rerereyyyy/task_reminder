import os
from dotenv import load_dotenv

load_dotenv()

SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")
SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")
TASK_API_URL = os.getenv("TASK_API_URL")

if not SLACK_API_TOKEN or not SLACK_CHANNEL_ID:
    raise ValueError("Slack APIトークンまたはチャンネルIDが設定されていません")

