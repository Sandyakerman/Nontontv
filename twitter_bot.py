import os
import tweepy

# Ambil kredensial dari GitHub Secrets
api_key = os.environ.get("TWITTER_API_KEY")
api_secret = os.environ.get("TWITTER_API_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# Inisialisasi Twitter API v2 Client
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def kirim_tweet():
    # Isi pesan tweet (bisa diubah atau diganti pakai generator teks otomatis)
    pesan = "Testing posting otomatis dari SandyAckerman Control Hub! 🚀"
    
    try:
        response = client.create_tweet(text=pesan)
        print("Berhasil posting tweet! Tweet ID:", response.data['id'])
    except Exception as e:
        print("Gagal posting tweet. Error:", str(e))

if __name__ == "__main__":
    kirim_tweet()
