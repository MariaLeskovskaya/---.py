import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup


bot = telebot.TeleBot('6093940768:AAEFTM9XJlBUKhFBcvy-D9Z7fRUu9aGCB1Q')

#url = 'https://lefood.menu/blyuda-iz-kuricy/'( обязательно доделаю, а пока ...)
#r = requests.get('https://lefood.menu/blyuda-iz-kuricy/')  #url
#r.encoding = 'UTF-8'
#soup = BeautifulSoup(r.text, 'html.parser')
#ank = soup.find_all('div', class ='banner-install-bottom-text')

chik = ['Продукты (на 6 порций)'
        'Курица - 1 шт.'
        '(или части курицы, например 8 куриных ножек)'
        'Сметана - 4 ст. ложки'
        'Лук репчатый - 1-2 шт.'
        'Чеснок - 1-2 зубчика'
        'Вода или куриный бульон - 200 мл.'
        'Масло подсолнечное - 2 ст. ложки'
        'Мука пшеничная - 0,5 ст. ложки'
        'Паприка молотая - 1 ч. ложка'
        'Базилик сушеный - 1 ч. ложка'
        'Соль - по вкусу'
        'Перец чёрный молотый - по вкусу'
        'Зелень (укроп или петрушка) - по вкусу.'
        'Подготовьте все необходимые продукты.'
        'Курицу промойте и разберите на порционные кусочки.'
        'Сковороду раскалите и выложите куски курицы кожей вниз. '
        'Если курица домашняя, кожа даст достаточное количество жира. '
        'В противном случае лучше раскалить сковороду с маслом, и на нём уже обжарить курицу.'
        'Итак, обжарьте куски курочки с двух сторон до румяной корочки.'
        'Добавьте нарезанный маленькими кусочками лук, обжарьте курицу с луком пару минут, затем добавьте измельчённый чеснок.'
        'Пока куриное мясо жарится, приготовьте соус - в кипятке или курином бульоне разведите сметану и муку. Комочков быть не должно.'
        'Залейте курицу сметанным соусом и доведите его до кипения.'
        'Всыпьте соль, чёрный молотый перец, сушеный базилик и молотую паприку.'
        'Перемешайте и тушите курицу в сметанном соусе под крышкой до готовности,'
        'примерно 20 минут (для домашней курицы понадобится больше времени). '
        'Готовое блюдо посыпьте измельчённой зеленью. Приятного аппетита! ']

por = ['Продукты (на 2 порции)'
        'Свинина (мякоть) - 400 г'
        'Лук репчатый - 60 г (1/2 шт.)'
        'Чеснок - 20 г (3 крупных зубчика)'
        'Соевый соус - 50 мл'
        'Мёд - 2 ст. ложки'
        'Уксус яблочный - 2 ст. ложки'
        'Масло растительное - 45 мл (3 ст. ложки)'
        'Соль - 1/2 ч. ложки (по вкусу)'
        'Чеснок сушёный молотый - 1/2 ч. ложки'
        'Перец чёрный молотый - 1/3 ч. ложки'
        'Перец красный острый молотый - 1/2 ч. ложки.'
        'Свинину сначала обжарим, а потом прогреем в густоватом соусе с мёдом, соевым соусом, уксусом и чесноком.'
        'Кисло-сладкий соус делает мясо очень мягким и нежным, а также придаёт ему изысканный вкус и аппетитный вид.']

fich2 = ['Тебе понадобится: 400 г рыбы, 4 ст.л. сметаны, '
         '2 ст.л. пармезана, 1 помидор,' 
         'укроп, зеленый лук, чеснок и специи.'
        'Приготовление: Мелко измельчи очищенный помидор,'
        'зеленый лук, укроп и чеснок. Смешай их со сметаной и тертым пармезаном.'
        'Натри филе рыбы специями, разложи по формочкам и залей соусом.'
        'Запекай около 20 минут при 180 градусах.']

df = ['Пожалуй, самое простое и уж точно беспроигрышное блюдо из говядины.'
        'Тебе понадобится: 500 г говядины, '
      '2 ст.л. соевого соуса, 2 ст.л. горчицы,'
      '1 головка чеснока, 1 ст.л. растительного масла,'
      'кунжут, перец.'
    'Приготовление: Смешай соевый соус с маринадом,'
    'обваляй говядину и оставь мариноваться.'
    'На сковороде обжарь зубчики чеснока и выброси,'
    'сразу же обжарь стейк по 2-2,5 минуты с каждой стороны.'
    'После сковороды заверни мясо в фольгу и оставь на 10 минут,'
    'а при подаче посыпь кунжутом.']

