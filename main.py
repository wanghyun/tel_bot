# main.py

from telegram import Bot
from telegram.error import TelegramError

# ✅ 봇 정보
BOT_TOKEN = "8114452918:AAFmdQAeIsuxmIMxneYp0SU6lcqlyU2JEsA"  # TongTong77_bot

# ✅ 메시지 보낼 채팅방 리스트 (chat_id는 실제 숫자 ID로 바꿔야 함)
CHAT_IDS = [
    -1001234567890,  # 예시 채팅방 ID
    -1009876543210,
    # 여기에 100개까지 추가 가능
]

# ✅ 전송할 메시지와 이미지
PROMO_TEXT = """
🎉 [TongTong 이벤트 안내]

🔥 지금 확인하세요!  
👉 https://yourlink.com

문의는 @TongTong77_bot 로 주세요 😊
"""

IMAGE_PATH = "banner.jpg"  # 같은 폴더에 이미지 파일 배치

def send_promo():
    bot = Bot(token=BOT_TOKEN)
    success, fail = [], []

    for chat_id in CHAT_IDS:
        try:
            with open(IMAGE_PATH, 'rb') as image:
                bot.send_photo(chat_id=chat_id, photo=image, caption=PROMO_TEXT)
            print(f"[전송 완료] {chat_id}")
            success.append(chat_id)
        except TelegramError as e:
            print(f"[전송 실패] {chat_id}: {e}")
            fail.append(chat_id)
    return success, fail

if __name__ == "__main__":
    send_promo()
