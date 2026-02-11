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

    client = gs.Client()
    cookies = {
        "ltoken_v2": os.getenv("LT_TOKEN"),
        "ltuid_v2": os.getenv("LT_UID")
        }
    #print(dict(cookies))
    client.set_cookies(dict(cookies))
    client.default_game = gs.Game.GENSHIN

    await claimDaily(client)

if __name__ == "__main__":
    asyncio.run(main())
