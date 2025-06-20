# create_session.py

from telethon.sync import TelegramClient

# 사용자 계정용 API 정보
api_id = 23817667
api_hash = 'c32943ce6be48cfa347251a3f3e6f15d'

# 'my_session' 세션 파일 이름 (동일 파일로 계속 유지됨)
client = TelegramClient('my_session', api_id, api_hash)

# 첫 로그인 시작
client.start()
print("✅ 세션 생성 완료! 'my_session.session' 파일이 저장되었습니다.")