sheep = ['Ковурма шурпа из баранины'
         'Тебе понадобится: 3 л воды, 1 кг баранины,'
         '2 репчатых лука, 2 помидора, 3 болгарских перца,'
         '400 г картофеля, 3 зубчика чеснока,'
         '50 мл растительного масла, 0,5 ч.л. зиры, '
         '2 лавровых листа, 5 горошин душистого перца,'
         'полстручка острого перца, 1,5 ст.л. соли, зелень.'
        'Приготовление: Баранину слегка обжарь на быстром огне.'
         'Добавь измельченные лук, морковь, сладкий перец и туши 7 минут.'
         'Всыпь приправы, нарезанные картофель, '
         'помидоры, острый перец и готовь еще 5 минут.'
         'Залей все горячей водой и вари 40 минут.'
         'Посоли, присыпь шурпу измельченными чесноком и зеленью.']
ps = [' Паста Карбонара.'
      'Тебе понадобится:'
      '200 г пасты, 150 г бекона,'
      '150 мл 20% сливок, 50 г пармезана,'
      '3 зубчика чеснока, 3 яичных желтка,'
      'соль, молотый черный перец.'   
    'Приготовление: Измельчи чеснок и слегка обжарь.'
    'Добавь нарезанный соломкой бекон и обжарь до румяности.'
    'Взбей яичные желтки со специями, сливками и тертым сыром.'
    'Вылей к бекону, туда же добавь отваренную пасту,'
    'перемешай и пару минут прогрей.']

st = ['Салат «Королевский»' 
      'Тебе понадобится: 250 г крабовых палочек,'
      '4 сваренных вкрутую яйца,'
      '300 г твердого сыра, 100 г сухариков,'
      '1/2 лимона, 2 дольки чеснока, майонез.'
      'Приготовление: '
      'Смешай в салатнике нарезанные кубиками крабовые палочки'
      'и вареные яйца, измельченный чеснок, натертый на крупной терке сыр.'
      'Сбрызни салат соком лимона и заправь майонезом, а перед подачей посыпь сухариками.']

pp = ['Отбивные из кабачков'
      'Советуем подавать их с любым любимым соусом и обязательно есть горячими!'
      'Тебе понадобится: 2 кабачка, 3 зубчика чеснока,'
      '2 яйца, 1 стакан муки, '
      '1 стакан панировочных сухарей, специи.'
      'Приготовление: Нарежь кабачки пластинками'
      'по 5-7 мм и слегка отбей. '
      'Перемешай со специями и давленым чесноком,'
      'и оставь на 10 минут. Обмакни каждый ломтик в муку,'
      'взбитые яйца и сухари, и обжарь с двух сторон.']

bak = ['Чизкейк с творогом без выпечки'
       'Тебе понадобится: 200 г печенья,'
       '100 г сливочного масла, 200 г творога,'
       '200 г сметаны, 4 ст.л. сахара,'
       '30 г желатина, 220 мл воды, 100 мл любимого сока.'
        'Приготовление: Взбей печенье со сливочным маслом в блендере,'
       'выложи основу чизкейка в форму, утрамбуй и убери в холодильник.'
       'Замочи желатин в 100 мл холодной воды.'
       'Творог взбей со сметаной и сахаром в блендере.'
        'В 2/3 желатина добавь оставшуюся горячую воду,'
       'влей в творог и перемешай.'
       'Вылей массу на корж, накрой пленкой и убери на полтора часа в холодильник.'
       'Оставшийся желатин смешай с горячим соком до растворения,'
       'вылей на творожную основу и убери чизкейк обратно в холодильник еще на пару часов.']


