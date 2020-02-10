# coding=utf-8
def step1():
    print(
        'Утка-маляр решила погулять.\n'
        'Взять ей зонтик?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Молодец!'
        'Сегодня день рождения друга бобра. Можно заглянуть на праздник и подарить ему зонтик.'
        'Навестим друга?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_friend()
    return step3_no_friend()


def step2_no_umbrella():
    print(
        'Молодец!'
        'Синоптики утверждают, что дождя сегодня не будет.'
        'Зато идет снег, и он завалил дверь домика 🏡 🦆.'
        'Как помочь утке погулять: развести у двери костер или прорубить дверь топором?'
    )
    option = ''
    options = {'развести у двери костер': True, 'прорубить дверь топором': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_fire()
    return step3_axe()


def step3_friend():
    print(
        'Бобер живет в ближайшем лесу. Добраться туда можно двумя способами: перелететь или пешком.'
        'Пешком долго, но безопасно. Лететь не больше получаса.'
        'Какой вариант выберем?'
    )
    option = ''
    options = {'перелететь': True, 'пешком': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step4_fly()
    return step4_no_fly()


def step3_no_friend():
    print(
        'Теперь 🦆 нечем заняться. Это был грустный день. 😞'
    )


def step3_fire():
    print(
        'О нет, кажется 🔥 вышел из под контроля!'
        'К сожалению 🦆 больше нет.'
    )


def step3_axe():
    print(
        'Утка-маляр на свободе. Но теперь в доме очень холодно.'
        '🦆 получила переохлаждение и никуда не пойдет. 😞'
    )


def step4_fly():
    print(
        'Жаль, очень жаль!'
        'Во время полета утку сбил местный охотник. ⚰'
    )


def step4_no_fly():
    print(
        'Отличный выбор!'
        'Безопасно, заодно и прогуляемся.'
        'Но идти долго. Надо взять с собой немного еды.'
        'В холодильнике осталось только 🥫 и 🍎'
        'Что возьмем с собой?'
    )
    option = ''
    options = {'консервы': True, 'яблоко': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step5_not_apple()
    return step5_apple()


def step5_not_apple():
    print(
        '🦆 взяла с собой консервы, но не смогла их открыть.'
        'Она была хорошей птицей.'
    )


def step5_apple():
    print(
        'По дороге через лес утке встретилась лиса 🦊'
        'Не уж то она съест утку? Может отдать ей яблоко'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step6_give_apple()
    return step6_not_give_apple()


def step6_give_apple():
    print(
        '🦆 отдала яблоко, но теперь ей нечего есть. А идти еще 3 дня'
        'Это конец'
    )


def step6_not_give_apple():
    print(
        'Ну и правильно, 🦊 все равно была сыта.'
        'Мы молодцы, 🦆 благополучно добралась до домика бобра и весело отметила день рождения!'
    )


if __name__ == '__main__':
    step1()
