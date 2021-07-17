import discord
from discord.ext import commands
client = discord.Client()

bot = commands.Bot(command_prefix = "!", description= "SPA Bot")

@bot.event
async def on_ready():
	print("Bot prêt")
@bot.command()
async def configurate(ctx):
	organisation = await ctx.guild.create_text_channel('organisation')

@bot.command()
async def newSPA(ctx):
	if ctx.channel.name == "organisation" :
		overwrites = {
			    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
			    ctx.author : discord.PermissionOverwrite(read_messages=True, administrator=True)

			}
		categorie = await ctx.guild.create_category("Soirée de "+ctx.author.name , overwrites=overwrites)
		await ctx.guild.create_text_channel("général",category=categorie)
		await ctx.guild.create_text_channel("Date",category=categorie)
		await ctx.guild.create_text_channel("Organisation",category=categorie)
		await ctx.guild.create_text_channel("Disponibilité",category=categorie)




@bot.command()
async def add(ctx,arg):
	server=ctx.guild
	j=0
	for k in server.members:
		if str(k.id) == str(arg):
			overwrites = {k: discord.PermissionOverwrite(read_messages=True)}
			for i in server.categories:
				if i.name[10:] ==(ctx.author.name):
					await i.edit(overwrites=overwrites)
					for channel in i.channels:
						await channel.edit(overwrites=overwrites)

				

bot.run(process.env.TOKEN) 
