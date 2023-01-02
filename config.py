# Bot token, получите у @botfather
token = 'xxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Путь к папке, в которой нужно создавать новые заметки
inbox_path = r'C:\your-obsidian-vault'

# Путь к папке, в которую нужно складывать полученные картинки
photo_path = r'C:\your-obsidian-vault\attachments'

# Если True, в сообщениях будет сохраняться форматирование (bold, italic, ccылки и т.п.)
# Если False, в сообщениях не будет сохраняться форматирование
format_messages = True

# Если True, голосовые сообщения будут распознаваться.
# Для этого должны быть установлены Whisper и FFMPEG
# Если False, голосовые сообщения не будут распознаваться.
recognize_voice = False

# Префикс имени файла заметки. К нему будет добавлена дата в формате ГГГГ-ММ-ДД
# Со значением по умолчанию итоговое имя файла будет иметь формат Telegram-2023-01-02_Notes.md
note_prefix = 'Telegram-'

# The string that will be added to the name after the note_prefix and the date in YYYY-MM-DD format
# If all the default config values are left be, the final name of the files will be Telegram-2023-01-02_Notes.md
note_postfix = '_Notes'

# Если в тексте сообщения встретится одно из указанных значений, сообщение будет преобразовано в задачу.
task_keywords = {'задач', 'сделать', 'todo'}

# Если в тексте сообщения встретится одно из указанных значений, к сообщению будет добавлен указанный далее тег
negative_keywords = {'негатив', 'печал'}

# Тег для добавления к тексту, в котором обнаружено ключевое слово
negative_tag = '#негатив'

# Идентификатор чата, который нужно читать. Сообщения в остальных чатах будут игнорироваться.
# Бот сообщает идентификатор чата при получении команды /start
# Этот параметр пока не используется
# my_chat_id = -xxxxxxxxx
