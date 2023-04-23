import discord
import random
import asyncio
from game_questions import gamequestions
from history_questions import histquestions
from geo_questions import geoquestions
from anime_questions import animequestions

intents = discord.Intents.default()
client = discord.Client(intents=discord.Intents.all())

def get_questiongame():
    question = random.choice(gamequestions)
    random.shuffle(question['options'])
    options = {option: option for option in question["options"]}
    return {"question": question['question'], "options": options, "answer": question['answer']}

def get_questionanime():
    question = random.choice(animequestions)
    random.shuffle(question['options'])
    options = {option: option for option in question["options"]}
    return {"question": question['question'], "options": options, "answer": question['answer']}

def get_questionhist():
    question = random.choice(histquestions)
    random.shuffle(question['options'])
    options = {option: option for option in question["options"]}
    return {"question": question['question'], "options": options, "answer": question['answer']}

def get_questiongeo():
    question = random.choice(geoquestions)
    random.shuffle(question['options'])
    options = {option: option for option in question["options"]}
    return {"question": question['question'], "options": options, "answer": question['answer']}

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help') or message.content.startswith("!trivia"):
        await message.channel.send('''Trivia Topics:

Gaming Trivia - !game-trivia
History Trivia - !hist-trivia
Anime Trivia - !anime-trivia
Geography Trivia - !geo-trivia''')

    if message.content.startswith('!game-trivia'):
        question = get_questiongame()
        options = "\n".join([f"{option}" for option in question['options'].keys()])
        await message.channel.send(f```"{question['question']}\n{options}```")

        user = message.author

        def check(m):
            return (m.author == user) and ((m.content.lower() == question["answer"].lower()) or (m.content.lower() in [option.lower() for option in question["options"]]))

        try:
            user_answer = await asyncio.wait_for(client.wait_for('message', check=check), timeout=10.0)
            if check_answer(user_answer.content, question['answer']):
                await message.channel.send("Correct!")
            else:
                if user_answer.content.lower() in [option.lower() for option in question['options'].keys()]:
                    await message.channel.send(f"Incorrect. The correct answer was {question['answer']}.")
                else:
                    await message.channel.send("Invalid response.")
        except asyncio.TimeoutError:
            await message.channel.send(f"Time's up! The correct answer was '{question['answer']}'.")

    if message.content.startswith('!geo-trivia'):
        question = get_questiongeo()

        options = "\n".join([f"{option}" for option in question['options'].keys()])
        await message.channel.send(f```"{question['question']}\n{options}```")

        user = message.author

        def check(m):
            return (m.author == user) and ((m.content.lower() == question["answer"].lower()) or (m.content.lower() in [option.lower() for option in question["options"]]))

        try:
            user_answer = await asyncio.wait_for(client.wait_for('message', check=check), timeout=10.0)
            if check_answer(user_answer.content, question['answer']):
                await message.channel.send("Correct!")
            else:
                if user_answer.content.lower() in [option.lower() for option in question['options'].keys()]:
                    await message.channel.send(f"Incorrect. The correct answer was {question['answer']}.")
                else:
                    await message.channel.send("Invalid response.")
        except asyncio.TimeoutError:
            await message.channel.send(f"Time's up! The correct answer was '{question['answer']}'.")


    if message.content.startswith('!hist-trivia'):
        question = get_questionhist()
        options = "\n".join([f"{option}" for option in question['options'].keys()])
        await message.channel.send(f"```{question['question']}\n{options}```")

        user = message.author

        def check(m):
            return (m.author == user) and ((m.content.lower() == question["answer"].lower()) or (m.content.lower() in [option.lower() for option in question["options"]]))

        try:
            user_answer = await asyncio.wait_for(client.wait_for('message', check=check), timeout=10.0)
            if check_answer(user_answer.content, question['answer']):
                await message.channel.send("Correct!")
            else:
                if user_answer.content.lower() in [option.lower() for option in question['options'].keys()]:
                    await message.channel.send(f"Incorrect. The correct answer was {question['answer']}.")
                else:
                    await message.channel.send("Invalid response.")
        except asyncio.TimeoutError:
            await message.channel.send(f"Time's up! The correct answer was '{question['answer']}'.")

    if message.content.startswith('!anime-trivia'):
        question = get_questionanime()
        options = "\n".join([f"{option}" for option in question['options'].keys()])
        await message.channel.send(f"```{question['question']}\n{options}```")

        user = message.author

        def check(m):
            return (m.author == user) and ((m.content.lower() == question["answer"].lower()) or (m.content.lower() in [option.lower() for option in question["options"]]))

        try:
            user_answer = await asyncio.wait_for(client.wait_for('message', check=check), timeout=10.0)
            if check_answer(user_answer.content, question['answer']):
                await message.channel.send("Correct!")
            else:
                if user_answer.content.lower() in [option.lower() for option in question['options'].keys()]:
                    await message.channel.send(f"Incorrect. The correct answer was '{question['answer']}'.")
                else:
                    await message.channel.send("Invalid response.")
        except asyncio.TimeoutError:
            await message.channel.send(f"Time's up! The correct answer was {question['answer']}.")


client.run('TOKEN')



