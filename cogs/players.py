from discord.ext import commands
from cogs.utils.player import Player


class PlayersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """ゲームに参加するコマンド"""
        if self.bot.game_status == "nothing":
            return await ctx.send("現在ゲームはありません。")
        elif self.bot.game_status == "playing":
            return await ctx.send("現在ゲーム進行中です。")
        member = ctx.author
        for p in self.bot.players:
            if member.id == p.id:
                return await ctx.send("すでにゲームに参加しています。")
        player = Player(member.id)
        self.bot.players.append(player)
        await ctx.send(f"{member.mention}さんが参加しました。")

    @commands.command()
    async def leave(self, ctx):
        """ゲームから退出するコマンド"""
        if self.bot.game_status == "nothing":
            return await ctx.send("現在ゲームはありません。")
        elif self.bot.game_status == "playing":
            return await ctx.send("既にゲームが始まっているため退出できません。")
        member = ctx.author
        for p in self.bot.players:
            if member.id == p.id:
                self.bot.players.remove(p)
                return await ctx.send("ゲームから退出しました。")
        return await ctx.send("ゲームに参加していません。")


def setup(bot):
    bot.add_cog(PlayersCog(bot))
