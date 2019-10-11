import discord

client = discord.Client()  # discord.Client() 대신 "app"를 써도 되게 만드는 부분이다.

token = "NjMxMTEwNDA1MjI1MzE2MzYy.XZyFhw.RdpsqSQdip-RWMmqGTGIi7h_xSg"
#봇의 토큰

# 봇이 구동되었을때 동작되는 코드부분이다.
@client.event
async def on_ready():
    print("Login as")  # 화면에 봇 이름, 아이디가 출력되는 부분이다.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    game = discord.Game("!help ChologBi")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:  # 보낸이가 봇일경우
        return None  # 동작하지 않는다

    if message.content.startswith("!help ChologBi"):
        await message.channel.send("Help----------------\n제작자: 집퍼 | 문의:  \n1. Skript 제작\n2. ChologCrew가입\n3. 초록비 유튜브 채널\n4. 초록비의 뜻\n5. 나이\n6. Skripter\n7. Builder\n8. 계약\n9. Skript 튜토리얼\n10. ChologCrew 만들어진날")

    if message.content.startswith("Skript 제작"):
        await message.channel.send("초록비#7626 으로 문의")
    if message.content.startswith("ChologCrew가입"):
        await message.channel.send("너 썩은물이냐?? 썩은물이면 내 동료가 되라!! 주소 https://discord.gg/MJuyQ2C")
    if message.content.startswith("초록비 유튜브 채널"):
        await message.channel.send("주소 https://www.youtube.com/channel/UCZ5VZd2hhGXvqG-dkDFkIwg/featured")
    if message.content.startswith("초록비의 뜻"):
        await message.channel.send("산성비다 어쯜래??")
    if message.content.startswith("나이"):
        await message.channel.send("내 나이는 삼겹살(헬레나님 죄송합니다)")
    if message.content.startswith("Skripter"):
        await message.channel.send("스크립트를 마스터한 사람")
    if message.content.startswith("Builder"):
        await message.channel.send("건축을 마스터 한 사람")
    if message.content.startswith("계약"):
        await message.channel.send("일단 프리미엄부터 사고나 말해")
    if message.content.startswith("Skript 튜토리얼"):
        await message.channel.send("Skript를 배우고 싶나?? 수강료나내!!(장난) 초록비#7626 으로 문의")
    if message.content.startswith("ChologCrew 만들어진날"):
        await message.channel.send("2019.10.10 매년 10월 10일마다 깊카 10,000원 뿌림!!(추첨)")
    if message.content.startswith("꼬냥이"):
        await message.channel.send("이스터에그 발견!! 다음 이스터에그 헬레나봇")

client.run(token)
