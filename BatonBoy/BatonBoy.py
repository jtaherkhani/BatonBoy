import os
import discord
from dotenv import load_dotenv
from CustomClient import CustomClient

load_dotenv()
token = os.getenv('TOKEN')

client = CustomClient();
client.run(token)