from dotenv import dotenv_values
from discord_webhook import DiscordWebhook, DiscordEmbed
import json

def sendMessage(image,timesRan=0,failed=0):
    config = dotenv_values(".env")
    webhook = DiscordWebhook(url=config["WEBHOOK"])
    embed = DiscordEmbed(title="**Macro Status**", description=f'- Times run: `{timesRan}` - Times failed: `{failed}` - Times remaing: `0`', color="03b2f8")
    webhook.add_embed(embed)
    response = webhook.execute()

    json.loads(response.content.decode())["webhook_id"]

def editWebhook(webhookId=None,timesRan=0,failed=0):
    config = dotenv_values(".env")
    embed = DiscordEmbed(title="**Macro Status**", description=f'- Times run: `{timesRan}` - Times failed: `{failed}` - Times remaing: `0`', color="03b2f8")
    if webhookId == None:
        webhook = DiscordWebhook(url=config["WEBHOOK"])
    else:
        webhook = DiscordWebhook(url=config["WEBHOOK"], id=webhookId)
        #webhook.remove_embed(1)
    webhook.add_embed(embed)
    response = webhook.execute()
    return json.loads(response.content.decode())["webhook_id"]



