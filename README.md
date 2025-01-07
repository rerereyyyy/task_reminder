# Slack Task Reminder

このプロジェクトは、Slackに月末に自動でタスクを送信するPythonスクリプトです。

# 必要なライブラリ
pip install -r requirements.txt

# .env ファイルを作成し、以下の内容を設定
SLACK_API_TOKEN=your_slack_api_token
SLACK_CHANNEL_ID=your_channel_id
TASK_API_URL=your_task_url

# task_remind.py を実行して、月末タスクをSlackに送信します。

```bash
python task_remind.py