@bot.message_handler(commands= ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте, я бот шеф-повар, который поможет вам найти рецепт на любой случай жизни. Пиши <привет> и начнем общение! Чтобы найти нужный рецепт, нажмите подходящую кнопку меню. Бот покажет вам разные вариации и способы его приготовления!')
@bot.message_handler(func=lambda message:True)
def get_text(message):
    if message.text == 'Привет' or message.text == 'привет':
        keyboard = types.InlineKeyboardMarkup()
        key_chicken = types.InlineKeyboardButton(text='Курица', callback_data='chicken')
        keyboard.add(key_chicken)
        key_pork = types.InlineKeyboardButton(text='Свинина', callback_data='pork')
        keyboard.add(key_pork)
        key_fish = types.InlineKeyboardButton(text='Рыба', callback_data='fish')
        keyboard.add(key_fish)
        key_beef = types.InlineKeyboardButton(text='Говядина', callback_data='beef')
        keyboard.add(key_beef)
        key_sheepmeat = types.InlineKeyboardButton(text='Баранина', callback_data='sheepmeat')
        keyboard.add(key_sheepmeat)
        key_pasta = types.InlineKeyboardButton(text='Паста', callback_data='pasta')
        keyboard.add(key_pasta)
        key_salad = types.InlineKeyboardButton(text='Салат', callback_data='salad')
        keyboard.add(key_salad)
        key_nutrition = types.InlineKeyboardButton(text='Здоровое питание', callback_data='nutrition')
        keyboard.add(key_nutrition)
        key_bakery = types.InlineKeyboardButton(text='Выпечка', callback_data='bakery')
        keyboard.add(key_bakery)
        bot.send_message(message.chat.id,'Привет, что сегодня будем готовить? Выбери из предложенных вариантов.',
                         reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю, я тупо бот.')

# создаем кнопки
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == 'chicken':
        key_chicken = types.InlineKeyboardMarkup()
        bot.send_message(call.message.chat.id, text='Курица – птица, которую мы готовим чаще всего. Блюда из курицы, цыпленка одни из самых востребованных. Курица довольно быстро готовится, вот рецепт: ', reply_markup= key_chicken)
        bot.send_message(call.message.chat.id,(chik))
    if call.data == 'pork':
        key_pork = types.InlineKeyboardMarkup()
        bot.send_message(call.message.chat.id, text='Мясо свинины можно сварить, запечь, зажарить или потушить - на ваш вкус. Вот ваш рецепт:', reply_markup=key_pork)
        bot.send_message(call.message.chat.id, (por))
    if call.data == 'fish':
        key_fish = types.InlineKeyboardMarkup()
        bot.send_message(call.message.chat.id, text='Отличный выбор! Вот рецептик: ', reply_markup=key_fish)
        bot.send_message(call.message.chat.id, (fich2))
    if call.data == 'beef':
        key_beef = types.InlineKeyboardMarkup()
        bot.send_message(call.message.chat.id, text='Блюда из говядины подаются как на первое, так и на второе: этот вид мяса сочетается с огромным количеством овощей, круп и специй. Рецепт:', reply_markup=key_beef)
        bot.send_message(call.message.chat.id, (df))
    if call.data == 'sheepmeat':
        key_sheepmeat = types.InlineKeyboardMarkup()
        bot.send_message(call.message.chat.id, text='Приготовление баранины в домашних условиях особенно популярно в среднеазиатской кухне. Спрашивая о том, как готовить баранину, хозяйки чаще всего интересуются тем, как приготовить баранину без запаха, вкусно. Рецепт:', reply_markup=key_sheepmeat)
        bot.send_message(call.message.chat.id, (sheep))
    if call.data == 'pasta':
        key_pasta= types.InlineKeyboardMarkup()
        bot.send_message(call.message.chat.id, text='Паста — блюдо итальянской кухни, состоящее из двух основных компонентов: любого макаронного изделия и соуса. Рецепт:', reply_markup=key_pasta)
        bot.send_message(call.message.chat.id, (ps))
    if call.data == 'salad':
        key_salad = types.InlineKeyboardMarkup()
        bot.send_message(call.message.chat.id, text='Салаты – самая разнообразная категория кулинарных блюд. Вкусных салатов множество. Например:  ', reply_markup=key_salad)
        bot.send_message(call.message.chat.id, (st))
    if call.data == 'nutrition':
        key_nutrition = types.InlineKeyboardMarkup()
        bot.send_message(call.message.chat.id, text='Здоровое питание − залог долгой жизни. Готовим сегодня: ', reply_markup=key_nutrition)
        bot.send_message(call.message.chat.id, (pp))
    if call.data == 'bakery':
        key_bakery = types.InlineKeyboardMarkup()
        bot.send_message(call.message.chat.id, text='Домашняя выпечка создает в доме непередаваемую атмосферу уюта и тепла. Ваш рецепт: ', reply_markup=key_bakery)
        bot.send_message(call.message.chat.id, (bak))



bot.polling(none_stop=True)


