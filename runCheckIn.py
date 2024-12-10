import genshin as gs
import asyncio, os

async def claimDaily(client) :
  try: 
    reward = await client.claim_daily_reward()
  except Exception as e:
    print("Daily reward already claimed")
    print(e)
  else:
    print(f"Claimed {reward.amount}x {reward.name}")
  return

def main():
  #ltuid = int(os.getenv("LT_UID"))
  #ltoken = os.getenv("LT_TOKEN")
  emailAddr = os.getenv("EMAIL_ADDR")
  passWord = os.getenv("PASSWORD")
  client = gs.Client()
  cookies = asyncio.run(client.login_with_password(emailAddr,passWord))
  print(cookies)
  client.set_cookies(cookies)
  client.default_game = gs.Game.GENSHIN
  asyncio.run(claimDaily(client))

if __name__ == "__main__":
  main()
