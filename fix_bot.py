import re

with open("bot.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add import re if not present
if "import re" not in content:
    content = content.replace("import os\n", "import os\nimport re\n")

# 2. Add safe generation function
safe_func = """
# ─────────────────────────────────────────
#  Безопасная генерация ответа
# ─────────────────────────────────────────
BANNED_WORDS = [
    "сукины дети", "блядские дети", "дети блядей", "дети сук", "сучьи дети", "сукин сын", "сын суки",
    "мать", "отец", "папа", "мама", "батя", "родители", "брат", "сестра", "дети", "сын", "дочь", 
    "жена", "муж", "бабушка", "дедушка", "родня", "родственники", "семья", "родословная", "род", 
    "предки", "потомки", "мамка", "папка", "мамуля", "папуля", "бабка", "дед"
]
BANNED_PATTERN = re.compile(r'\\b(?:' + '|'.join(BANNED_WORDS) + r')\\b', re.IGNORECASE)

async def generate_safe_reply(model: str, messages: list, max_tokens: int, temperature: float) -> str:
    for _ in range(5):
        response = await client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        reply = response.choices[0].message.content.strip()
        if not BANNED_PATTERN.search(reply):
            return reply
        log.warning(f"Сработал фильтр! Сгенерировано: {reply}. Переделываем...")
    return "Я хотел тебя жестко попустить, но цензура не пропустила."

"""

if "generate_safe_reply" not in content:
    content = content.replace("# ─────────────────────────────────────────\n#  Ядро — запрос к Groq", safe_func + "# ─────────────────────────────────────────\n#  Ядро — запрос к Groq")

# 3. Replace direct API calls with safe API calls
# In get_rofl_reply
old_rofl = """    response = await client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        max_tokens=200,
        temperature=0.7,
    )
    
    reply = response.choices[0].message.content.strip()"""
new_rofl = """    reply = await generate_safe_reply(
        model="llama-3.1-8b-instant",
        messages=messages,
        max_tokens=200,
        temperature=0.7,
    )"""
content = content.replace(old_rofl, new_rofl)

# In talk_group
old_greet = """            response = await client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": GREET_PROMPT},
                    {"role": "user",   "content": "Поздоровайся с чатом по-своему"},
                ],
                max_tokens=150,
                temperature=0.9,
            )
            reply = response.choices[0].message.content.strip()"""
new_greet = """            reply = await generate_safe_reply(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": GREET_PROMPT},
                    {"role": "user",   "content": "Поздоровайся с чатом по-своему"},
                ],
                max_tokens=150,
                temperature=0.9,
            )"""
content = content.replace(old_greet, new_greet)

# In fas_command
old_fas = """        response = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT + "\\n\\n" + FAS_PROMPT.format(target_name=target)},
                {"role": "user", "content": f"Фас! Разорви его: {target}"},
            ],
            max_tokens=200,
            temperature=0.8,
        )
        reply = response.choices[0].message.content.strip()"""
new_fas = """        reply = await generate_safe_reply(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT + "\\n\\n" + FAS_PROMPT.format(target_name=target)},
                {"role": "user", "content": f"Фас! Разорви его: {target}"},
            ],
            max_tokens=200,
            temperature=0.8,
        )"""
content = content.replace(old_fas, new_fas)

# In random_talk_group
old_random = """        response = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT + "\\n\\n" + RANDOM_ROAST_PROMPT},
                {"role": "user", "content": f"{name} написал: {user_text}"},
            ],
            max_tokens=200,
            temperature=0.8,
        )
        reply = response.choices[0].message.content.strip()"""
new_random = """        reply = await generate_safe_reply(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT + "\\n\\n" + RANDOM_ROAST_PROMPT},
                {"role": "user", "content": f"{name} написал: {user_text}"},
            ],
            max_tokens=200,
            temperature=0.8,
        )"""
content = content.replace(old_random, new_random)

with open("bot.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Done patching.")
