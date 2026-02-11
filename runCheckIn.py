import genshin as gs
import asyncio
import os

async def claimDaily(client):
    try:
        reward = await client.claim_daily_reward()
    except Exception as e:
        print("Daily reward already claimed")
        print(e)
    else:
        print(f"Claimed {reward.amount}x {reward.name}")

async def main():
    emailAddr = os.getenv("EMAIL_ADDR")
    passWord = os.getenv("PASSWORD")

    client = gs.Client()
    cookies = await client.login_with_password(emailAddr, passWord)

    client.set_cookies(dict(cookies))
    client.default_game = gs.Game.GENSHIN

    await claimDaily(client)

if __name__ == "__main__":
    asyncio.run(main())
