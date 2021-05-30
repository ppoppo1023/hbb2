import discord
import random

client = discord.Client()

@client.event
async def on_message(message):
    if message.content == '섬삭은?':
        await message.channel.send('바보')
    if message.content == '커뉴는?':
        await message.channel.send('잘생겼다                                                       유료광고포함')
    if message.content == '샌즈는?':
        await message.channel.send('https://ww.namu.la/s/c80fdba0c6ddeb12406e44c16cb11af88a33a04e67b9a7a171a5112db448c41d505c52a9c7e01ddad827d0dabde3d1d1fd8608ff85e5a7bd771725283678b05f0b01aaa4f8ee501456f801603d10fb66cf2cfa6e4bcfde93609ca45cc5e727b0')
    if message.content == '!명령어':
        await message.channel.send(' ``섬삭은?`` ``커뉴는?`` ``샌즈는?`` ``슷칼봇은?`` ``배추봇은?`` ``한바는?`` ``우커바`` ``섬바삭보`` ``섬삭바보`` ``와`` ``?`` ** 이 외의 것은 니가 알아서 찾아 ㅡㅡ **')
    if message.content == '슷칼봇은?':
        await message.channel.send('거기 너! 지금당장이안철도를사라고')
    if message.content == '배추봇은?':
        await message.channel.send('유사메이플스토리')
    if message.content == '한바는?':
        await message.channel.send('**갓**')
    if message.content == '와':
        await message.channel.send('샌즈')
    if message.content == '우커바':
        await message.channel.send('ㅇ')
    if message.content == '섬바삭보':
        await message.channel.send('ㄹㅇㅋㅋㄹㅇㅋㅋㄹㅇㅋㅋ')
    if message.content == '섬삭바보':
        await message.channel.send('ㄹㅇㅋㅋ')
    if message.content == '?':
        await message.channel.send('미아핑추')
    if message.content == '실첵은?':
        await message.channel.send('바보')
    if message.content == '디스코드':
        await message.channel.send('섭폭')
    if message.content == '오크일꾼':
        await message.channel.send('https://media.discordapp.net/attachments/761073346971566113/770188807403208744/1597723742764.jpg?width=359&height=360')
    if message.content == '명월은?':
        await message.channel.send('명월이다')
    if message.content == '오':
        await message.channel.send('크')
    if message.content == '일':
        await message.channel.send('꾼')
    if message.content == '이프야 낚시':
        await message.channel.send('으엑 오류가... ```css\nCommand raised an exception: CacheNotLoaded: 캐시가 로드되어 있지 않습니다.```')
    if message.content == 'toswm':
        i = random.randint(1, 2)
        if i == 1:
            await message.channel.send("ㄹㅇ")
        if i == 2:
            await message.channel.send("ㄹㅇㅋㅋ")
    if message.content == '커뉴샌즈':
        await message.channel.send("샌\n\t\n즈")
    if message.content == '테스트':
        embed1 = discord.Embed(colour=0x00FFFF)
        embed1.set_thumbnail(url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDA0MjBfNzIg%2FMDAxNTg3MzEzMDQwNjg5.VU75lDZqt5UZBiv-mULDGFT5A6E-mCYxJuPLg7kdM6Eg.t1cj4Oy4DqL5yJ-U1hP9PNOX-eP5tBjQ3UaMmNNkWycg.PNG.soui1704%2FIMG_0842.PNG&type=sc960_832")
        embed1.add_field(name="그거 알아?", value="와 샌즈 ")
        await message.channel.send(embed=embed1)
    if message.content == '커뉴':
        await message.channel.send('바보')
    if message.content == '커뉴바보':
        await message.channel.send('ㄹㅇㅋㅋㅋㅋㅋㅋ컼ㅋㅋㅋㅋㅋㅋ늌ㅋㅋㅋㅋㅋ밬ㅋㅋㅋㅋㅋ봌ㅋㅋㅋㅋㅋ')
        
client.run("Nzc1OTc4Mzg3NDIzODg3Mzcw.X6uMMA.FzKFUpoNDZh0iQic3Mchm1GUXTU")
