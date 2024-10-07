import time
import random
import datetime







print("Привет! Я виртуальный помощник VirtuAl!")
print(' ')
time.sleep(1)

username = input('Введите ваше имя: ')
print('Привет,', username + '!')
print()

print('Вот список команд:')
print("1. Игра")
print("2. Квиз")
print('3. Тесты')
print('4. Рандомайзер')
print('5. Советчик')
print('6. Предсказание на день')
print('7. Калькулятор')
print('8. Тех. Поддержка')

print(' ')
print('Чтобы увидеть список команд, напишите - commands.')
print('Чтобы выбрать, напишите номер команды.')



while True:
    

    time.sleep(1.5)
    print()
    print()
    command = input('Введите номер команды: ')
    print()

    if command.lower() == 'привет' or command.lower() == 'привет!' or command.lower() == 'hi':
        print('')
        print('Привет, чем я могу тебе помочь сегодня?')
        print('')

        

    elif command.lower() == 'как дела?' or command.lower() == 'как дела' or command.lower() == 'как у тебя дела?' or command.lower() == 'как у тебя дела':
        print('У меня все отлично! А как у вас?')
        kakdela = input()

        if kakdela.lower() == 'у меня тоже' or kakdela.lower() == 'тоже' or kakdela.lower() == 'у меня тоже!':
            print('Я рад, что у вас тоже все хорошо!')
        else:
            print('')

        

    elif command.lower() == 'спасибо':
        print('Всегда пожалуйста! Если вам понадобится что-то еще, обращайтесь!')

        

    elif command.lower() == 'broke' or command.lower() == 'error':
        for olololo in range(10000):
            print('error 404')

        

            
    
        
        
        
        
 
    elif command.lower() == 'команды' or command.lower() == 'commands':
        print(' ')
        print('Вот список команд, которые вы можете использовать:')
        print("1. Игра")
        print("2. Квиз")
        print('3. Тесты')
        print('4. Рандомайзер')
        print('5. Советчик')
        print('6. Предсказание на день')
        print('7. Калькулятор')
        print('8. Тех. Поддержка')
        
        print(' ')
    
    
    elif command.lower() == 'игра' or command == '1':
        print("Выберите тип игр, в которые хотите поиграть:")
        print("1. Текстовые игры")
        print('2. Игры с рандомом')
        
        print('')
        
        command_tip_igri = input('Введите номер нужного типа: ')
        
        if command_tip_igri.lower() == 'текстовые игры' or command_tip_igri == '1':
            print()
            print("Вот список Текстовых игр:")
            print("1. Три Двери")
            print('')
                
    
        
            command_textgame = input("Введите номер игры: ")
            print('')
        
            if command_textgame.lower() == "три двери"  or command_textgame == '1':
           
              print("ИГРА - 3 ДВЕРИ")
            
             
              print('Добро пожаловать,', username,'!')
              print()
              print('Чтобы продолжить напиши - Start')
              
              enter = input()  
              if enter.lower() == "start":
                    print('')
                    print('')
                    print('Предисловие:')
                    print('Вы идёте устраиваться на работу в компанию Kodland. Но перед самым входом в офис, вас похищает Zloddy и увозит в подвал' )
                    print('расположенный под офисом Kodland. Вы можете сбежать из этого подвала, но для этого вам предстоит выбрать правильную дверь.')
                    print('Ведь далеко не каждая дверь приведет вас в офис Kodland...')
                    
                    while True:
                        print('')
                        print('Напишите номер двери (1-3), в которую хотите войти')
                        
                        door = input()
                        if door == "1":
                            
                            print('')
                            print('Вы открыли первую дверь.')
                            print('Вы только подумали что вам повезло, как вдруг, будто из неоткуда, выскочил вампир и заговорил:')
                            
                            print()
                            print('- Здравствуй, человек. Чтобы выбраться из подвала тебе предстоит выйграть меня в Камень, Ножницы, Бумага!')
                            print('Если выйграешь меня, я так уж и быть выведу тебя на свободу, а если выйграю я, отправишься на корм акулам!')
                            
                            print()
                            print('Ну что ж, видимо нам придется сыграть с вампиром')
                            print()
                            
                            print('Если вы не помните правила этой игры, напишите - Rules, если помните, напишите - Yes')
                            otvet = input()
                            if otvet.lower() == 'правила' or otvet.lower() == 'rules':
                                print('')
                                print('В игре Камень - Ножницы - Бумага, двоим игрокам предстоит одновременно выбрать и написать один предмет из трёх - Камень, Ножницы или Бумагу, чей предмет окажется сильнее, тот и победил!')
                                print(' ')
                                print('СИЛА ПРЕДМЕТОВ')
                                print('Камень побеждает Ножницы.')
                                print('Ножницы побеждают Бумагу.')
                                print('Бумага побеждает Камень.')
                                
                            else:
                                print('')
                             
                            time.sleep(1)
                            print('Чтобы выбрать: Камень, напишите - 1, Ножницы, напишите - 2, Бумагу, напишите - 3')    
                            time.sleep(2)
                            
                            
                             
                
                            
                            print('')
                            print('Камень, Ножницы, Бумага')
                            time.sleep(1)
                            print(3)
                            time.sleep(0.5)
                            print(2)
                            time.sleep(0.5)
                            print(1)
                            time.sleep(0.5)
                            
                            kmn = input('Ваш выбор (1/2/3): ')
    
                            if kmn == '1':
                                kamenibumaga = 'Камень'
                                
                            if kmn == '2':
                                kamenibumaga = 'Ножницы'
                                
                            if kmn == '3':
                                kamenibumaga = 'Бумага'
                            time.sleep(0.5)    
                                    
                                
                                
                            print(username + ': Я выбираю - ',kamenibumaga)
                                
                            kmnotvet = random.choice(['Ножницы','Бумага','Камень'])
                                
                            print('VirtuAl: Я выбираю - ',kmnotvet)
                            
                            print()    
                            
                            if kmn == '1' and kmnotvet == 'Ножницы':
                                print('Поздравляю, вы победили!')
                                print('')
                                print('Вампир, как и обещал, вывел вас на свободу и вы успешно устроились на работу в офис Kodland!')
                                print('') 
                                print('YOU WIN!!!')
                                
                                
                                        
                                break    
                                    
                                
                            elif kmn == '2' and kmnotvet == 'Бумага':
                                print('Поздравляю, вы победили!')
                                print('')
                                print('Вампир, как и обещал, вывел вас на свободу и вы успешно устроились на работу в офис Kodland!')
                                print('') 
                                print('YOU WIN!!!')
    
                                
                            elif kmn == '3' and kmnotvet == 'Камень':
                                print('Поздравляю, вы победили!')
                                print('')
                                print('Вампир, как и обещал, вывел вас на свободу и вы успешно устроились на работу в офис Kodland!')
                                print('') 
                                print('YOU WIN!!!')
                                
                                
                                            
                            elif kmn == '1' and kmnotvet == 'Бумага':
                                print('Победил вампир...')
                                print('')
                                print('Вампир не стал медлить с выполнением своего обещания... Он грубо схватил вас и бросил в бассейн с акулами. От вас остался лишь клочок одежды...')
                                print('')
                                time.sleep(2)
                                print('Вы погибли.')
                                time.sleep(2)
                                print('')
                                print('Чтобы начать сначала, напишите - again')
                                again = input()
                                if again.lower() == 'again':
                                    print()
                                    
                                else:
                                    break
                                
                                    
                            elif kmn == '2' and kmnotvet == 'Камень':
                                print('Победил вампир...')
                                print('')
                                print('Вампир не стал медлить с выполнением своего обещания... Он грубо схватил вас и бросил в бассейн с акулами. От вас остался лишь клочок одежды...')
                                print('')
                                time.sleep(2)
                                print('Вы погибли.')
                                time.sleep(2)
                                print('')
                                print('Чтобы начать сначала, напишите - again')
                                again = input()
                                if again.lower() == 'again':
                                    print()
                                    
                                else:
                                    break
                                    
                            elif kmn == '3' and kmnotvet == 'Ножницы':
                                print('Победил вампир...')    
                                print('')
                                print('Вампир не стал медлить с выполнением своего обещания... Он грубо схватил вас и бросил в бассейн с акулами. От вас остался лишь клочок одежды...')
                                print('')
                                time.sleep(2)
                                print('Вы погибли.')
                                time.sleep(2)
                                print('')
                                print('Чтобы начать сначала, напишите - again')
                                again = input()
                                if again.lower() == 'again':
                                    print()
                                    
                                else:
                                    break
                                
                            elif kmn == '1' and kmnotvet == 'Камень':
                                print('У вас ничья!')
                                print()
                                print('Вампиру не понравилось то, что у вас ничья, и он отправил вас на старт.')
                                print()
                                time.sleep(2)
                                
                            elif kmn == '2' and kmnotvet == 'Ножницы':
                                print('У вас ничья!')
                                print()
                                print('Вампиру не понравилось то, что у вас ничья, и он отправил вас на старт.')
                                print()
                                time.sleep(2)
                                
                                
                            elif kmn == '3' and kmnotvet == 'Бумага':
                                print('У вас ничья!')
                                print()
                                print('Вампиру не понравилось то, что у вас ничья, и он отправил вас на старт.')
                                print()
                                time.sleep(2)
                                
                                
                                
                                
                            
                                
                                    
                            
                             
                                
                            
                            
                           
                            
                            
                        elif door == '2':
                            
                            print('')
                            print('Вы открыли вторую дверь.')
                            print('Вы идете по темному коридору, опасности нет.')
                            print('Вдруг дорога раздваивается.')
                            print('Вы можете пойти либо направо, либо налево.')
                            print('')
                            
                            
    
                            print('Чтобы идти направо, напишите - Right')
                            print('Чтобы идти налево, напишите - Left')
                            rightorleft = input()
                            
                            if rightorleft.lower() == 'right':
                                print('')
                                print('Вы повернули направо.')
                                print('Сразу за поворотом оказался обрыв.')
                                print('Вы упали и разбились.')
                                print('')
                                print('Вы проиграли.')
                                time.sleep(1)
                                print()
                                print("Чтобы начать сначала, напишите - Again")
                                print('Чтобы закончить напишите - Stop')
                                atamobriv = input()
                                print()
                            
                                if atamobriv.lower() == 'again':
                                    print()
                            
                                else:
                                    break
                                                                                    
                            elif rightorleft.lower() == 'left': 
                                print('')
                                print('Вы повернули налево.')
                                print('За поворотом оказался длинный коридор.')
                                print('')
                                
                                print('Чтобы идти дальше, напишите - Go')
                                print('Чтобы остановиться, напишите - Stop')
                                
                                goorstop = input()
                                if goorstop.lower() == 'go':
                                    print('')
                                    print('Вы пошли дальше.')
                                    print('Вы дошли до двери.')
                                    print('')
                                
                                    print('Чтобы зайти, напишите - Room')
                                    print('Чтобы не заходить, напишите - Hall')
                                
                                    roomorhall = input()
                                    if roomorhall.lower() == 'room':
                                        print('')
                                        print('Вы зашли в комнату.')
                                        print('Вдруг вы услышали, как дверь за вами захлопнулась.')
                                        print('В комнате выключился свет.')
                                        print('Вдруг комната начала наполняться ядовитым газом.')
                                        print('')
                                        print('Вы проиграли.')
                                        time.sleep(1)
                                        print()
                                
                                        print("Чтобы начать сначала, напишите - Again")
                                        print('Чтобы закончить напишите - Stop')
                                        roomihall = input()
                                        print()
                                
                                        if roomihall.lower() == 'again':
                                            print()
                                
                                        else:
                                            break
    
    
    
                                                    
                                                
                                    elif roomorhall.lower() == 'hall':
                                        print('')
                                        print('Вы не стали заходить в комнату. ')
                                        print('Вдруг вы услышали шаги позади вас.')
                                        print('Но обернутся вы так и не успели.')
                                        print('Вам в спину воткнули нож.')
                                        print('')
                                        print('Вы проиграли.')
                                                        
                                        time.sleep(1)
                                        print()
                                        print("Чтобы начать сначала напишите - Again")
                                        print('Чтобы закончить напишите - Stop')
                                                    
                                        hallllll = input()
                                        print()
                                                    
                                        if hallllll.lower() == 'again':
                                            print()
                                                            
                                        else:
                                            print()
                                            break
                                                        
                                                        
                                            
                                                        
                                    else:
                                        print('Такого варианта ответа нет.')
                                        print()
                                        time.sleep(1)    
                                                    
                                                    
                                                    
                                elif goorstop.lower() == 'stop': 
                                    print('')
                                    print('Вы не стали идти дальше по коридру.')
                                    print('Пока вы стояли и думали, что делать дальше, весь пол вокруг вас заполнился ядовитыми пауками.')
                                    print('Вы пытались от них убежать.')
                                    print('Но один из них все равно вас укусил.')
                                    print('Вы потеряли сознание...')
                                    print('')
                                    print('Вы проиграли.')
                                    time.sleep(1)
                                    print()
                                    print("Чтобы начать сначала, напишите - Again")
                                    print('Чтобы закончить напишите - Stop')
                                    goilistop = input()
                                    print()
                                                
                                    if goilistop.lower() == 'again':
                                            print()
                                                
                                    else:
                                        break
                                                
                                
                                
                                        
                                
                        
                                
                                
                        elif door == "3":  
                            print('')
                            print('Вы открыли третью дверь.')
                            print('Сразу за дверью оказался лифт.')
                            print('Вы зашли в него.')
                            print('Выберите этаж на который хотите подняться (1-3).')
                                
                            print('Чтобы выбрать, напишите номер этажа:') 
                            
                            viberietazhplz = input()
                            if viberietazhplz == '1':
                                print('')
                                print('Пока вы поднимались, трос лифта оборвался и лифт упал в шахту.')
                                print('Вы не пережили падения и разбились.')
                                print('')
                                print('Вы проиграли.')
                                time.sleep(1)
                                print()
                                print("Чтобы начать сначала, напишите - Again")
                                print('Чтобы закончить напишите - Stop')
                                liftupal = input()
                                print()
                            
                                if liftupal.lower() == 'again':
                                    print()
                            
                                else:
                                    break
                                                   
                                
                            elif viberietazhplz == '2': 
                                print('')
                                print('Вы поднялись на второй этаж.')
                                print('Перед вами большая, абсолютно белая комната')
                                print('В другом конце комнаты вы замечаете 2 лестницы')
                                print('Вы можете спустится на первый этаж, либо поднятся на 3 этаж.')
                                print('')
                                print('Чтобы спустится, напишите - Down')
                                print('Чтобы поднятся, напишите - Up')
                                
                                downorup = input()
                                if downorup.lower() == 'down':
                                    print('')
                                    print('Вы спустились на 1 этаж.')
                                    print('В комнате выключен свет, и вам абсолютно ничего не видно, кроме последней ступеньки.')
                                    print('Вы решаете испытать судьбу и пойти дальше.')
                                    print('Пола внизу не оказывается')
                                    print('Вы падаете вниз, в бассейн с крокодилами')
                                    print('Они вас съели...')
                                    print('')
                                    print('Вы проиграли.')
                                    
                                    time.sleep(1)
                                    print()
                                    print("Чтобы начать сначала, напишите - Again")
                                    print('Чтобы закончить напишите - Stop')
                                    usholdown = input()
                                    print()
                                
                                    if usholdown.lower() == 'again':
                                        print()
                                
                                    else:
                                        break
                                
                                elif downorup.lower() == 'up':  
                                    print('')
                                    print('Вы поднялись на третий этаж.')
                                    print('На третьем этаже вы увидели испуганного мужчину.')
                                    print('Вы подошли к нему, и как только он увидел вас, на его лице проступило облегчение.')
                                    print('Оказалось, что это работник компании Kodland, который обыскался вас.')
                                    print('Мужчина провел вас в офис компании и вы успешно устроились на работу!')
                                    print('')
                                    print('YOU WIN!!!')
                                    
                                    break
                                
                                else:
                                    print('Такого варианта нет.')
                            
                            elif viberietazhplz == '3':
                                print('')
                                print('Вы поднялись на третий этаж')
                                print('На третьем этаже вы увидели испуганного мужчину.')
                                print('Вы подошли к нему, и как только он увидел вас, на его лице проступило облегчение.')
                                print('Оказалось, что это работник компании Kodland, который обыскался вас.')
                                print('Мужчина провел вас в офис компании и вы успешно устроились на работу!.')
                                print('')
                                print('YOU WIN!!!')
                                
                                break
                                
                            else:
                                print()
                                print('Такого этажа нет.')
                                
                                
                        else:
                            print('Такой двери нет.')
                            
              else:
                  print('Такой команды не')
          
            else:
                print('Других текстовых игр пока что нет(')
        
        
        
        
        
        elif command_tip_igri.lower() == 'игры с рандомом' or command_tip_igri == '2':
            print()
            print("Вот список Игр c рандомом:")
            print("1. Камень. Ножницы. Бумага")
            print('2. Крестики-Нолики')
            print('3. Угадай число!')
            print()
                
    
        
            command_randomgame = input("Введите номер игры: ")
            print('')
        
            
                        
        
        
        
        
            if command_randomgame.lower() == 'камень ножницы бумага' or command_randomgame.lower() == 'кнб' or command_randomgame.lower() == 'камень, ножницы, бумага' or command_randomgame == '1':
                print('')
                
                print('Приветствую,' ,username, '!')
                
                playerkmn_score = 0 
                compkmn_score = 0
                
                print('')
                print('Думаю, вы знаете игру Камень-Ножницы-Бумага. Давайте в нее сыграем!')
                time.sleep(0.5)
                print('')
                time.sleep(1)
                print('По моей команде, вам надо будет выбрать - Камень, Ножницы или Бумагу')
                print('Чтобы выбрать: Камень, напишите - 1, Ножницы, напишите - 2, Бумагу, напишите - 3')
                print('')
                time.sleep(1)
                print('Если вы не помните правила этой игры, напишите - Rules, если помните, напишите Go:')
                kamennajabumaga = input()
                if kamennajabumaga.lower() == 'правила' or kamennajabumaga.lower() == 'rules':
                    print('')
                    print('В игре Камень - Ножницы - Бумага, двоим игрокам предстоит одновременно выбрать и написать один предмет из трёх -')
                    print('Камень, Ножницы или Бумагу, чей предмет окажется сильнее, тот и победил!')
                    print(' ')
                    print('СИЛА ПРЕДМЕТОВ')
                    print('Камень побеждает Ножницы.')
                    print('Ножницы побеждают Бумагу.')
                    print('Бумага побеждает Камень.')
                    
                else:
                    print('')
                
    
                
                time.sleep(2)
                
                while True:    
                    print('')
                    print('Камень, Ножницы, Бумага')
                    time.sleep(1)
                    print(3)
                    time.sleep(0.5)
                    print(2)
                    time.sleep(0.5)
                    print(1)
                    time.sleep(0.3)
                    print()
                    
                    hodigrokakmn = input('Ваш выбор (1/2/3): - ')
                    print()
                    if hodigrokakmn == '1':
                        print(username,': Я выбираю - Камень')
                        
                    elif hodigrokakmn == '2':
                        print(username,': Я выбираю - Ножницы')
                        
                    elif hodigrokakmn == '3':
                        print(username,': Я выбираю - Бумага')
                        
                    elif hodigrokakmn.lower() ==  'stop':
                        print('Ну стоп, так стоп...(')
                        print()
                        break
                    
                    else:
                        print('Такой команды нет.')
                        
                         
                    
                    
                    hodbotakmn = random.choice(['Ножницы','Бумага','Камень'])
                    
                    print('VirtuAl: Я выбираю - ',hodbotakmn,)
                    print()
                    
                    if (hodigrokakmn == '2') and (hodbotakmn == 'Бумага' or hodbotakmn == 'бумага'):
                        print('Поздравляю, вы победили!')
                        playerkmn_score += 1
                        
                        print()
                        print('У вас',playerkmn_score,'очков')
                        print('У VirtuAl',compkmn_score,'очков')
                        print()
                        
                        print("Чтобы продолжить играть, напишите - F")
                        print('Чтобы закончить напишите - Stop')
                        voprosleavekmn = input()
                        print()
                                
                        if voprosleavekmn.lower() == 'f':
                            print()
                                
                        else:
                            print('Игра окончена.')
                            break
                        
                    
                    elif (hodigrokakmn == '3') and (hodbotakmn == 'Камень' or hodbotakmn == 'камень'):
                        print('Поздравляю, вы победили!')
                        playerkmn_score += 1
                        
                        
                        print()
                        print('У вас',playerkmn_score,'очков')
                        print('У VirtuAl',compkmn_score,'очков')
                        print()
                        
                        print("Чтобы продолжить играть, напишите - F")
                        print('Чтобы закончить напишите - Stop')
                        voprosleavekmn = input()
                        print()
                                
                        if voprosleavekmn.lower() == 'f':
                            print()
                                
                        else:
                            print('Игра окончена.')
                            break
                    
                    elif (hodigrokakmn == '1') and (hodbotakmn == 'Ножницы'  or hodbotakmn == 'ножницы'):
                        print('Поздравляю, вы победили!')
                        playerkmn_score += 1
                        
                        print()
                        print('У вас',playerkmn_score,'очков')
                        print('У VirtuAl',compkmn_score,'очков')
                        print()
                        
                        print("Чтобы продолжить играть, напишите - F")
                        print('Чтобы закончить напишите - Stop')
                        voprosleavekmn = input()
                        print()
                                
                        if voprosleavekmn.lower() == 'f':
                            print()
                                
                        else:
                            print('Игра окончена.')
                            break
                                
                    elif (hodbotakmn == 'Ножницы' or hodbotakmn == 'ножницы') and (hodigrokakmn == '3'):
                        print('Победил VirtuAl.')
                        compkmn_score += 1
                        
                        print()
                        print('У вас',playerkmn_score,'очков')
                        print('У VirtuAl',compkmn_score,'очков')
                        print()
                        
                        print("Чтобы продолжить играть, напишите - F")
                        print('Чтобы закончить напишите - Stop')
                        voprosleavekmn = input()
                        print()
                                
                        if voprosleavekmn.lower() == 'f':
                            print()
                                
                        else:
                            print('Игра окончена.')
                            break
                        
                    elif (hodbotakmn == 'Бумага' or hodbotakmn == 'бумага') and (hodigrokakmn == '1'):
                        print('Победил VirtuAl.')
                        compkmn_score += 1
                        
                        print()
                        print('У вас',playerkmn_score,'очков')
                        print('У VirtuAl',compkmn_score,'очков')
                        print()
                        
                        print("Чтобы продолжить играть, напишите - F")
                        print('Чтобы закончить напишите - Stop')
                        voprosleavekmn = input()
                        print()
                                
                        if voprosleavekmn.lower() == 'f':
                            print()
                                
                        else:
                            print('Игра окончена.')
                            break
                        
                        
                    elif (hodbotakmn == 'Камень' or hodbotakmn == 'камень') and (hodigrokakmn == '2'):
                        print('Победил VirtuAl.')    
                        compkmn_score += 1
                        
                        print()
                        print('У вас',playerkmn_score,'очков')
                        print('У VirtuAl',compkmn_score,'очков')
                        print()
                        
                        
                        print("Чтобы продолжить играть, напишите - F")
                        print('Чтобы закончить напишите - Stop')
                        voprosleavekmn = input()
                        print()
                                
                        if voprosleavekmn.lower() == 'f':
                            print()
                                
                        else:
                            print('Игра окончена.')
                            break
                        
                    elif hodigrokakmn == '1' and hodbotakmn == 'Камень':
                        print('У вас ничья!')
                        
                        print()
                        print('У вас',playerkmn_score,'очков')
                        print('У VirtuAl',compkmn_score,'очков')
                        print()
                        
                        print("Чтобы продолжить играть, напишите - F")
                        print('Чтобы закончить напишите - Stop')
                        voprosleavekmn = input()
                        print()
                                
                        if voprosleavekmn.lower() == 'f':
                            print()
                                
                        else:
                            print('Игра окончена.')
                            break
                        
                    elif hodigrokakmn == '2' and hodbotakmn == 'Ножницы':
                        print('У вас ничья!')   
                        
                        print()
                        print('У вас',playerkmn_score,'очков')
                        print('У VirtuAl',compkmn_score,'очков')
                        print()
                        
                        
                        print("Чтобы продолжить играть, напишите - F")
                        print('Чтобы закончить напишите - Stop')
                        voprosleavekmn = input()
                        print()
                                
                        if voprosleavekmn.lower() == 'f':
                            print()
                                
                        else:
                            print('Игра окончена.')
                            break
                        
                    elif hodigrokakmn == '3' and hodbotakmn == 'Бумага':
                        print('У вас ничья!')    
                        
                        print()
                        print('У вас',playerkmn_score,'очков')
                        print('У VirtuAl',compkmn_score,'очков')
                        print()
                        
                        print("Чтобы продолжить играть, напишите - F")
                        print('Чтобы закончить напишите - Stop')
                        voprosleavekmn = input()
                        print()
                                
                        if voprosleavekmn.lower() == 'f':
                            print()
                                
                        else:
                            print('Игра окончена.')
                            time.sleep(1)
                            break
                    
            
            elif command_randomgame.lower() == 'крестики нолики' or command_randomgame.lower() == 'крестики-нолики' or command_randomgame == '2':
                print()
                print('КРЕСТИКИ-НОЛИКИ')
                print()
                print()
                board = list(range(1, 10))
                
                for i in range(3):
                    print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
                
                while True:
                    
                    print()
                    hod_usera = input('Введите, на какую клетку вы хотите поставить X: ')
                    print()
                
                   
                    if hod_usera.isdigit():
                        hod_usera = int(hod_usera)
                        if 1 <= hod_usera <= 9 and board[hod_usera - 1] != 'X' and board[hod_usera - 1] != 'O':
                            board[hod_usera - 1] = 'X'
                        else:
                            print('Некорректный ход. Пожалуйста, выберите свободную клетку от 1 до 9.')
                            
                    else:
                        print('Некорректный ввод. Введите число от 1 до 9.')
                        
                    
                    for i in range(3):
                        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")    
                    print()    
                        
                    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
                        print('Вы собрали 3 X в ряд')
                        break
                    
                    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
                        print('Вы собрали 3 X в ряд')
                        break
                        
                    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
                        print('Вы собрали 3 X в ряд')
                        break
                        
                    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
                        print('Вы собрали 3 X в ряд') 
                        break
                        
                    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
                        print('Вы собрали 3 X в ряд')
                        break
                        
                    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
                        print('Вы собрали 3 X в ряд')
                        break
                        
                    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
                        print('Вы собрали 3 X в ряд')
                        break
                        
                    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
                        print('Вы собрали 3 X в ряд') 
                        break
                        
                        
                        
                        
                    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
                        print('Virtual собрал 3 O в ряд')
                        break
                    
                    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
                        print('Virtual собрал 3 O в ряд')
                        break
                        
                    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
                        print('Virtual собрал 3 O в ряд')
                        break
                        
                    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
                        print('Virtual собрал 3 O в ряд')   
                        break
                        
                    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
                        print('Virtual собрал 3 O в ряд')
                        break
                        
                    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
                        print('Virtual собрал 3 O в ряд')
                        break
                        
                    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
                        print('Virtual собрал 3 O в ряд')
                        break
                        
                    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
                        print('Virtual собрал 3 O в ряд')
                        break
                    
                    
                    print()    
                    time.sleep(1)
                    print('Ход компьютера...')
                    time.sleep(2)
                    print()
                   
                    
                      
                
                    
                
                    hod_kompyutera = random.choice([i for i in range(1, 10) if board[i - 1] not in ['X', 'O']])
                    board[hod_kompyutera - 1] = 'O'
                
                 
                    
                    for i in range(3):
                        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
                        
                    print()    
                        
                    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
                        print('Вы собрали 3 X в ряд!')
                    
                    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
                        print('Вы собрали 3 X в ряд!')
                        
                    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
                        print('Вы собрали 3 X в ряд!')
                        
                    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
                        print('Вы собрали 3 X в ряд!')   
                        
                    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
                        print('Вы собрали 3 X в ряд!')
                        
                    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
                        print('Вы собрали 3 X в ряд!')
                        
                    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
                        print('Вы собрали 3 X в ряд!')
                        
                    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
                        print('Вы собрали 3 X в ряд!')    
                        
                        
                        
                        
                    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
                        print('Virtual собрал 3 O в ряд.')
                    
                    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
                        print('Virtual собрал 3 O в ряд.')
                        
                    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
                        print('Virtual собрал 3 O в ряд.')
                        
                    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
                        print('Virtual собрал 3 O в ряд.')   
                        
                    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
                        print('Virtual собрал 3 O в ряд.')
                        
                    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
                        print('Virtual собрал 3 O в ряд.')
                        
                    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
                        print('Virtual собрал 3 O в ряд.')
                        
                    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
                        print('Virtual собрал 3 O в ряд.')
                        
                        
            elif command_randomgame.lower() == 'угадай число!' or  command_randomgame.lower() == 'угадай число' or command_randomgame.lower() == '3':
                
                while True:
                    win = 0
                    print('Выберите сложность игры:')
                    print('Чтобы выбрать EASY - введите 1')
                    print('Чтобы выбрать HARD - введите 2')
                    print()
                    vibbb = input('')
                    
                    if vibbb.lower() == 'easy' or vibbb == '1':
                        ch100 = random.randint(1,100)
                        time.sleep(1.5)
                        print()
                        print('Число загадано!')
                        print()
                        while True:
                            if win == 0:
                                print()
                                ugg = int(input('Введите число: '))
                                
                                if ugg == ch100:
                                    print('Вы угадали число!')
                                    print()
                                    win += 1
                                    
                                elif ugg < ch100:
                                    print('Загаданное число больше!')
                                    
                                elif ugg > ch100:
                                    print('Загаданное число меньше!')
                                
                                
                                
                            else:
                                break
                        
                        print('Чтобы сыграть еще раз - введите 1')
                        print('Чтобы выйти - введите 2')
                        resultr = input('')
                        
                        if resultr == '1':
                            print()
                            
                        elif resultr == '2':
                            print()
                            break
                        
                        
                        
                    elif vibbb.lower() == 'hard' or vibbb == '2':
                        ch1000 = random.randint(1,1000)
                        time.sleep(1.5)
                        print()
                        print('Число загадано!')
                        print()
                        while True:
                            if win == 0:
                                print()
                                ugg = int(input('Введите число: '))
                                
                                if ugg == ch1000:
                                    print('Вы угадали число!')
                                    print()
                                    win += 1
                                    
                                elif ugg < ch1000:
                                    print('Загаданное число больше!')
                                    
                                elif ugg > ch1000:
                                    print('Загаданное число меньше!')
                                
                                
                                
                            else:
                                break
                        
                        print('Чтобы сыграть еще раз - введите 1')
                        print('Чтобы выйти - введите 2')
                        resultr = input('')
                        
                        if resultr == '1':
                            print()
                            
                        elif resultr == '2':
                            print()
                            break    
            
            else:
                print('Других игр с рандомом пока что нет(')
                
                
                
        elif command_tip_igri.lower() == 'игры с датами' or command_tip_igri == '3':    
            print()
            print("Вот список Игр c датами:")
            
            print("1. С какой знаменитостью у меня ДР в один день?")
            print('')
                
    
        
            command_datagame = input("Введите номер игры: ")
            print('')
                
            if command_datagame == '1':
                
                print('Привет. ')
                print('В этой программе, вы сможете узнать у кого из знаменитостей ДР в один день с вами!')
                print()
                
                
                datadr = input('Введите дату своего дня рождения в формате DAY.MONTH : ')
                
                #Январь

                j1 = random.choice(['актриса Мишель Мерсье', 'актер Колин Морган', 'актер Нил Бёргер'])
                j2 = random.choice(['актриса Аглая Шиловская', 'актриса Валерия Ланская', 'актриса Кейт Босуорт'])
                j3 = random.choice(['писатель Джон Толкин', 'певица Джису', 'актриса Алисен Даун'])
                j4 = random.choice(['физик Исаак Ньютон', 'актер Ренни Мирро', 'актриса Шарлин Йи'])
                j5 = random.choice(['певец Мэрилин Мэнсон', 'актер Клэнси Браун', 'певица Анастасия Осипова'])
                j6 = random.choice(['певец Macan', 'актер Норман Ридус', 'актер Эдди Редмэйн'])
                j7 = random.choice(['актриса Джоди Лонг', 'актер Роберт Шиэн', 'актер Джереми Реннер'])
                j8 = random.choice(['комик Дмитрий Романов', 'певец Дэвид Боуи', 'певец Элвис Пресли'])
                j9 = random.choice(['актриса Нина Добрев', 'актриса Джоэли Ричардсон', 'актриса Нина Гогаева'])
                j10 = random.choice(['актер Грант Тохатян', 'бизнесмен Джаред Кушнер', 'журналист Алена Долецкая'])
                j11 = random.choice(['певица Мэри Джей Блайдж', 'актер Андрей Малахов', 'актер Константин Хабенский'])
                j12 = random.choice(['актриса Рейчел Харрис', 'бизнесмен Джефф Безос', 'актриса Анна Полищук'])
                j13 = random.choice(['актер Милош Бикович', 'актер Александр Головин', 'актер Бо Мирчофф'])
                j14 = random.choice(['рэпер Кравц', 'актер Зак Гилфорд', 'актер Станислав Ярушин'])
                j15 = random.choice(['актриса Екатерина Волкова', 'актер Дмитрий Шаракоис', 'писатель Александр Грибоедов'])
                j16 = random.choice(['актер Джейк Эпштейн', 'певица Дженни Ким', 'модель Кейт Мосс'])
                j17 = random.choice(['актер Мейсон Темпл', 'актер Джим Керри', 'композитор Игорь Николаев'])
                j18 = random.choice(['актер Сэмюэл Джослин', 'актер Кевин Костнер', 'актер Дэйв Батиста'])
                j19 = random.choice(['блогер Ивангай', 'актриса Лидия Джюэтт', 'певец Алексей Воробьев'])
                j20 = random.choice(['актер Рино Уилсон', 'певица Ольга Бузова', 'танцовщица Анастасия Волочкова'])
                j21 = random.choice(['рэпер SLIMUS', 'актер Дмитрий Харатьян', 'ведущая Валерия Дергилева'])
                j22 = random.choice(['певица Нета Барзилай', 'рэпер Logic', 'актер Леонид Ярмольник'])
                j23 = random.choice(['рэпер XXXTentacion', 'актриса Джулия Джонс', 'модель Анастасия Решетова'])
                j24 = random.choice(['актриса Анжелика Каширина', 'актриса Джордан Клэр Роббинс', 'актер Мэттью Лиллард'])
                j25 = random.choice(['актриса Алиша Киз', 'певица Тина Кароль', 'актриса Светлана Камынина'])
                j26 = random.choice(['актриса Анна Большова', 'ведущий Леонид Парфенов', 'актер Кристиан Бейл'])
                j27 = random.choice(['певица Елена Ваенга', 'композитор Вольфган Моцарт', 'футболист Денис Глушаков'])
                j28 = random.choice(['актер Том Хоппер', 'актер Элайджа Вуд', 'актриса Ольга Кабо'])
                j29 = random.choice(['певец Адам Ламберт', 'писатель Антон Чехов', 'певец Дмитрий Маликов'])
                j30 = random.choice(['рэпер Pharaoh', 'актриса Фрида Ардженто', 'актер Кристиан Бейл'])
                j31 = random.choice(['рэпер Oxxxymiron', 'актриса Инна Королева', 'блогер Miss Katy'])
                
                
                
                
                
                #Февраль
                
                
                f1 = random.choice(['рэпер Рем Дигга', 'блогер Рома Желудь', 'певец Лев Лещенко'])
                f2 = random.choice(['актер Анируд Пишароди', 'певица Шакира', 'футболист'])
                f3 = random.choice(['актриса Диана Пожарская', 'певица Вера Брежнева', 'актриса Гленн МакКуин'])
                f4 = random.choice(['актриса Анна Невская', 'блогер Mister Max', 'актер Эдвин Рюдинг'])
                f5 = random.choice(['футболист Неймар', 'футболист Криштиану Роналду', 'актриса Барбара Херши'])
                f6 = random.choice(['актриса Ангелина Добророднова', 'актер Фабиан Пенье', 'актриса Кэти Наджими'])
                f7 = random.choice(['ведущая Алла Михеева', 'ведущий Антон Иванов', 'актер Эштон Кутчер'])
                f8 = random.choice(['ученый Дмитрий Менделеев', 'блогер Белла Порч', 'фигурист Роман Костомаров'])
                f9 = random.choice(['актриса Дарья Мельникова', 'актер Владислав Ветров', 'рэпер Feduk'])
                f10 = random.choice(['ведущая Роза Сябитова', 'актриса Людмила Артемьева', 'актер Владимир Зельдин'])
                f11 = random.choice(['актриса Дженнифер Энистон', 'певица Розэ', 'актер Евгений Капорин'])
                f12 = random.choice(['певец Егор Шип', 'актер Александр Соколовский', 'актер Джош Бролин'])
                f13 = random.choice(['актриса Пернилла Аугуст', 'певица Марина Демещенко', 'актриса Мина Сувари'])
                f14 = random.choice(['певец Pink Sweat$', 'певица Юлия Савичева', 'актриса Минди Робинсон'])
                f15 = random.choice(['актриса Анна Уколова', 'блогер Mia Boyka', 'актер Закари Гордон'])
                f16 = random.choice(['актриса Анастасия Акатова', 'певец The Weeknd', 'теннисист Джон Макинрой'])
                f17 = random.choice(['рэпер Моргенштерн', 'актриса Бонни Райт', 'баскетболист Майкл Джордан'])
                f18 = random.choice(['рэпер Dr. Dre', 'певец Джей-Хоуп', 'певица Варвара Визбор'])
                f19 = random.choice(['певец Витас', 'автор книг Марисса Мейер', 'певец Юрий Антонов'])
                f20 = random.choice(['певица Оливия Родриго', 'певица Рианна', 'актер Дмитрий Хрусталёв'])
                f21 = random.choice(['актер Джо Элвин', 'актер Илья Любимов', 'актер Алан Рикман'])
                f22 = random.choice(['I президент США - Джордж Вашингтон', 'актриса Геннея Уолтон', 'продюссер Юрий Антонов'])
                f23 = random.choice(['актриса Нэш, Ниси', 'модель Анна Чапман', 'актриса Кристин Дэвис'])
                f24 = random.choice(['бизнесмен Стив Джобс', 'актриса Полина Денисова', 'певец Трэйс Сайрус'])
                f25 = random.choice(['блогер Бустер', 'актер Ноа Джуп', 'актер Иван Жвакин'])
                f26 = random.choice(['певец Джонни Кэш', 'рэпер Ханза', 'певец Джонн Кэш'])
                f27 = random.choice(['актриса Элизабет Тейлор', 'футболист Динияр Билялетдинов', 'актриса Кейт Мара'])
                f28 = random.choice(['комик Гарик Харламов', 'певица Эмили де Форест', 'актриса Инджела Олссон'])
                f29 = random.choice(['писатель Тони Роббинс', 'певец Jony', 'изобретатель Герман Холлерит'])
                
                
                
                
                
                #Март
                
                m1 = random.choice(['певец Джастин Бибер', 'рэпер Нурминский', 'актриса Мирослава Карпович'])
                m2 = random.choice(['актер Пилу Асбек', 'актер Юрий Богатырев', 'актер Даниель Крейг'])
                m3 = random.choice(['актриса Алина Ланина', 'актер Джордж Миллер', 'певица Лиз Ассиа'])
                m4 = random.choice(['актриса Александра Кузенкина', 'композитор Антонио Вивальди', 'певец Борис Моисеев'])
                m5 = random.choice(['автор книг Сара Маас', 'актриса Елена Яковлева', 'пианист Даниил Трифонов'])
                m6 = random.choice(['актер Сергей Бурунов', 'актер Джеймс Саито', 'певица Татьяна Буланова'])
                m7 = random.choice(['автор книг Анна Хуанг', 'актриса Сарайю Блю', 'актриса Рэйчел Вайс'])
                m8 = random.choice(['актер Кит Коннор', 'певец Макс Барских', 'актриса Настя Ивлеева'])
                m9 = random.choice(['рэпер Шуга', 'блогер Хаби Лейм', 'космонавт Юрий Гагарин'])
                m10 = random.choice(['актер Кристер Фант', 'актриса Эмили Осмент', 'комик Данила Поперечный'])
                m11 = random.choice(['актер Джеффри Нордлинг', 'актер Джоэл Мэдден', 'актер Антон Ельчин'])
                m12 = random.choice(['певица Алена Швец', 'актриса Елена Аросьева', 'певец Алексей Чумаков'])
                m13 = random.choice(['актриса Ирина Алферова', 'Гарри Меллинг', 'актер Вадим Демчог'])
                m14 = random.choice(['актер Роман Курцын', 'комик Павел Воля', 'физик Альберт Эйнштейн'])
                m15 = random.choice(['актер Джай Кортни', 'актриса Любовь Аксенова', 'певица Алия Бхатт'])
                m16 = random.choice(['блогер Dava', 'актриса Александра Даддарио', 'модель Николь Трунфио'])
                m17 = random.choice(['актер Гэри Синиз', 'актриса Елизавета Арзамасова', 'космонавт Калпана Чавла'])
                m18 = random.choice(['актриса Лили Коллинз', 'президент Грузии - Саломе Зурабишвили', 'актриса Лили Коллинз'])
                m19 = random.choice(['певец Валерий Леонтьев', 'актер Брюс Уиллис', 'фуиболист Александр Кокорин'])
                m20 = random.choice(['комик Арсений Попов', 'актриса Нина Персиянинова', 'актер Джастин Х. Мин'])
                m21 = random.choice(['актер Андрей Бедняков', 'актер Гэри Олдмен', 'актер Скотт Иствуд'])
                m22 = random.choice(['певец Валерий Сюткин', 'актер Виктор Хориняк', 'актер Риз Уизерспун'])
                m23 = random.choice(['актриса Мишель Монаган', 'актриса Мишель Монахэн', 'актер Стивен Стрейт'])
                m24 = random.choice(['актриса Анна Азкарате', 'актер Джим Парсонс', 'актриса Элисон Ханниган'])
                m25 = random.choice(['певица Дина Гарипова', 'певец Элтон Джон', 'боксер Владимир Кличко'])
                m26 = random.choice(['актер Люка Браво', 'президент Эстонии - Алар Карис', 'модель Джессика Харт'])
                m27 = random.choice(['певица Полина Гагарина', 'певица Лиса', 'певица Мэрайя Кэри'])
                m28 = random.choice(['певица Леди Гага', 'писатель Максим Горький', 'актриса Меган Сури'])
                m29 = random.choice(['певец Владимир Пресняков', 'певица Ирина Круг', 'ведущий Александр Рогов'])
                m30 = random.choice(['актер Робби Колтрейн', 'певица Селин Дион', 'певица Флорида Чантурия'])
                m31 = random.choice(['актер Егор Корешков', 'композитор Йозеф Гайдн', 'композитор Иоганн Себастьян Бах'])
                
                
                
                #Апрель
                
                
                a1 = random.choice(['певец Монатик', 'певец Сергей Лазарев', 'актриса София Стеценко'])
                a2 = random.choice(['блогер Юлия Годунова', 'актер Майкл Фассбендер', 'актриса Эмма Майерс'])
                a3 = random.choice(['певица Аманда Байнс', 'актер Эдди Мерфи', 'актер Адам Скотт'])
                a4 = random.choice(['актер Роберт Дауни — младший', 'актер Дмитрий Нагиев', 'актриса Маргарита Шубина'])
                a5 = random.choice(['певец Дэниэл Сизар', 'актриса Фелиция Трудссон', 'актриса Лили Джеймс'])
                a6 = random.choice(['автор книг Ли Бардуго', 'актер Майкл Рукер', 'актер Зак Брафф'])
                a7 = random.choice(['актер Евгений Кошевой', 'певец Михаил Круг', 'актер Георгий Дронов'])
                a8 = random.choice(['актриса Елена Муравьева', 'актриса Робин Райт', 'певец Илья Прусикин'])
                a9 = random.choice(['блогер Eto Liana', 'актриса Эль Фэннинг', 'бизнесмен Марк Джейкобс'])
                a10 = random.choice(['актриса Елена Подкаминская', 'певица Noa Kirel', 'актриса Кайлер Ли'])
                a11 = random.choice(['певец Дункан Лоуренс', 'актриса Никита Уггла', 'актриса Морган Лили'])
                a12 = random.choice(['актриса Ретта', 'актер Андрей Гайдулян', 'певица Монсеррат Кабалье'])
                a13 = random.choice(['певец Сергей Шнуров', 'блогер Сыендук', 'певец Михаил Шуфутинский'])
                a14 = random.choice(['актер Питер Капальди', 'актриса Умберли Гонсалес', 'актриса Кристина Асмус'])
                a15 = random.choice(['художник Леонардо да Винчи', 'певица Алла Пугачева', 'актриса Ольга Волкова', 'Эмма Уотсон'])
                a16 = random.choice(['актриса Мидори Френсис', 'ведущий Иван Ургант', 'блогер Герман Черных'])
                a17 = random.choice(['актриса Дженнифер Гарнер', 'певица Валерия', 'актер Шон Бин'])
                a18 = random.choice(['актриса Аглая Тарасова', 'актер Кевин Ранкин', 'актриса Анастасия Калашникова'])
                a19 = random.choice(['комик Антон Шастун', 'актер Игнасио Серричио', 'бизнесмен Шуг Найт'])
                a20 = random.choice(['рэпер Баста', 'блогер Алена Венум', 'диктатор Адольф Гитлер'])
                a21 = random.choice(['королева Елизавета II', 'певица Dorofeeva', 'актриса Лили Д. Мур'])
                a22 = random.choice(['блогер Mamix', 'актер Алексей Лукин', 'актер Куэ Лоуренс'])
                a23 = random.choice(['актриса Юлия Паршута', 'модель Джиджи Хадид', 'актриса Джейми Кинг'])
                a24 = random.choice(['певица Юлиана Караулова', 'певица Келли Кларксон', 'актриса Ребекка Мэйдер'])
                a25 = random.choice(['актер Кэмерон Бродер', 'актриса Филиппин Леруа-Больё', 'певец Мэвл'])
                a26 = random.choice(['писатель Уильям Шекспир', 'актер Григорий Сиятвинда', 'актриса Анна Старшенбаум'])
                a27 = random.choice(['певец Стас Михайлов', 'актриса Салли Хокинс', 'актер Дэррен Барнет'])
                a28 = random.choice(['актриса Мадлен Харрис', 'писатель Терри Прачетт', 'певица Мелани Мартинес'])
                a29 = random.choice(['актриса Ума Турман', 'актер Дэниел Дэй-Льюис', 'актриса Мишель Пфайффер'])
                a30 = random.choice(['король Швеции - Карл XVI Густав', 'актер Сергей Друзьяк', 'певец Филипп Киркоров'])
                
                
                
                
                
                #Май
                
                mj1 = random.choice(['актриса Галина Безрук', 'блогер Чарли Дамелио', 'певица Софья Таюрская'])
                mj2 = random.choice(['актер Дуэйн Джонсон', 'певица Лили Аллен', 'актер Филипп Бледный'])
                mj3 = random.choice(['актриса Кристина Хендрикс', 'ведущая Ида Галич', 'актер Данила Козловский'])
                mj4 = random.choice(['актер Денис Дорохов', 'певица Настя Каменских', 'рэпер Миша Крупин'])
                mj5 = random.choice(['певец Крис Браун', 'актер Челси Кларк', 'певица Адель'])
                mj6 = random.choice(['актриса Александра Ребенок', 'актер Джордж Клуни', 'актер Владимир Этуш'])
                mj7 = random.choice(['блогер MrBeast', 'композитор Пётр Чайковский', 'актер Брекин Мейер'])
                mj8 = random.choice(['певец Потап', 'актер Стивен Амелл', 'актер Нора Арнезедер'])
                mj9 = random.choice(['актер Федор Бондарчук', 'президент Словении - Наташа Пирц-Мусар', 'певец Брейсон Сайрус'])
                mj10 = random.choice(['актриса Каззи Дэвид', 'актриса Одетт Эннэбл', 'ведущий Влад Листьев'])
                mj11 = random.choice(['певица Инстасамка', 'композитор Константин Меладзе', 'художник Сальвадор Дали'])
                mj12 = random.choice(['актер Рами Малек', 'певица Виктория Дайнеко', 'актриса Кэтрин Хепберн'])
                mj13 = random.choice(['певец Джонни Логан', 'актер Александр Рыбак', 'певица Маша Распутина'])
                mj14 = random.choice(['бизнесмен Марк Цукерберг', 'актер Тим Рот', 'актер Ярослав Бойко'])
                mj15 = random.choice(['писатель Михаил Булгаков', 'модель Стелла Максвелл', 'певец Рома Кенга'])
                mj16 = random.choice(['блогер Артур Бабич', 'писательница Катерина Сильванова', 'журналист Такер Карлсон'])
                mj17 = random.choice(['актер Станислав Дужников', 'Президент Казахстана - Касым-Жомарт Токаев', 'актриса Анастасия Денисова'])
                mj18 = random.choice(['актриса Виталия Корниенко', 'певица Марина Кравец', 'писательница Елена Малисова'])
                mj19 = random.choice(['блогер Катя Клэп', 'певец Позитив', 'президент Литвы - Гитанас Науседа'])
                mj20 = random.choice(['актер Рузиль Минекаев', 'писатель Борис Акунин', 'актер Гоша Куценко'])
                mj21 = random.choice(['блогер Полина Велл', 'актриса Бери Гервайз', 'актер Никита Пресняков'])
                mj22 = random.choice(['ведущий Антон Птушкин', 'актриса Анастасия Уколова', 'певец Сергей Жуков'])
                mj23 = random.choice(['ведущая Лариса Гузеева', 'продюссер DJ Smash', 'певица Бланка Стайков'])
                mj24 = random.choice(['певица Кристина Орбакайте', 'президент Молдовы - Майя Санду', 'актриса Брианна Хоуи'])
                mj25 = random.choice(['актер Итан Сапли', 'певица Кристина Орбакайте', 'актер Майк Майерс'])
                mj26 = random.choice(['певица Анжелика Варум', 'актриса Рича Мурджани', 'актер Константин Белошапка'])
                mj27 = random.choice(['писатель Крис Колфер', 'ученый Лоуренс Краусс', 'актер Пол Беттани'])
                mj28 = random.choice(['певица Кайли Миноуг', 'актриса Кэри Маллиган', ''])
                mj29 = random.choice(['бывший президент США - Джон Кеннеди', 'актер Грегг Салкин', 'певица Мелани Браун'])
                mj30 = random.choice(['космонавт Алексей Леонов', 'актриса Мария Берсенева', 'певица Мари Фредрикссон'])
                mj31 = random.choice(['певица Нормани Кордей', 'актриса Брук Шилдс', 'актер Колин Фаррелл'])
                
                
                #Июнь
                
                jn1 = random.choice(['певица Монеточка', 'блогер Хабиб', 'писательница Колин Маккалоу'])
                jn2 = random.choice(['писатель Фредрик Бакман', 'актриса Карина Зверева', 'актер Закари Куинто'])
                jn3 = random.choice(['рэпер Скриптонит', 'актер Всеволод Шиловский', 'ведущая Юлия Барановская'])
                jn4 = random.choice(['актриса Анджелина Джоли', 'певец Эльдар Гасымов', 'певец Игорь Бурнышев'])
                jn5 = random.choice(['блогер А4', 'автор книг Рик Риордан', 'блогер Гусейн Гасанов'])
                jn6 = random.choice(['поэт Александр Пушкин', 'актриса Эшли Парк', 'актер Самвел Тадевосян'])
                jn7 = random.choice(['актер Дин Мартин', 'музыкант Александр Дольский', 'актриса Анден Мини'])
                jn8 = random.choice(['актер Фрэнк Грилло', 'актриса Эрика Шмидт', 'рэпер Канье Уэст'])
                jn9 = random.choice(['актер Джонни Депп', 'рэпер Xcho', 'актер Майкл Джей Фокс'])
                jn10 = random.choice(['певица МакSим', 'композитор The D.O.C.', 'актриса Лили Собески'])
                jn11 = random.choice(['комик Дмитрий Позов', 'актер Магнус Росманн', 'актер Питер Динклэйдж'])
                jn12 = random.choice(['ведущий Алексей Пивоваров', 'актриса Алиса Гребенщикова', 'блогер Диана Шурыгина'])
                jn13 = random.choice(['певец Монс Сельмерлёв', 'президент Румынии - Клаус Йоханнис', 'актер Кристофер Эванс'])
                jn14 = random.choice(['бывший президент США - Дональд Трамп', 'ведущая Регина Тодоренко', 'актриса Люси Хейл'])
                jn15 = random.choice(['актриса Анна Ковальчук', 'рэпер Айс Кьюб', 'актер Андрей Леонов'])
                jn16 = random.choice(['рэпер MC Ren', 'актер Тупак Шакур', 'актриса Ольга Кузьмина'])
                jn17 = random.choice(['ведущий Дмитрий Комаров', 'рэпер Кендрик Ламар', 'хоккеист Никита Кучеров'])
                jn18 = random.choice(['актриса Юлия Агафонова', 'комик Максим Галкин', 'блогер Николай Соболев'])
                jn19 = random.choice(['разработчик этого помощника 🤩', 'блогер Pat04Chek', 'актриса Зои Салдана'])
                jn20 = random.choice(['актриса Николь Кидман', 'актер Стивен Фрирз', 'актер Мари Гийяр'])
                jn21 = random.choice(['блогер Karrambaby', 'певица Лана Дель Рей', 'президент Словакии - Зузана Чапутова'])
                jn22 = random.choice(['танцор Дмитрий Красилов', 'актер Брюс Кэмпбелл', 'актер Дональд Фэйсон'])
                jn23 = random.choice(['поэтесса Анна Ахматова', 'комик Сергей Орлов', 'певец Валерий Меладзе'])
                jn24 = random.choice(['певица Анна Асти', 'футболист Лионель Месси', 'актер Иэн Глен'])
                jn25 = random.choice(['певец Егор Крид', 'актриса Маргарита Аброськина', 'актер Тимур Бекмамбетов'])
                jn26 = random.choice(['блогер Юля Гаврилина', 'певица Ариана Гранде', 'рэпер 9 грамм'])
                jn27 = random.choice(['актер Мэттью Льюис', 'певица Алсу', 'актер Дрейк Белл'])
                jn28 = random.choice(['бизнесмен Илон Маск', 'актер Александр Панкратов', 'актриса Кеана Мари'])
                jn29 = random.choice(['рэпер DJ Pooh', 'актер Михаил Тарабукин', 'певец Сосо Павлиашвили'])
                jn30 = random.choice(['актер Питер Аутербридж', 'боксер Майк Тайсон', 'певица Шерил Коул'])
                
                
                
                #Июль
                
                jl1 = random.choice(['актер Сергей Епишев', 'принцесса Диана Уэльская', 'актриса Татьяна Орлова'])
                jl2 = random.choice(['певица Ёлка', 'актер Павел Деревянко', 'ведущая Алёна Водонаева'])
                jl3 = random.choice(['актер Том Круз', 'актриса Сара Вайсгласс', 'актер Денис Рожков'])
                jl4 = random.choice(['рэпер Post Malone', 'актер Дмитрий Назаров', 'актриса Юлия Зимина'])
                jl5 = random.choice(['блогер Милс Кел', 'актер Максим Коновалов', 'актриса Маха Горячева'])
                jl6 = random.choice(['актриса Кристина Каширина', 'актер Кевин Харт', 'актер Дмитрий Лысенков'])
                jl7 = random.choice(['автор книг Виктория Шваб', 'писатель Захар Прилепин', 'актриса Ив Хьюсон'])
                jl8 = random.choice(['автор книг Стефани Гарбер', 'актер Дмитрий Певцов', 'актриса Малахат Аббасова'])
                jl9 = random.choice(['рэпер Элджей', 'актер Том Хэнкс', 'актер Роберт Капрон'])
                jl10 = random.choice(['актер Юрий Стоянов', 'актер Магнус Эрнер', 'актриса София Вергара'])
                jl11 = random.choice(['актриса Екатерина Вилкова', 'певица Алессия Кара', 'актер Роб Хипс'])
                jl12 = random.choice(['актриса Полина Максимова', 'певец Эльдар Джарахов', 'актриса Екатерина Кузнецова'])
                jl13 = random.choice(['актер Борис Клюев', 'певец Мэд Цай', 'композитор Мирослав Скорик'])
                jl14 = random.choice(['комик Ваня Усович', 'певица Пелагея', 'актриса Юлия Куварзина'])
                jl15 = random.choice(['актер Иэн Армитидж', 'писатель Кристофер Холт', 'актриса Диана Крюгер'])
                jl16 = random.choice(['певец Леонид Агутин', 'певец Григорий Лепс', 'актриса Виктория Тарасова'])
                jl17 = random.choice(['актер Джонатан Поттс', 'певица Кали Учис', 'актриса Александра Назарова'])
                jl18 = random.choice(['актриса Келли Райлли', 'актриса Кристен Белл', 'актер Чейс Кроуфорд'])
                jl19 = random.choice(['продюсер Доминик Джокер', 'поэт Владимир Маяковский', 'музыкант Брайан Мэй'])
                jl20 = random.choice(['актер Майкл Парк', 'актриса Сандра О', 'модель Жизель Бюндхен'])
                jl21 = random.choice(['танцор Мигель', 'актриса Нонна Гришаева', 'актер Робин Уильямс'])
                jl22 = random.choice(['певица Селена Гомес', 'блогер EdisonPts', 'актер Джавон Уолтон'])
                jl23 = random.choice(['певица Клава Кока', 'актер Дэниел Рэдклифф', 'актер Александр Олешко'])
                jl24 = random.choice(['актриса Анна Пэкуин', 'писатель Александр Дюма', 'танцовщица Дженнифер Лопес'])
                jl25 = random.choice(['актриса Наталья Бочкарева', 'футболист Халк', 'актер Мэтт Леблан'])
                jl26 = random.choice(['певица Зара', 'певец Мик Джаггер', 'актриса Хелен Миррен'])
                jl27 = random.choice(['блогер Глент', 'актер Сергей Лавыгин', 'автор книг Кассандра Клэр'])
                jl28 = random.choice(['блогер Егор Жуков', 'актриса Юлия Захарова', 'рэпер Фогель'])
                jl29 = random.choice(['актер Хенесис Родригес', 'актриса Т. Дж. Макгиббон', 'актер Стивен Дорфф'])
                jl30 = random.choice(['певец Финнеас О’Коннелл', 'актер Арнольд Шварценеггер', 'режиссер Кристофер Нолан'])
                jl31 = random.choice(['писательница Джоан Роулинг', 'ведущий Леонид Якубович', 'хоккеист Евгений Малкин'])
                
                
                
                #Август
                
                ag1 = random.choice(['актер Кристен Холден-Рид', 'актриса Салли Прессман', 'актер Джейсон Момоа'])
                ag2 = random.choice(['рэпер Джиган', 'актер Сэм Уортингтон', 'актер Денис Никифоров'])
                ag3 = random.choice(['актриса Мэми Гаммер', 'модель Эванджелин Лилли', 'журналист Александр Невзоров'])
                ag4 = random.choice(['политик Барак Обама', 'актер Коул Спраус', 'актер Джеймс Таппер'])
                ag5 = random.choice(['актер Джонатан Силвермен', 'космонавт Нил Армстронг', 'актер Джесси Уильямс'])
                ag6 = random.choice(['актриса Янина Студилина', 'актриса Марина Могилевская', 'режиссер Вера Фармига'])
                ag7 = random.choice(['певица София Ротару', 'блогер Егорик', 'модель Шарлиз Терон'])
                ag8 = random.choice(['певец Шон Мендес', 'актер Кит Кэррадайн', 'теннисист Роджер Федерер'])
                ag9 = random.choice(['блогер Макс Максимов', 'актриса Людмила Дмитриева', 'певица Елена Максимова'])
                ag10 = random.choice(['модель Кайли Дженнер', 'актер Антонио Бандерас', 'политик Герберт Гувер'])
                ag11 = random.choice(['актер Крис Хемсворт', 'актер Оскар Кучера', 'программист Стивен Возняк'])
                ag12 = random.choice(['актриса Валерия Федорович', 'актер Дэн Бейрн', 'актер Юсуф Гейтвуд'])
                ag13 = random.choice(['певец Стас Пьеха', 'актриса Лидия Арефьева', 'режиссер Альфред Хичкок'])
                ag14 = random.choice(['актриса Мила Кунис', 'модель Хэлли Берри', 'актриса Надежда Бахтина'])
                ag15 = random.choice(['рэпер Тимати', 'император Наполеон I', 'певица Нюша'])
                ag16 = random.choice(['актер Стив Карелл', 'актриса Эванна Линч', 'актриса Рина Гришина'])
                ag17 = random.choice(['актер Николай Добрынин', 'певец Томас Хидон', 'актер Роберт Де Ниро'])
                ag18 = random.choice(['режиссер Эдвард Нортон', 'актер Патрик Суэйзи', 'режиссер Роберт Редфорд'])
                ag19 = random.choice(['актер Михаил Башкатов', 'блогер Marmok', 'певец Nate Dogg'])
                ag20 = random.choice(['актер Леонард Терфельт', 'писатель Говард Лавкрафт', 'певица Деми Ловато'])
                ag21 = random.choice(['певица Мари Краймбери', 'певица Кейси Масгрейвсм', 'актриса Ким Кэттролл'])
                ag22 = random.choice(['актер Евгений Михеев', 'писатель Рэй Брэдбери', 'актер Колм Фиори'])
                ag23 = random.choice(['актер Игорь Петренко', 'певица Алена Апина', 'модель Валерия Лукьянова'])
                ag24 = random.choice(['актер Руперт Гринт', 'актриса Элизабет Дебики', 'режиссер Сарик Андреасян'])
                ag25 = random.choice(['актер Билли Рэй Сайрус', 'актер Александр Скарсгард', 'актриса Рэйчел Билсон'])
                ag26 = random.choice(['певица Земфира', 'актер Маколей Калкин', 'актриса Кеке Палмер'])
                ag27 = random.choice(['актриса Фаина Раневская', 'певица Джамала', 'актер Аарон Пол'])
                ag28 = random.choice(['актер Джек Блэк', 'актер Арми Хаммер', 'актер Луис Гусман'])
                ag29 = random.choice(['певица Лиа Мишель', 'певец Майкл Джексон', 'актриса Марина Александрова'])
                ag30 = random.choice(['актриса Анна Фроловцева', 'актриса Марин Айрленд', 'актер Тихон Жизневский'])
                ag31 = random.choice(['певица Сара Рамирес', 'актер Ричард Гир', 'балерина Матильда Кшесинская'])
                
                
                #Сентябрь
                
                s1 = random.choice(['певец Чонгук', 'актриса Ирина Антоненко', 'актриса Дарья Мороз'])
                s2 = random.choice(['актер Остин Абрамс', 'актер Киану Ривз', 'актриса Синтия Уотрос'])
                s3 = random.choice(['актер Клас Хартелиус', 'актер Синтия Уотрос', 'актриса Евгения Брик'])
                s4 = random.choice(['актриса Виктория Моролес', 'актриса Айони Скай', 'актер Лазло Джонс'])
                s5 = random.choice(['актриса Эмми Рэвер-Лэмпман', 'певец Фредди Меркьюри', 'актриса Роуз Макгоуэн'])
                s6 = random.choice(['певец David Kushner', 'певец Юрий Шатунов', 'актер Робин Аткин Даунс'])
                s7 = random.choice(['певица Нигяр Джамал', 'рэпер Eazy-E', 'актриса Ян Гэ'])
                s8 = random.choice(['актер Джулиан Ричингс', 'актер Владимир Епифанцев', 'актер Рэй Фишер'])
                s9 = random.choice(['певица Кети Топурия', 'писатель Лев Толстой', 'актер Стивен Богерт'])
                s10 = random.choice(['певец Александр Ревва', 'певица Лариса Долина', 'блогер Himan'])
                s11 = random.choice(['космонавт Герман Титов', 'актер Фёдор Добронравов', 'актриса Лада Дэнс'])
                s12 = random.choice(['певец Ким Намджун', 'актриса Наталья Щукина', 'актер Гидеон Эмери'])
                s13 = random.choice(['актриса Лили Рейнхарт', 'певец Найл Хоран', 'композитор Александр Розенбаум'])
                s14 = random.choice(['актер Фёдор Воронцов', 'продюссер Нас', 'певица Эми Уайнхаус'])
                s15 = random.choice(['актер Том Харди', 'режиссер Оливер Стоун', 'принц Гарри'])
                s16 = random.choice(['певец Ник Джонас', 'актриса Эми Полер', 'боксер Микки Рурк'])
                s17 = random.choice(['актриса Риту Эрийа', 'певица Бьянка', 'футболист Павел Мамаев'])
                s18 = random.choice(['актер Эйдан Галлахер', 'певица Анна Нетребко', 'актер Джейсон Судейкис'])
                s19 = random.choice(['актриса Василина Юсковец', 'художник Покрас Лампас', 'боксер Костя Цзю'])
                s20 = random.choice(['писатель Джордж Мартин', 'актер Колтон Гоббо', 'актриса Софи Лорен'])
                s21 = random.choice(['президент Латвии - Эдгарс Ринкевичс', 'писатель Стивен Кинг', 'актер Джеймс Лежер'])
                s22 = random.choice(['актер Том Фелтон', 'писательница Розамунда Пилчер', 'актер Майкл Грациадей'])
                s23 = random.choice(['рэпер Гуф', 'рэпер ST', 'актриса Кэйли ДеФер'])
                s24 = random.choice(['актер Джо Лок', 'певица Алина Бараз', 'актриса Александра Бортич'])
                s25 = random.choice(['блогер Брайн Мапс', 'актер Уилл Смит', 'актриса Антония Джентри'])
                s26 = random.choice(['актриса Александра Флоринская', 'актер Мэнни Монтана', 'писательница Стейс Крамер'])
                s27 = random.choice(['певица Mitski', 'актриса Дженна Ортега', 'певица Ани Лорак'])
                s28 = random.choice(['актер Калеб Эмери', 'актер Владимир Турчинский', 'актриса Наоми Уоттс'])
                s29 = random.choice(['певец Jah Khalib', 'певица Холзи', 'актриса Ксения Буравская'])
                s30 = random.choice(['актер Эзра Миллер', 'актриса Моника Беллуччи', 'актриса Марион Котийяр'])
                
                
                #Октябрь
                
                o1 = random.choice(['актер Ричард Харрис', 'певец Niletto', 'актер Иззи Стэннард'])
                o2 = random.choice(['рэпер Andy Panda', 'актер Илья Малаков', 'актер Андрей Данилко'])
                o3 = random.choice(['актер Клайв Оуэн', 'поэт Сергей Есенин', 'актриса Валентина Рубцова'])
                o4 = random.choice(['актриса Дакота Джонсон', 'певица Елена Катина', 'актер Аристарх Венес'])
                o5 = random.choice(['блогер Юлия Коваль', 'актриса Кейт Уинслет', 'актер Один Байрон'])
                o6 = random.choice(['актер Данте Браун', 'актер Николай Шрайбер', 'актриса Оливия Тирлби'])
                o7 = random.choice(['блогер Марьяна Ро', 'актер Аарон Эшмор', 'актриса Сабрина Грдевич'])
                o8 = random.choice(['актриса Анна Тараторкина', 'певица Белла Торн', 'поэтесса Марина Цветаева'])
                o9 = random.choice(['рэпер L’One', 'актер Егор Бероев', 'модель Белла Хадид'])
                o10 = random.choice(['бизнесмен Павел Дуров', 'актер Филипп Янковский', 'актриса Анастасия Сиваева'])
                o11 = random.choice(['блогер Юрий Дудь', 'актер Игорь Верник', 'блогер Lady Diana'])
                o12 = random.choice(['блогер Елена Райтман', 'актер Максим Лагашкин', 'актриса Виктория Исакова'])
                o13 = random.choice(['актриса Кейт Уолш', 'певец Чимин', 'актриса Киле Санчес'])
                o14 = random.choice(['ведущий Тимур Родригез', 'актриса Миа Васиковска', 'ведущая Ирена Понарошку'])
                o15 = random.choice(['певец Николай Басков', 'поэт Михаил Лермонтов', 'блогер Маргарита Дьяченкова'])
                o16 = random.choice(['писатель Оскар Уайльд', 'певица Loreen', 'певец Джон Мэйер'])
                o17 = random.choice(['рэпер Эминем', 'музыкант Иван Дорн', 'актер Джон Мэйер'])
                o18 = random.choice(['актер Сергей Безруков', 'блогер Катя Адушкина', 'певица Светлана Лобода'])
                o19 = random.choice(['комик Богдан Лисевский', 'актер Майкл Гэмбон', 'ведущая Леся Никитюк'])
                o20 = random.choice(['рэпер Снуп Догг', 'модель Кэндис Свейнпол', 'актер Вигго Мортенсен'])
                o21 = random.choice(['певец Käärijä', 'актриса Ким Кардашьян', 'певец Кейн Браун'])
                o22 = random.choice(['актриса Анна Кошмал', 'композитор Ференц Лист', 'актер Кристофер Ллойд'])
                o23 = random.choice(['актер Райан Рейнольдс', 'актриса Наталья Гудкова', 'актриса Джессика Строуп'])
                o24 = random.choice(['блогер PewDiePie', 'актер Дэвид Кастанеда', 'рэпер Дрейк'])
                o25 = random.choice(['певец Ваня Дмитриенко', 'блогер Карина Кросс', 'актер Михаил Галустян'])
                o26 = random.choice(['актриса Эмилия Кларк', 'футболист Дмитрий Сычев', 'актер Дилан Макдермотт'])
                o27 = random.choice(['певец Слава Марлоу', 'актриса Келли Осборн', 'актер Артур Смольянинов'])
                o28 = random.choice(['актер Михаил Трухин', 'актриса Екатерина Старшова', 'бизнесмен Билл Гейтс'])
                o29 = random.choice(['актер Владимир Виноградов', 'актриса Екатерина Шпица', 'актер Руфус Сьюэлл'])
                o30 = random.choice(['актер Иван Янковский', 'модель Иванка Трамп', 'футболист Диего Марадона'])
                o31 = random.choice(['блогер Влад Кобяков', 'актер Джон Кэнди', 'актриса Маралл Насири'])
                
                
                #Ноябрь
                
                n1 = random.choice(['блогер +100500', 'президент Чехии - Петр Павел', 'актриса Мария Порошина'])
                n2 = random.choice(['актер Шахрух Хан', 'актриса Елена Захарова', 'актер Дэвид Швиммер'])
                n3 = random.choice(['певец Александр Градский', 'режиссер Дольф Лундгрен', 'ведущий Сергей Дружко'])
                n4 = random.choice(['рэпер Шон Комбс', 'актриса Галина Боб', 'актер Мэттью Макконахи'])
                n5 = random.choice(['актриса Зоя Кайдановская', 'журналистка Ксения Собчак', 'актер Джастин Корнуэлл'])
                n6 = random.choice(['ведущая Яна Чурикова', 'актер Анатолий Васильев', 'актриса Салли Филд'])
                n7 = random.choice(['актриса Ангелина Варганова', 'певица Лорд', 'актриса Елена Бирюкова'])
                n8 = random.choice(['певица SZA', 'актриса Тара Рид', 'актер Олег Меньшиков'])
                n9 = random.choice(['рэпер Френч Монтана', 'писатель Иван Тургенев', 'актер Эрик Дэйн'])
                n10 = random.choice(['автор книг Холли Блэк', 'ведущая Тина Канделаки', 'писатель Нил Гейман'])
                n11 = random.choice(['актер Леонардо Ди Каприо', 'блогер Валя Карнавал', 'актриса Олеся Железняк'])
                n12 = random.choice(['певец Омар Рудберг', 'актриса Меган Маллалли', 'актер Райан Гослинг'])
                n13 = random.choice(['комик Сергей Матвиенко', 'актриса Стелла Хадженс', 'певица Ольга Орлова'])
                n14 = random.choice(['актер Семен Трескунов', 'актер Андрей Бурковский', 'певица Лолита Милявская'])
                n15 = random.choice(['актер Реймонд Эблэк', 'актриса Кэтлин Роуз Перкинс', 'актриса Шейлин Вудли'])
                n16 = random.choice(['автор книг Наталья Щерба', 'барабанщик Макс Морандо', 'актриса Мэгги Джилленхол'])
                n17 = random.choice(['актер Тимур Еремеев', 'актриса Людмила Гаврилова', 'режиссер Софи Марсо'])
                n18 = random.choice(['писатель Алан Мур', 'актриса Эллисон Толман', 'актер Эльдар Рязанов'])
                n19 = random.choice(['актриса Мария Ильюхина', 'ученый Михаил Ломоносов', 'фигуристка Евгения Медведева'])
                n20 = random.choice(['президент США - Джо Байден', 'актер Павел Трубинер', 'актер Риз Уэйкфилд'])
                n21 = random.choice(['певец Олег Майами', 'актриса Джена Мэлоун', 'режиссер Голди Хоун'])
                n22 = random.choice(['писатель Виктор Пелевин', 'актер Джейми Кэмпбелл Бауэр', 'актриса Карина Мишулина'])
                n23 = random.choice(['певец Макс Корж', 'певица Майли Сайрус', 'писатель Алексей Иванов'])
                n24 = random.choice(['актриса Дженнифер Робертсон', 'певец Том Оделл', 'модель Ханде Эрчел'])
                n25 = random.choice(['блогер Дмитрий Куплинов', 'певица Кэти Кэссиди', 'политик Аугусто Пиночет'])
                n26 = random.choice(['певец Прохор Шаляпин', 'танцовщица Рита Ора', 'актер Антон Макарский'])
                n27 = random.choice(['блогер Саша Спилберг', 'актер Брюс Ли', 'футболист Александр Кержаков'])
                n28 = random.choice(['певица Zivert', 'актер Андрей Ургант', 'комик Виктория Складчикова'])
                n29 = random.choice(['актер Эндрю Маккарти', 'писатель Клайв Стейплз Льюис', 'рэпер The Game'])
                n30 = random.choice(['блогер Литвин', 'певица Дора', 'актер Александр Лыков'])
                
                
                #Декабрь
                
                dc1 = random.choice(['актер Дэвид Хорнсби', 'актер Нестор Карбонелл', 'певица Зои Кравиц'])
                dc2 = random.choice(['певица Бритни Спирс', 'певица Бритни Спирс', 'комик Владимир Маркони'])
                dc3 = random.choice(['актер Рейнбоу Сан Фрэнкс', 'актриса Мила Сивацкая', 'актер Никита Тарасов'])
                dc4 = random.choice(['певец Чин', 'актер Даниил Белых', 'рэпер Jay-Z'])
                dc5 = random.choice(['блогер Маша Вэй', 'актер Джейк Ти Остин', 'поэт Фёдор Тютчев'])
                dc6 = random.choice(['блогер Даня Милохин', 'актер Натан Митчелл', 'актриса Эшли Мадекве'])
                dc7 = random.choice(['певица Катя Ли', 'актер Александр Феклистов', 'актер Николас Холт'])
                dc8 = random.choice(['актер Петер Карлберг', 'актер Уткарш Амбудкар', 'актер Дов Тифенбах'])
                dc9 = random.choice(['актер Джарен Льюисон', 'актриса Татьяна Кравченко', 'певец Artik'])
                dc10 = random.choice(['певица Таисия Повалий', 'ведущая A(Z)IZA', 'певица Айза Анохина'])
                dc11 = random.choice(['автор книг Колин Гувер', 'певец Андрей Макаревич', 'рэпер DJ Yella'])
                dc12 = random.choice(['актриса Дженнифер Коннелли', 'актер Сергей Светлаков', 'писатель Николай Карамзин'])
                dc13 = random.choice(['певица Тейлор Свифт', 'рэпер Miyagi', 'актер Джейми Фокс'])
                dc14 = random.choice(['актер Томми Веттринг', 'хореограф Дарья Сагалова', 'певица Ванесса Хадженс'])
                dc15 = random.choice(['блогер Аня Покров', 'комик Алексей Щербаков', 'актер Юрий Колокольников'])
                dc16 = random.choice(['певица Анна Седокова', 'композитор Людвиг ван Бетховен', 'актер Тео Джеймс'])
                dc17 = random.choice(['фигуристка Елизавета Туктамышева', 'актриса Елена Ксенофонтова', 'певица Милла Йовович'])
                dc18 = random.choice(['актер Брэд Питт', 'певица Билли Айлиш', 'певица Сиа'])
                dc19 = random.choice(['автор книг Брэндон Сандерсон', 'актер Тиль Швайгер', 'актер Павел Баршак'])
                dc20 = random.choice(['диджей DJ MEG', 'футболист Килиан Мбаппе', 'актриса Елизавета Боярская'])
                dc21 = random.choice(['президент Франции - Эмманюэль Макрон', 'блогер Дима Масленников', 'модель Снежана Самохина'])
                dc22 = random.choice(['комик Нурлан Сабуров', 'актер Рэйф Файнс', 'актер Марк Богатырев'])
                dc23 = random.choice(['актриса Анастасия Макеева', 'блогер Арина Данилова', 'политик Максим Кац'])
                dc24 = random.choice(['певец Дима Билан', 'музыкант Лемми', 'певец Рики Мартин'])
                dc25 = random.choice(['певица Саша Савельева', 'бизнесмен Олег Тиньков', 'композитор Константин Кинчев'])
                dc26 = random.choice(['актриса Евгения Добровольская', 'актер Михаил Боярский', 'актриса Мария Горбань'])
                dc27 = random.choice(['актер Тимоти Шаламе', 'актриса Эмили де Рэвин', 'актер Жерар Депардье'])
                dc28 = random.choice(['актриса Мэгги Смит', 'актер Дензел Вашингтон', 'певец Салвадор Собрал'])
                dc29 = random.choice(['актер Джуд Лоу', 'актриса Элисон Бри', 'актриса Лилли Вачовски'])
                dc30 = random.choice(['актер Кирилл Плетнев', 'певец Ви', 'певица Элли Голдинг'])
                dc31 = random.choice(['артист Николай Цискаридзе', 'композитор Пак Чэсан', 'модель Алина Санько'])










                if datadr == '01.01':
                    print('')
                    
                    
                    print('У тебя день рождения 1 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j1)
                    
                    
                    
                    
                elif datadr == '02.01':
                    print('')
                    
                    
                    print('У тебя день рождения 2 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j2)
                    
                    
                    
                    
                elif datadr == '03.01':
                    print('')
                    
                    
                    print('У тебя день рождения 3 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j3)    
                    
                elif datadr == '04.01':
                    print('')
                    
                    
                    print('У тебя день рождения 4 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j4)
                    
                    
                    
                elif datadr == '05.01':
                    print('')
                    
                    
                    print('У тебя день рождения 5 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j5)
                    
                    
                    
                elif datadr == '06.01':
                    print('')
                    
                    
                    print('У тебя день рождения 6 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j6)
                    
                    
                    
                elif datadr == '07.01':
                    print('')
                    
                    
                    print('У тебя день рождения 7 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j7)
                    
                    
                    
                elif datadr == '08.01':
                    print('')
                    
                    
                    print('У тебя день рождения 8 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j8)
                    
                    
                    
                elif datadr == '09.01':
                    print('')
                    
                    
                    print('У тебя день рождения 9 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j9)
                    
                    
                    
                elif datadr == '10.01':
                    print('')
                    
                    
                    print('У тебя день рождения 10 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j10)
                    
                    
                    
                elif datadr == '11.01':
                    print('')
                    
                    
                    print('У тебя день рождения 11 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j11)
                    
                    
                    
                elif datadr == '12.01':
                    print('')
                    
                    print('У тебя день рождения 12 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j12)
                    
                    
                    
                elif datadr == '13.01':
                    print('')
                    
                    
                    print('У тебя день рождения 13 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j13)
                    
                    
                    
                elif datadr == '14.01':
                    print('')
                    
                    
                    print('У тебя день рождения 14 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j14)
                    
                    
                    
                elif datadr == '15.01':
                    print('')
                    
                    
                    print('У тебя день рождения 15 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j15)
                    
                    
                    
                elif datadr == '16.01':
                    print('')
                    
                    
                    print('У тебя день рождения 16 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j16)
                    
                    
                    
                elif datadr == '17.01':
                    print('')
                    
                    
                    print('У тебя день рождения 17 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j17)
                    
                    
                    
                elif datadr == '18.01':
                    print('')
                    
                    
                    print('У тебя день рождения 18 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j18)
                    
                    
                    
                elif datadr == '19.01':
                    print('')
                    
                    
                    print('У тебя день рождения 19 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j19)
                    
                    
                    
                elif datadr == '20.01':
                    print('')
                    
                    
                    print('У тебя день рождения 20 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j20)
                    
                    
                    
                elif datadr == '21.01':
                    print('')
                    
                    
                    print('У тебя день рождения 21 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j21)
                    
                    
                    
                elif datadr == '22.01':
                    print('')
                    
                    
                    print('У тебя день рождения 22 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j22)
                    
                    
                    
                elif datadr == '23.01':
                    print('')
                    
                    
                    print('У тебя день рождения 23 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j23)
                    
                    
                    
                elif datadr == '24.01':
                    print('')
                    
                    
                    print('У тебя день рождения 24 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j24)
                    
                    
                    
                elif datadr == '25.01':
                    print('')
                    
                    print('У тебя день рождения 25 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j25)
                    
                    
                    
                elif datadr == '26.01':
                    print('')
                    
                    print('У тебя день рождения 26 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j26)
                    
                    
                    
                elif datadr == '27.01':
                    print('')
                    
                    print('У тебя день рождения 27 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j27)
                    
                    
                    
                elif datadr == '28.01':
                    print('')
                    
                    print('У тебя день рождения 28 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j28)
                    
                    
                    
                elif datadr == '29.01':
                    print('')
                    
                    print('У тебя день рождения 29 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j29)
                    
                    
                    
                elif datadr == '30.01':
                    print('')
                    
                    print('У тебя день рождения 30 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j30)
                    
                    
                    
                elif datadr == '31.01':
                    print('')
                    
                    print('У тебя день рождения 31 января. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,j31)
                    
                    
                    
                
                    
                    
                
                
                #ФЕВРАЛЬ
                
                
                
                elif datadr == '01.02':
                    print('')
                    
                    print('У тебя день рождения 1 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f1)
                    
                    
                    
                    
                elif datadr == '02.02':
                    print('')
                    
                    print('У тебя день рождения 2 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f2)
                    
                    
                    
                    
                elif datadr == '03.02':
                    print('')
                    
                    print('У тебя день рождения 3 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f3)    
                    
                elif datadr == '04.02':
                    print('')
                    
                    print('У тебя день рождения 4 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f4)
                    
                    
                    
                elif datadr == '05.02':
                    print('')
                    
                    print('У тебя день рождения 5 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f5)
                    
                    
                    
                elif datadr == '06.02':
                    print('')
                    
                    print('У тебя день рождения 6 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f6)
                    
                    
                    
                elif datadr == '07.02':
                    print('')
                    
                    print('У тебя день рождения 7 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f7)
                    
                    
                    
                elif datadr == '08.02':
                    print('')
                    
                    print('У тебя день рождения 8 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f8)
                    
                    
                    
                elif datadr == '09.02':
                    print('')
                    
                    print('У тебя день рождения 9 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f9)
                    
                    
                    
                elif datadr == '10.02':
                    print('')
                    
                    print('У тебя день рождения 10 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f10)
                    
                    
                    
                elif datadr == '11.02':
                    print('')
                    
                    print('У тебя день рождения 11 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f11)
                    
                    
                    
                elif datadr == '12.02':
                    print('')
                    
                    print('У тебя день рождения 12 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f12)
                    
                    
                    
                elif datadr == '13.02':
                    print('')
                    
                    print('У тебя день рождения 13 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f13)
                    
                    
                    
                elif datadr == '14.02':
                    print('')
                    
                    print('У тебя день рождения 14 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f14)
                    
                    
                    
                
                
                    
                    
                elif datadr == '15.02':
                    print('')
                    
                    print('У тебя день рождения 15 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f15)
                    
                    
                    
                elif datadr == '16.02':
                    print('')
                    
                    print('У тебя день рождения 16 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f16)
                    
                    
                    
                elif datadr == '17.02':
                    print('')
                    
                    print('У тебя день рождения 17 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f17)
                    
                    
                    
                elif datadr == '18.02':
                    print('')
                    
                    print('У тебя день рождения 18 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f18)
                    
                    
                    
                elif datadr == '19.02':
                    print('')
                    
                    print('У тебя день рождения 19 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f19)
                    
                    
                    
                elif datadr == '20.02':
                    print('')
                    
                    print('У тебя день рождения 20 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f20)
                    
                    
                    
                elif datadr == '21.02':
                    print('')
                    
                    print('У тебя день рождения 21 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f21)
                    
                    
                    
                elif datadr == '22.02':
                    print('')
                    
                    print('У тебя день рождения 22 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f22)
                    
                    
                    
                elif datadr == '23.02':
                    print('')
                    
                    print('У тебя день рождения 23 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f23)
                    
                    
                    
                elif datadr == '24.02':
                    print('')
                    
                    print('У тебя день рождения 24 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f24)
                    
                    
                    
                elif datadr == '25.02':
                    print('')
                    
                    print('У тебя день рождения 25 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f25)
                    
                    
                    
                elif datadr == '26.02':
                    print('')
                    
                    print('У тебя день рождения 26 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f26)
                    
                    
                    
                elif datadr == '27.02':
                    print('')
                    
                    print('У тебя день рождения 27 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f27)
                    
                    
                    
                elif datadr == '28.02':
                    print('')
                    
                    print('У тебя день рождения 28 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f28)
                    
                    
                    
                elif datadr == '29.02':
                    print('')
                    
                    print('У тебя день рождения 29 февраля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,f29)
                    
                    
                    
                
                
                
                #МАРТ
                
                
                
                elif datadr == '01.03':
                    print('')
                    
                    print('У тебя день рождения 1 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m1)
                    
                    
                    
                    
                elif datadr == '02.03':
                    print('')
                    
                    print('У тебя день рождения 2 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m2)
                    
                    
                    
                    
                elif datadr == '03.03':
                    print('')
                    
                    print('У тебя день рождения 3 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m3)    
                    
                elif datadr == '04.03':
                    print('')
                    
                    print('У тебя день рождения 4 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m4)
                    
                    
                    
                elif datadr == '05.03':
                    print('')
                    
                    print('У тебя день рождения 5 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m5)
                
                    
                    
                    
                elif datadr == '06.03':
                    print('')
                    
                    print('У тебя день рождения 6 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m6)
                    
                    
                    
                elif datadr == '07.03':
                    print('')
                    
                    print('У тебя день рождения 7 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m7)
                    
                    
                    
                elif datadr == '08.03':
                    print('')
                    
                    print('У тебя день рождения 8 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m8)
                    
                    
                    
                elif datadr == '09.03':
                    print('')
                    
                    print('У тебя день рождения 9 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m9)
                    
                    
                    
                elif datadr == '10.03':
                    print('')
                    
                    print('У тебя день рождения 10 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m10)
                    
                    
                    
                elif datadr == '11.03':
                    print('')
                    
                    print('У тебя день рождения 11 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m11)
                    
                    
                    
                elif datadr == '12.03':
                    print('')
                    
                    print('У тебя день рождения 12 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m12)
                    
                    
                    
                elif datadr == '13.03':
                    print('')
                    
                    print('У тебя день рождения 13 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m13)
                    
                    
                    
                elif datadr == '14.03':
                    print('')
                    
                    print('У тебя день рождения 14 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m14)
                    
                    
                    
                elif datadr == '15.03':
                    print('')
                    
                    print('У тебя день рождения 15 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m15)
                    
                    
                    
                elif datadr == '16.03':
                    print('')
                    
                    print('У тебя день рождения 16 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m16)
                    
                    
                    
                elif datadr == '17.03':
                    print('')
                    
                    print('У тебя день рождения 17 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m17)
                    
                    
                    
                elif datadr == '18.03':
                    print('')
                    
                    print('У тебя день рождения 18 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m18)
                    
                    
                    
                elif datadr == '19.03':
                    print('')
                    
                    print('У тебя день рождения 19 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m19)
                    
                    
                    
                elif datadr == '20.03':
                    print('')
                    
                    print('У тебя день рождения 20 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m20)
                    
                    
                    
                elif datadr == '21.03':
                    print('')
                    
                    print('У тебя день рождения 21 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m21)
                    
                    
                    
                elif datadr == '22.03':
                    print('')
                    
                    print('У тебя день рождения 22 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m22)
                    
                    
                    
                elif datadr == '23.03':
                    print('')
                    
                    print('У тебя день рождения 23 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m23)
                    
                    
                    
                elif datadr == '24.03':
                    print('')
                    
                    print('У тебя день рождения 24 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m24)
                    
                    
                    
                elif datadr == '25.03':
                    print('')
                    
                    print('У тебя день рождения 25 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m25)
                    
                    
                    
                elif datadr == '26.03':
                    print('')
                    
                    print('У тебя день рождения 26 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m26)
                    
                    
                    
                elif datadr == '27.03':
                    print('')
                    
                    print('У тебя день рождения 27 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m27)
                    
                    
                    
                elif datadr == '28.03':
                    print('')
                    
                    print('У тебя день рождения 28 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m28)
                    
                    
                    
                elif datadr == '29.03':
                    print('')
                    
                    print('У тебя день рождения 29 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m29)
                    
                
                
                elif datadr == '30.03':
                    print('')
                    
                    print('У тебя день рождения 30 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m30)
                    
                    
                    
                elif datadr == '31.03':
                    print('')
                    
                    print('У тебя день рождения 31 марта. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,m31)
                
                    
                
                
                
                #АПРЕЛЬ
                
                
                
                
                
                elif datadr == '01.04':
                    print('')
                    print('У тебя день рождения 1 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a1)
                
                elif datadr == '02.04':
                    print('')
                    print('У тебя день рождения 2 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a2)
                
                elif datadr == '03.04':
                    print('')
                    print('У тебя день рождения 3 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a3)
                
                elif datadr == '04.04':
                    print('')
                    print('У тебя день рождения 4 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a4)
                
                
                
                elif datadr == '05.04':
                    print('')
                    print('У тебя день рождения 5 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a5)
                
                elif datadr == '06.04':
                    print('')
                    print('У тебя день рождения 6 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a6)
                
                elif datadr == '07.04':
                    print('')
                    print('У тебя день рождения 7 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a7)
                
                elif datadr == '08.04':
                    print('')
                    print('У тебя день рождения 8 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a8)
                
                
                
                    
                    
                elif datadr == '09.04':
                    print('')
                    print('У тебя день рождения 9 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a9)
                
                elif datadr == '10.04':
                    print('')
                    print('У тебя день рождения 10 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a10)
                
                elif datadr == '11.04':
                    print('')
                    print('У тебя день рождения 11 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a11)
                
                elif datadr == '12.04':
                    print('')
                    print('У тебя день рождения 12 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a12)
                
                elif datadr == '13.04':
                    print('')
                    print('У тебя день рождения 13 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a13)
                
                elif datadr == '14.04':
                    print('')
                    print('У тебя день рождения 14 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a14)
                
                elif datadr == '15.04':
                    print('')
                    print('У тебя день рождения 15 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a15)
                
                elif datadr == '16.04':
                    print('')
                    print('У тебя день рождения 16 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a16)
                
                elif datadr == '17.04':
                    print('')
                    print('У тебя день рождения 17 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a17)
                
                elif datadr == '18.04':
                    print('')
                    print('У тебя день рождения 18 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a18)
                
                    
                    
                elif datadr == '19.04':
                    print('')
                    print('У тебя день рождения 19 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a19)
                
                elif datadr == '20.04':
                    print('')
                    print('У тебя день рождения 20 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a20)
                
                elif datadr == '21.04':
                    print('')
                    print('У тебя день рождения 21 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a21)
                
                elif datadr == '22.04':
                    print('')
                    print('У тебя день рождения 22 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a22)
                
                elif datadr == '23.04':
                    print('')
                    print('У тебя день рождения 23 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a23)
                
                elif datadr == '24.04':
                    print('')
                    print('У тебя день рождения 24 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a24)
                
                elif datadr == '25.04':
                    print('')
                    print('У тебя день рождения 25 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a25)
                
                elif datadr == '26.04':
                    print('')
                    print('У тебя день рождения 26 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a26)
                
                elif datadr == '27.04':
                    print('')
                    print('У тебя день рождения 27 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a27)
                
                elif datadr == '28.04':
                    print('')
                    print('У тебя день рождения 28 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a28)
                
                elif datadr == '29.04':
                    print('')
                    print('У тебя день рождения 29 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a29)
                
                elif datadr == '30.04':
                    print('')
                    print('У тебя день рождения 30 апреля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,a30)
                
    
    
                
                
                

                #МАЙ
                
                
                
                elif datadr == '01.05':
                    print('')
                    print('У тебя день рождения 1 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj1)
                
                elif datadr == '02.05':
                    print('')
                    print('У тебя день рождения 2 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj2)
                
                elif datadr == '03.05':
                    print('')
                    print('У тебя день рождения 3 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj3)
                
                elif datadr == '04.05':
                    print('')
                    print('У тебя день рождения 4 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj4)
                    
                    
                    
                elif datadr == '05.05':
                    print('')
                    print('У тебя день рождения 5 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj5)
                
                elif datadr == '06.05':
                    print('')
                    print('У тебя день рождения 6 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj6)
                    
                    
                elif datadr == '07.05':
                    print('')
                    print('У тебя день рождения 7 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj7)
                
                elif datadr == '08.05':
                    print('')
                    print('У тебя день рождения 8 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj8)
                
                elif datadr == '09.05':
                    print('')
                    print('У тебя день рождения 9 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj9)
                
                elif datadr == '10.05':
                    print('')
                    print('У тебя день рождения 10 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj10)
                
                elif datadr == '11.05':
                    print('')
                    print('У тебя день рождения 11 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj11)
                
                elif datadr == '12.05':
                    print('')
                    print('У тебя день рождения 12 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj12)
                
                elif datadr == '13.05':
                    print('')
                    print('У тебя день рождения 13 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj13)
                
                elif datadr == '14.05':
                    print('')
                    print('У тебя день рождения 14 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj14)
                
                elif datadr == '15.05':
                    print('')
                    print('У тебя день рождения 15 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj15)
                
                elif datadr == '16.05':
                    print('')
                    print('У тебя день рождения 16 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj16)
                
                elif datadr == '17.05':
                    print('')
                    print('У тебя день рождения 17 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj17)
                
                elif datadr == '18.05':
                    print('')
                    print('У тебя день рождения 18 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj18)
                
                elif datadr == '19.05':
                    print('')
                    print('У тебя день рождения 19 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj19)
                
                elif datadr == '20.05':
                    print('')
                    print('У тебя день рождения 20 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj20)
                
                    
                    
                    
                elif datadr == '21.05':
                    print('')
                    print('У тебя день рождения 21 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj21)
                
                elif datadr == '22.05':
                    print('')
                    print('У тебя день рождения 22 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj22)
                
                elif datadr == '23.05':
                    print('')
                    print('У тебя день рождения 23 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj23)
                
                elif datadr == '24.05':
                    print('')
                    print('У тебя день рождения 24 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj24)
                
                elif datadr == '25.05':
                    print('')
                    print('У тебя день рождения 25 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj25)
                
                elif datadr == '26.05':
                    print('')
                    print('У тебя день рождения 26 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj26)
                
                elif datadr == '27.05':
                    print('')
                    print('У тебя день рождения 27 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj27)
                
                elif datadr == '28.05':
                    print('')
                    print('У тебя день рождения 28 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj28)
                
                elif datadr == '29.05':
                    print('')
                    print('У тебя день рождения 29 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj29)
                
                elif datadr == '30.05':
                    print('')
                    print('У тебя день рождения 30 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj30)
                
                elif datadr == '31.05':
                    print('')
                    print('У тебя день рождения 31 мая. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,mj31)
                
                    
                    
                    
                
                    
                    
                    
                    
                    
                
                
                
                #ИЮНЬ
                
                
                
                elif datadr == '01.06':
                    print('')
                    print('У тебя день рождения 1 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn1)
                
                elif datadr == '02.06':
                    print('')
                    print('У тебя день рождения 2 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn2)
                
                elif datadr == '03.06':
                    print('')
                    print('У тебя день рождения 3 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn3)
                
                elif datadr == '04.06':
                    print('')
                    print('У тебя день рождения 4 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn4)
                
                elif datadr == '05.06':
                    print('')
                    print('У тебя день рождения 5 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn5)
                
                elif datadr == '06.06':
                    print('')
                    print('У тебя день рождения 6 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn6)
                
                elif datadr == '07.06':
                    print('')
                    print('У тебя день рождения 7 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn7)
                
                elif datadr == '08.06':
                    print('')
                    print('У тебя день рождения 8 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn8)
                
                elif datadr == '09.06':
                    print('')
                    print('У тебя день рождения 9 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn9)
                
                elif datadr == '10.06':
                    print('')
                    print('У тебя день рождения 10 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn10)
                
                elif datadr == '11.06':
                    print('')
                    print('У тебя день рождения 11 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn11)
                
                elif datadr == '12.06':
                    print('')
                    print('У тебя день рождения 12 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn12)
                
                elif datadr == '13.06':
                    print('')
                    print('У тебя день рождения 13 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn13)
                
                elif datadr == '14.06':
                    print('')
                    print('У тебя день рождения 14 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn14)
                
                elif datadr == '15.06':
                    print('')
                    print('У тебя день рождения 15 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn15)
                
                    
                    
                    
                elif datadr == '16.06':
                    print('')
                    print('У тебя день рождения 16 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn16)
                
                elif datadr == '17.06':
                    print('')
                    print('У тебя день рождения 17 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn17)
                
                elif datadr == '18.06':
                    print('')
                    print('У тебя день рождения 18 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn18)
                
                elif datadr == '19.06':
                    print('')
                    print('У тебя день рождения 19 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn19)
                
                elif datadr == '20.06':
                    print('')
                    print('У тебя день рождения 20 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn20)
                
                elif datadr == '21.06':
                    print('')
                    print('У тебя день рождения 21 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn21)
                
                elif datadr == '22.06':
                    print('')
                    print('У тебя день рождения 22 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn22)
                
                elif datadr == '23.06':
                    print('')
                    print('У тебя день рождения 23 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn23)
                
                elif datadr == '24.06':
                    print('')
                    print('У тебя день рождения 24 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn24)
                
                elif datadr == '25.06':
                    print('')
                    print('У тебя день рождения 25 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn25)
                
                elif datadr == '26.06':
                    print('')
                    print('У тебя день рождения 26 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn26)
                
                elif datadr == '27.06':
                    print('')
                    print('У тебя день рождения 27 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn27)
                
                elif datadr == '28.06':
                    print('')
                    print('У тебя день рождения 28 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn28)
                
                elif datadr == '29.06':
                    print('')
                    print('У тебя день рождения 29 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn29)
                
                elif datadr == '30.06':
                    print('')
                    print('У тебя день рождения 30 июня. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jn30)
                
                    
                    
                    
                    
                    
                    
                
                
                
                
                
                
                
                
                
                
                
                
                #ИЮЛЬ
                
                
                
                
                
                
                elif datadr == '01.07':
                    print('')
                    print('У тебя день рождения 1 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl1)
                
                elif datadr == '02.07':
                    print('')
                    print('У тебя день рождения 2 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl2)
                
                elif datadr == '03.07':
                    print('')
                    print('У тебя день рождения 3 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl3)
                
                elif datadr == '04.07':
                    print('')
                    print('У тебя день рождения 4 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl4)
                
                elif datadr == '05.07':
                    print('')
                    print('У тебя день рождения 5 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl5)
                
                elif datadr == '06.07':
                    print('')
                    print('У тебя день рождения 6 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl6)
                
                elif datadr == '07.07':
                    print('')
                    print('У тебя день рождения 7 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl7)
                
                elif datadr == '08.07':
                    print('')
                    print('У тебя день рождения 8 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl8)
                
                elif datadr == '09.07':
                    print('')
                    print('У тебя день рождения 9 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl9)
                
                elif datadr == '10.07':
                    print('')
                    print('У тебя день рождения 10 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl10)
                
                elif datadr == '11.07':
                    print('')
                    print('У тебя день рождения 11 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl11)
                
                elif datadr == '12.07':
                    print('')
                    print('У тебя день рождения 12 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl12)
                
                elif datadr == '13.07':
                    print('')
                    print('У тебя день рождения 13 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl13)
                
                elif datadr == '14.07':
                    print('')
                    print('У тебя день рождения 14 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl14)
                
                elif datadr == '15.07':
                    print('')
                    print('У тебя день рождения 15 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl15)
                
                    
                    
                    
                elif datadr == '16.07':
                    print('')
                    print('У тебя день рождения 16 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl16)
                
                elif datadr == '17.07':
                    print('')
                    print('У тебя день рождения 17 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl17)
                
                elif datadr == '18.07':
                    print('')
                    print('У тебя день рождения 18 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl18)
                
                elif datadr == '19.07':
                    print('')
                    print('У тебя день рождения 19 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl19)
                
                elif datadr == '20.07':
                    print('')
                    print('У тебя день рождения 20 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl20)
                
                elif datadr == '21.07':
                    print('')
                    print('У тебя день рождения 21 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl21)
                
                elif datadr == '22.07':
                    print('')
                    print('У тебя день рождения 22 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl22)
                
                elif datadr == '23.07':
                    print('')
                    print('У тебя день рождения 23 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl23)
                
                elif datadr == '24.07':
                    print('')
                    print('У тебя день рождения 24 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl24)
                
                elif datadr == '25.07':
                    print('')
                    print('У тебя день рождения 25 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl25)
                
                elif datadr == '26.07':
                    print('')
                    print('У тебя день рождения 26 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl26)
                
                elif datadr == '27.07':
                    print('')
                    print('У тебя день рождения 27 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl27)
                
                elif datadr == '28.07':
                    print('')
                    print('У тебя день рождения 28 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl28)
                
                elif datadr == '29.07':
                    print('')
                    print('У тебя день рождения 29 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl29)
                
                elif datadr == '30.07':
                    print('')
                    print('У тебя день рождения 30 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl30)
                
                elif datadr == '31.07':
                    print('')
                    print('У тебя день рождения 31 июля. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,jl31)
                
                    
                    
                    
                
                    
                    
                
                
                #АВГУСТ
                
                
                
                elif datadr == '01.08':
                    print('')
                    print('У тебя день рождения 1 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag1)
                    
                    
                    
                elif datadr == '02.08':
                    print('')
                    print('У тебя день рождения 2 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag2)
                    
                    
                    
                elif datadr == '03.08':
                    print('')
                    print('У тебя день рождения 3 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag3)
                    
                    
                    
                elif datadr == '04.08':
                    print('')
                    print('У тебя день рождения 4 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag4)
                    
                    
                    
                elif datadr == '05.08':
                    print('')
                    print('У тебя день рождения 5 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag5)
                    
                    
                    
                elif datadr == '06.08':
                    print('')
                    print('У тебя день рождения 6 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag6)
                    
                    
                    
                elif datadr == '07.08':
                    print('')
                    print('У тебя день рождения 7 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag7)
                    
                    
                    
                elif datadr == '08.08':
                    print('')
                    print('У тебя день рождения 8 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag8)
                    
                    
                    
                elif datadr == '09.08':
                    print('')
                    print('У тебя день рождения 9 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag9)
                    
                    
                    
                elif datadr == '10.08':
                    print('')
                    print('У тебя день рождения 10 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag10)
                    
                    
                    
                elif datadr == '11.08':
                    print('')
                    print('У тебя день рождения 11 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag11)
                    
                    
                    
                elif datadr == '12.08':
                    print('')
                    print('У тебя день рождения 12 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag12)
                    
                    
                    
                elif datadr == '13.08':
                    print('')
                    print('У тебя день рождения 13 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag13)
                    
                    
                    
                elif datadr == '14.08':
                    print('')
                    print('У тебя день рождения 14 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag14)
                    
                    
                    
                elif datadr == '15.08':
                    print('')
                    print('У тебя день рождения 15 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag15)
                    
                    
                elif datadr == '16.08':
                    print('')
                    print('У тебя день рождения 16 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag16)
                    
                    
                    
                elif datadr == '17.08':
                    print('')
                    print('У тебя день рождения 17 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag17)
                    
                    
                    
                elif datadr == '18.08':
                    print('')
                    print('У тебя день рождения 18 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag18)
                    
                    
                    
                elif datadr == '19.08':
                    print('')
                    print('У тебя день рождения 19 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag19)
                    
                    
                    
                elif datadr == '20.08':
                    print('')
                    print('У тебя день рождения 20 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag20)
                    
                    
                    
                elif datadr == '21.08':
                    print('')
                    print('У тебя день рождения 21 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag21)
                    
                    
                    
                elif datadr == '22.08':
                    print('')
                    print('У тебя день рождения 22 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag22)
                    
                    
                    
                elif datadr == '23.08':
                    print('')
                    print('У тебя день рождения 23 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag23)
                    
                    
                    
                elif datadr == '24.08':
                    print('')
                    print('У тебя день рождения 24 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag24)
                    
                    
                    
                elif datadr == '25.08':
                    print('')
                    print('У тебя день рождения 25 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag25)
                    
                    
                    
                elif datadr == '26.08':
                    print('')
                    print('У тебя день рождения 26 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag26)
                    
                    
                    
                elif datadr == '27.08':
                    print('')
                    print('У тебя день рождения 27 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag27)
                    
                    
                    
                elif datadr == '28.08':
                    print('')
                    print('У тебя день рождения 28 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag28)
                    
                    
                    
                elif datadr == '29.08':
                    print('')
                    print('У тебя день рождения 29 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag29)
                    
                    
                    
                elif datadr == '30.08':
                    print('')
                    print('У тебя день рождения 30 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag30)
                    
                    
                    
                elif datadr == '31.08':
                    print('')
                    print('У тебя день рождения 31 августа.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,ag31)
                
                
                
                #СЕНТЯБРЬ
                
                
                
                elif datadr == '01.09':
                    print('')
                    print('У тебя день рождения 1 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s1)
                
                elif datadr == '02.09':
                    print('')
                    print('У тебя день рождения 2 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s2)
                
                elif datadr == '03.09':
                    print('')
                    print('У тебя день рождения 3 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s3)
                
                elif datadr == '04.09':
                    print('')
                    print('У тебя день рождения 4 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s4)
                
                elif datadr == '05.09':
                    print('')
                    print('У тебя день рождения 5 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s5)
                
                elif datadr == '06.09':
                    print('')
                    print('У тебя день рождения 6 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s6)
                
                elif datadr == '07.09':
                    print('')
                    print('У тебя день рождения 7 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s7)
                
                elif datadr == '08.09':
                    print('')
                    print('У тебя день рождения 8 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s8)
                
                elif datadr == '09.09':
                    print('')
                    print('У тебя день рождения 9 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s9)
                
                elif datadr == '10.09':
                    print('')
                    print('У тебя день рождения 10 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s10)
                
                elif datadr == '11.09':
                    print('')
                    print('У тебя день рождения 11 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s11)
                
                elif datadr == '12.09':
                    print('')
                    print('У тебя день рождения 12 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s12)
                
                elif datadr == '13.09':
                    print('')
                    print('У тебя день рождения 13 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s13)
                
                elif datadr == '14.09':
                    print('')
                    print('У тебя день рождения 14 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s14)
                
                elif datadr == '15.09':
                    print('')
                    print('У тебя день рождения 15 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s15)
                
                    
                    
                elif datadr == '16.09':
                    print('')
                    print('У тебя день рождения 16 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s16)
                
                elif datadr == '17.09':
                    print('')
                    print('У тебя день рождения 17 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s17)
                
                elif datadr == '18.09':
                    print('')
                    print('У тебя день рождения 18 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s18)
                
                elif datadr == '19.09':
                    print('')
                    print('У тебя день рождения 19 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s19)
                
                elif datadr == '20.09':
                    print('')
                    print('У тебя день рождения 20 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s20)
                
                elif datadr == '21.09':
                    print('')
                    print('У тебя день рождения 21 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s21)
                
                elif datadr == '22.09':
                    print('')
                    print('У тебя день рождения 22 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s22)
                
                elif datadr == '23.09':
                    print('')
                    print('У тебя день рождения 23 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s23)
                
                elif datadr == '24.09':
                    print('')
                    print('У тебя день рождения 24 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s24)
                
                elif datadr == '25.09':
                    print('')
                    print('У тебя день рождения 25 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s25)
                
                elif datadr == '26.09':
                    print('')
                    print('У тебя день рождения 26 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s26)
                
                elif datadr == '27.09':
                    print('')
                    print('У тебя день рождения 27 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s27)
                
                elif datadr == '28.09':
                    print('')
                    print('У тебя день рождения 28 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s28)
                
                elif datadr == '29.09':
                    print('')
                    print('У тебя день рождения 29 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s29)
                
                elif datadr == '30.09':
                    print('')
                    print('У тебя день рождения 30 сентября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,s30)
                
                    
                    
                
                    
                    
                
                
                
                #ОКТЯБРЬ
                
                
                
                elif datadr == '01.10':
                    print('')
                    print('У тебя день рождения 1 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o1)
                
                elif datadr == '02.10':
                    print('')
                    print('У тебя день рождения 2 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o2)
                
                elif datadr == '03.10':
                    print('')
                    print('У тебя день рождения 3 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o3)
                
                elif datadr == '04.10':
                    print('')
                    print('У тебя день рождения 4 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o4)
                
                elif datadr == '05.10':
                    print('')
                    print('У тебя день рождения 5 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o5)
                
                elif datadr == '06.10':
                    print('')
                    print('У тебя день рождения 6 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o6)
                
                elif datadr == '07.10':
                    print('')
                    print('У тебя день рождения 7 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o7)
                
                elif datadr == '08.10':
                    print('')
                    print('У тебя день рождения 8 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o8)
                 
                elif datadr == '09.10':
                    print('')
                    print('У тебя день рождения 9 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o9)
                
                elif datadr == '10.10':
                    print('')
                    print('У тебя день рождения 10 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o10)
                
                elif datadr == '11.10':
                    print('')
                    print('У тебя день рождения 11 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o11)
                
                elif datadr == '12.10':
                    print('')
                    print('У тебя день рождения 12 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o12)
                
                elif datadr == '13.10':
                    print('')
                    print('У тебя день рождения 13 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o13)
                
                elif datadr == '14.10':
                    print('')
                    print('У тебя день рождения 14 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o14)
                
                elif datadr == '15.10':
                    print('')
                    print('У тебя день рождения 15 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o15)
                
                    
                    
                elif datadr == '16.10':
                    print('')
                    print('У тебя день рождения 16 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o16)
                
                elif datadr == '17.10':
                    print('')
                    print('У тебя день рождения 17 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o17)
                
                elif datadr == '18.10':
                    print('')
                    print('У тебя день рождения 18 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o18)
                
                elif datadr == '19.10':
                    print('')
                    print('У тебя день рождения 19 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o19)
                
                elif datadr == '20.10':
                    print('')
                    print('У тебя день рождения 20 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o20)
                
                elif datadr == '21.10':
                    print('')
                    print('У тебя день рождения 21 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o21)
                
                elif datadr == '22.10':
                    print('')
                    print('У тебя день рождения 22 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o22)
                
                elif datadr == '23.10':
                    print('')
                    print('У тебя день рождения 23 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o23)
                
                elif datadr == '24.10':
                    print('')
                    print('У тебя день рождения 24 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o24)
                
                elif datadr == '25.10':
                    print('')
                    print('У тебя день рождения 25 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o25)
                
                elif datadr == '26.10':
                    print('')
                    print('У тебя день рождения 26 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o26)
                
                elif datadr == '27.10':
                    print('')
                    print('У тебя день рождения 27 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o27)
                
                elif datadr == '28.10':
                    print('')
                    print('У тебя день рождения 28 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o28)
                
                elif datadr == '29.10':
                    print('')
                    print('У тебя день рождения 29 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o29)
                
                elif datadr == '30.10':
                    print('')
                    print('У тебя день рождения 30 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o30)
                
                elif datadr == '31.10':
                    print('')
                    print('У тебя день рождения 31 октября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,o31)
                
                    
                    
                    
                    
                
                
                
                #НОЯБРЬ
                
                
                
                elif datadr == '01.11':
                    print('')
                    print('У тебя день рождения 1 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n1)
                
                elif datadr == '02.11':
                    print('')
                    print('У тебя день рождения 2 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n2)
                
                elif datadr == '03.11':
                    print('')
                    print('У тебя день рождения 3 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n3)
                
                elif datadr == '04.11':
                    print('')
                    print('У тебя день рождения 4 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n4)
                
                elif datadr == '05.11':
                    print('')
                    print('У тебя день рождения 5 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n5)
                
                elif datadr == '06.11':
                    print('')
                    print('У тебя день рождения 6 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n6)
                
                elif datadr == '07.11':
                    print('')
                    print('У тебя день рождения 7 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n7)
                
                elif datadr == '08.11':
                    print('')
                    print('У тебя день рождения 8 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n8)
                
                elif datadr == '09.11':
                    print('')
                    print('У тебя день рождения 9 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n9)
                
                elif datadr == '10.11':
                    print('')
                    print('У тебя день рождения 10 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n10)
                
                elif datadr == '11.11':
                    print('')
                    print('У тебя день рождения 11 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n11)
                
                elif datadr == '12.11':
                    print('')
                    print('У тебя день рождения 12 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n12)
                
                elif datadr == '13.11':
                    print('')
                    print('У тебя день рождения 13 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n13)
                
                elif datadr == '14.11':
                    print('')
                    print('У тебя день рождения 14 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n14)
                
                elif datadr == '15.11':
                    print('')
                    print('У тебя день рождения 15 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n15)
                
                    
                    
                elif datadr == '16.11':
                    print('')
                    print('У тебя день рождения 16 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n16)
                
                elif datadr == '17.11':
                    print('')
                    print('У тебя день рождения 17 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n17)
                
                elif datadr == '18.11':
                    print('')
                    print('У тебя день рождения 18 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n18)
                
                elif datadr == '19.11':
                    print('')
                    print('У тебя день рождения 19 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n19)
                
                elif datadr == '20.11':
                    print('')
                    print('У тебя день рождения 20 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n20)
                
                elif datadr == '21.11':
                    print('')
                    print('У тебя день рождения 21 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n21)
                
                elif datadr == '22.11':
                    print('')
                    print('У тебя день рождения 22 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n22)
                
                elif datadr == '23.11':
                    print('')
                    print('У тебя день рождения 23 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n23)
                
                elif datadr == '24.11':
                    print('')
                    print('У тебя день рождения 24 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n24)
                
                elif datadr == '25.11':
                    print('')
                    print('У тебя день рождения 25 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n25)
                
                elif datadr == '26.11':
                    print('')
                    print('У тебя день рождения 26 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n26)
                
                elif datadr == '27.11':
                    print('')
                    print('У тебя день рождения 27 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n27)
                
                elif datadr == '28.11':
                    print('')
                    print('У тебя день рождения 28 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n28)
                
                elif datadr == '29.11':
                    print('')
                    print('У тебя день рождения 29 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n29)
                
                elif datadr == '30.11':
                    print('')
                    print('У тебя день рождения 30 ноября.')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,n30)
                
                    
                    
                    
                
                    
                    
                    
                
                    
                    
                    
                    
                    
                
                
                
                #ДЕКАБРЬ
                
                
                
                elif datadr == '01.12':
                    print('')
                    
                    print('У тебя день рождения 1 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc1)
                    
                    
                    
                    
                elif datadr == '02.12':
                    print('')
                    
                    
                    print('У тебя день рождения 2 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc2)
                    
                    
                    
                    
                elif datadr == '03.12':
                    print('')
                    
                    
                    print('У тебя день рождения 3 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc3)    
                    
                elif datadr == '04.12':
                    print('')
                   
                    
                    print('У тебя день рождения 4 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc4)
                    
                    
                    
                elif datadr == '05.12':
                    print('')
                    
                    
                    print('У тебя день рождения 5 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc5)
                    
                    
                    
                elif datadr == '06.12':
                    print('')
                    
                    
                    print('У тебя день рождения 6 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc6)
                    
                    
                    
                elif datadr == '07.12':
                    print('')
                    
                    
                    print('У тебя день рождения 7 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc7)
                    
                    
                    
                elif datadr == '08.12':
                    print('')
                    
                    
                    print('У тебя день рождения 8 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc8)
                    
                    
                    
                elif datadr == '09.12':
                    print('')
                    
                    print('У тебя день рождения 9 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc9)
                    
                    
                    
                elif datadr == '10.12':
                    print('')
                    
                    
                    print('У тебя день рождения 10 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc10)
                    
                    
                    
                elif datadr == '11.12':
                    print('')
                    
                    
                    print('У тебя день рождения 11 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc11)
                    
                    
                    
                elif datadr == '12.12':
                    print('')
                    
                    
                    print('У тебя день рождения 12 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc12)
                    
                    
                    
                elif datadr == '13.12':
                    print('')
                    
                    
                    print('У тебя день рождения 13 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc13)
                    
                    
                    
                elif datadr == '14.12':
                    print('')
                    
                    
                    print('У тебя день рождения 14 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc14)
                    
                    
                    
                elif datadr == '15.12':
                    print('')
                    
                    
                    print('У тебя день рождения 15 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc15)
                    
                    
                    
                elif datadr == '16.12':
                    print('')
                    
                    
                    print('У тебя день рождения 16 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc16)
                    
                    
                    
                elif datadr == '17.12':
                    print('')
                    
                    
                    print('У тебя день рождения 17 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc17)
                    
                    
                    
                elif datadr == '18.12':
                    print('')
                    
                    
                    print('У тебя день рождения 18 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc18)
                    
                    
                    
                elif datadr == '19.12':
                    print('')
                    
                    
                    print('У тебя день рождения 19 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc19)
                    
                    
                    
                elif datadr == '20.12':
                    print('')
                    
                    
                    print('У тебя день рождения 20 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc20)
                    
                    
                    
                elif datadr == '21.12':
                    print('')
                    
                    
                    print('У тебя день рождения 21 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc21)
                    
                    
                    
                elif datadr == '22.12':
                    print('')
                    
                    
                    print('У тебя день рождения 22 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc22)
                    
                    
                    
                elif datadr == '23.12':
                    print('')
                    
                    
                    print('У тебя день рождения 23 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc23)
                    
                    
                    
                elif datadr == '24.12':
                    print('')
                   
                    
                    print('У тебя день рождения 24 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc24)
                    
                    
                    
                elif datadr == '25.12':
                    print('')
                    
                    
                    print('У тебя день рождения 25 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc25)
                    
                    
                    
                elif datadr == '26.12':
                    print('')
                    
                    
                    print('У тебя день рождения 26 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc26)
                    
                    
                    
                elif datadr == '27.12':
                    print('')
                    
                    
                    print('У тебя день рождения 27 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc27)
                    
                    
                    
                elif datadr == '28.12':
                    print('')
                    
                    
                    print('У тебя день рождения 28 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc28)
                    
                    
                    
                elif datadr == '29.12':
                    print('')
                     
                    
                    print('У тебя день рождения 29 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc29)
                    
                
                
                elif datadr == '30.12':
                    print('')
                    
                    
                    print('У тебя день рождения 30 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc30)    
                    
                
                
                
                elif datadr == '31.12':
                    print('')
                    
                    print('У тебя день рождения 31 декабря. ')
                    print('Вот у какой знаменитости с тобой ДР в один день - ' ,dc31)    
                        

                                                                                                                                                                                                                                                    
            else:
                print('Других игр с датами пока что нет.')

                        

                                                                                                                                                                                                                                                    
        
        
        else:
            print()
            print('К сожалению других типов игр пока что нет(')
        
                    
            
                             
              
    elif command.lower() == "квиз" or command == '2':
        print('Вот список доступных квизов:')
        print("1. Книги")
        print('2. Фильмы')
        print("3. GTA 5")
        print('')
        
        nomerkviza = input("Введите номер квиза: ")
        
        if nomerkviza.lower() == 'gta 5' or nomerkviza == '3':
            pointsingtatest = 0
            print('')
            print('Привет! Если ты любишь играть в игру Gta 5 и Gta Online, этот квиз тебе понравится!')
           
            print('')
            print('Quiz - GTA 5')
            print('')
    
            gtavopros1 = input('Сколько главных героев в игре? (Напиши цифру) - ')
            if gtavopros1 == "3" or gtavopros1.lower() == "три":
                print("Правильный ответ!")
                pointsingtatest += 1
            else:
                print('Это неправильный ответ!')
    
            print('')
            if pointsingtatest == 1:
                print('У вас', pointsingtatest, 'пункт')
            else:
                print('У вас 0 пунктов')
    
            print('')
            print('В каком городе разворачиваются события игры GTA V? ')
            
            time.sleep(2)
            print('')
            print('Напиши номер варианта:')
            print('1. Лос-Сантос')
            print('2. Лос-Анджелес')
            print('3. Вайс Сити')
            print('4. Либерти Сити')
            print()
            
            time.sleep(1)
            gtavopros2 = input('Ваш выбор: ')
            
            
            if gtavopros2.lower() == "лос-сантос" or gtavopros2 == "1" or gtavopros2.lower() == "лос сантос":
                print("Правильный ответ!")
                pointsingtatest += 1
            else:
                print('Это неправильный ответ!')
    
            print('')
            if pointsingtatest == 0:
                print('У вас', pointsingtatest, 'пунктов')
            elif pointsingtatest == 1:
                print('У вас', pointsingtatest, 'пункт')  
            elif pointsingtatest >= 2:
                print('У вас', pointsingtatest, 'пункта')    
    
            print('')
            gtavopros3 = input('В каком году происходят события игры? (Напиши число) - ')
            if gtavopros3 == "2013":
                print("Правильный ответ!")
                pointsingtatest += 1
            else:
                print('Это неправильный ответ!')
    
            print('')
            if pointsingtatest == 0:
                print('У вас', pointsingtatest, 'пунктов')
            elif pointsingtatest == 1:
                print('У вас', pointsingtatest, 'пункт')  
            elif pointsingtatest >= 2:
                print('У вас', pointsingtatest, 'пункта') 
    
            print('')
            
            gtavopros4 = input('Сколько вариантов концовки есть в игре? (Напиши цифру) - ')
            if gtavopros4 == "3" or gtavopros4.lower() == "три":
                print("Правильный ответ!")
                pointsingtatest += 1
            else:
                print('Это неправильный ответ!')
    
            print('')
            if pointsingtatest == 0:
                print('У вас', pointsingtatest, 'пунктов')
            elif pointsingtatest == 1:
                print('У вас', pointsingtatest, 'пункт')  
            elif pointsingtatest >= 2:
                print('У вас', pointsingtatest, 'пункта') 
    
            print('')
            gtavopros5 = input('Напиши дату, когда GTA 5 исполнилось 10 лет (пиши в формате DAY.MONTH.YEAR) - ')
            if gtavopros5 == "17.09.2023" :
                print("Правильный ответ!")
                pointsingtatest += 1
            else:
                print('Это неправильный ответ!')
    
            print('')
            if pointsingtatest == 1:
                print('У вас', pointsingtatest, 'пункт')
            elif pointsingtatest >= 2 and pointsingtatest <=4:
                print('У вас', pointsingtatest, 'пункта')
            elif pointsingtatest >= 5:
                print('У вас', pointsingtatest, 'пунктов')
            else:
                print('У вас 0 пунктов')
    
            print()
            print('Сейчас будет целых 3 вопроса подряд! Ответишь на все правильно и заберешь 3 пункта!')
            print()
            time.sleep(2)
            print('Вам надо будет написать первую букву имени персонажа о котором идет речь. (F/M/T) - буквы пиши на английском!')
            print()
            print('F - Франклин, M - Майкл, T - Тревор')
            print('')
            gtavopros6 = input('Как зовут персонажа который работает на Симона? (F/M/T) - ')
            gtavopros7 = input ('Как зовут персонажа который живет в пустыне Сэнди Шорс? (F/M/T) - ')
            gtavopros8 = input('Как зовут персонажа у которого есть двое детей? (F/M/T) - ')
            print()
    
            if gtavopros6.lower() == "f" and gtavopros7.lower() == "t" and gtavopros8.lower() == 'm':
                print("Правильные ответы!")
                pointsingtatest += 3
            else:
                print('Это неправильный ответ!')    
        
            print('')
            if pointsingtatest == 0:
                print('У вас', pointsingtatest, 'пунктов из 8!')
            elif pointsingtatest == 1:
                print('У вас', pointsingtatest, 'пункт из 8!')  
            elif pointsingtatest >= 2 and pointsingtatest <=4:
                print('У вас', pointsingtatest, 'пункта из 8!') 
            elif pointsingtatest >= 5:
                print('У вас', pointsingtatest, 'пунктов из 8!')   
    
    
            elif pointsingtatest == 8:
                print('Поздравляем! Вы ответили правильно на все вопросы. Вы настоящий эксперт по GTA 5!')
               
            if pointsingtatest >= 5:
                print('Вы отлично справились! Вы знаете GTA 5 хорошо.')
               
            elif pointsingtatest >= 3:
                print('У вас есть базовые знания об игре GTA 5, но есть еще место для улучшений.')
               
            else:
                print('Вам стоит побольше узнать об игре GTA 5. Но не переживайте, вы можете улучшить свои знания!')
            
        
        elif nomerkviza.lower() ==  'фильмы' or nomerkviza == '2':
            pointsinfilmquiz = 0
            print()
            print('КВИЗ - ФИЛЬМЫ')
            print('')
            time.sleep(1.5)
            print('')
            print('Я буду описывать тебе фильм, а ты должен правильно его угадать!')
            print('')
            time.sleep(1)
            print('Начинаем!')
            print()
            
            time.sleep(1)
        
            print('1. Как называется 4-ый фильм про мальчика, который выжил?')
            time.sleep(1)
            print()
            print('1. Гарри Поттер и принц Полукровка')
            print('2. Гарри Поттер и узник Азкабана')
            print('3. Гарри Поттер и кубок Огня')
            print()
            
            time.sleep(2)
            voprosprofilmi1 = input('Напишите номер варианта - ')
            print('')
            
            if voprosprofilmi1.lower() == 'гарри поттер и кубок огня' or voprosprofilmi1.lower() == 'кубок огня'  or voprosprofilmi1 == '3':
                print('Верно! Это фильм - Гарри Поттер и Кубок огня! Ты получаешь балл!')
                pointsinfilmquiz +=1
                
            else:
                print('Увы! Это неправильный ответ!')
                print('Правильный ответ - Гарри Поттер и Кубок огня. ')
                
            print('')
            print('Следующий вопрос:')
            print()
            
            time.sleep(1)
            
            print('2. Как называется новогодний фильм, где родители забывают сына дома и он остается один?')
            time.sleep(1)
            print()
            print('1. Один дома')
            print('2. Джуманджи')
            print('3. Привет семье')
            print()
            
            
            voprosprofilmi2 = input('Напишите номер варианта - ')
            print('')
            if voprosprofilmi2.lower() == 'один дома' or voprosprofilmi2 == '1':
                print('Верно! Это фильм - Один Дома! Ты получаешь балл!')
                pointsinfilmquiz +=1
                
            else:
                print('Увы! Это неправильный ответ!')
                print('Правильный ответ - Один Дома. ')
                
            print('')
            print('Следующий вопрос:')
            print()
            
            time.sleep(1)   
            
            print('3. Как назывался фильм, где группа подростков попала в компьютерную игру?')
            time.sleep(1)
            print()
            print('1. Город костей')
            print('2. Джуманджи')
            print('3. Локвуд и компания')
            print()
            
            
            voprosprofilmi3 = input('Напишите номер варианта - ')
            print('')
            if voprosprofilmi3.lower() == 'джуманджи' or voprosprofilmi3 == '2':
                print('Верно! Это фильм - Джуманджи! Ты получаешь балл!')
                pointsinfilmquiz +=1
                
            else:
                print('Увы! Это неправильный ответ!')
                print('Правильный ответ - Джуманджи. ')
                
            print('')
            print('Следующий вопрос:')
            print()
            
            time.sleep(1) 
            
            print('4. Как называется фильм, где мужчина устроился работать охранником в музей, и увидел что ночью все экспонаты оживают?')
            time.sleep(1)
            print()
            print('1. Билет в рай')
            print('2. Ночь в музее')
            print('3. Перси Джексон')
            print()
            
            voprosprofilmi4 = input('Напишите номер варианта - ')
            print('')
            if voprosprofilmi4 == 'ночь в музее' or voprosprofilmi4 == '2':
                print('Верно! Это фильм - Ночь в музее! Ты получаешь балл!')
                pointsinfilmquiz +=1
                
            else:
                print('Увы! Это неправильный ответ!')
                print('Правильный ответ - Ночь в музее. ')
                
            print('')
            print('Следующий вопрос:')
            print()
            
            time.sleep(1)
            
            print('5. Как называется мультфильм, в котором игрушки - живые?')
            time.sleep(1)
            print()
            print('1. Холодное сердце')
            print('2. Мадагаскар')
            print('3. История игрушек')
            print()
            
            voprosprofilmi5 = input('Напишите номер варианта - ')
            print('')
            if voprosprofilmi5.lower() == 'история игрушек' or voprosprofilmi5 == '3':
                print('Верно! Это мультфильм - История игрушек! Ты получаешь балл!')
                pointsinfilmquiz +=1
                
            else:
                print('Увы! Это неправильный ответ!')
                print('Правильный ответ - История игрушек ')
                
            print('')
            
            time.sleep(3)
            
            print('Это был последний вопрос!')
            
            time.sleep(2)
            
            print('Подсчитываем баллы...')
            print('')
                
            time.sleep(3)
            
            if pointsinfilmquiz == 5:
                print('Поздравяем! Вы получили 5 из 5 баллов! Похоже вы настоящий киноэксперт!')
                
            elif pointsinfilmquiz == 4:
                print('Вы набрали 4 балла из 5! Это очень хороший результат!')
                
            elif pointsinfilmquiz == 3:
                print('Вы набрали 3 балла из 5. Вы неплохо разбираетесь в кино!')
                
            elif pointsinfilmquiz == 2:
                print('Вы набрали 2 балла из 5. Надеюсь в следующий раз вам повезет!')    
                    
            elif pointsinfilmquiz == 1:                    
                print('Вы набрали 1 балл из 5. Видимо вы не очень хорошо знаете фильмы...')
                    
            elif pointsinfilmquiz == 0:
                print('К сожалению, вы на все вопросы ответили неправильно! Но ничего страшного, вы всегда можете перепройти этот тест! ')
            
            print('')
            
            
            
        elif nomerkviza.lower() == 'книги' or nomerkviza == '1':
            print()
            print('КВИЗ - КНИГИ')
            print('')
            print('')
            
            pointsinbookq = 0
            
            print('Я буду описывать тебе книгу, а ты должен правильно ее угадать!')
            print('')
            time.sleep(1)
            print('Начинаем!')
            
            time.sleep(1)
            
            print('1. Как называется классическая книга, где в конце главная героиня прыгнула под поезд?')
            time.sleep(1)
            print()
            print('1. Война и мир')
            print('2. Сестра Керри')
            print('3. Анна Каренина')
            print()
            
            
            
            bookvoprosik1 = input('Напишите номер варианта: ')
            print('')
            time.sleep(1)
            
            
            
            if bookvoprosik1 == 'анна каренина' or bookvoprosik1 == '3':
                print('Верно! Это книга - Анна Каренина от Льва Толстого! Ты получаешь балл!')
                pointsinbookq +=1
                
            else:
                print('Увы! Это неправильный ответ!')
                print('Правильный ответ - Анна Каренина ')
                
            print('')
            print('')
            print('Следующий вопрос:')
            
            time.sleep(1)
            
            print('2. Как называется часть серии книг о мальчике который выжил, в которой погибает директор школы?')
            time.sleep(1)
            print()
            print('1. Гарри Поттер и принц Полукровка')
            print('2. Гарри Поттер и кубок Огня')
            print('3. Гарри Поттер и тайная комната')
            print()
            
            bookvoprosik2 = input('Напишите номер варианта: ')
            print('')
            if bookvoprosik2.lower() == 'гарри поттер и принц полукровка' or bookvoprosik2.lower() == 'гарри поттер и принц-полукровка' or bookvoprosik2 == '1':
                print('Верно! Это книга - Гарри Поттер и принц Полукровка! Ты получаешь балл!')
                pointsinbookq +=1
                
            else:
                print('Увы! Это неправильный ответ!')
                print('Правильный ответ - Гарри Поттер и принц Полукровка. ')
                
            print('')
            print('')
            print('Следующий вопрос:')
            
            time.sleep(1)   
            
            print('3. Как называется серия книг, о девочке Василисе, которая умеет управлять временем?')
            time.sleep(1)
            print()
            print('1. Вичхантеры')
            print('2. Хрупкое равновесие')
            print('3. Часодеи')
            print()
            
            
            bookvoprosik3 = input('Напишите номер варианта: ')
            print('')
            if bookvoprosik3 == '3' or bookvoprosik3.lower() == 'часодеи':
                print('Верно! Это серия книг Часодеи, от Натальи Щербы! Ты получаешь балл!')
                pointsinbookq +=1
                
            else:
                print('Увы! Это неправильный ответ!')
                print('Правильный ответ - Часодеи. ')
                
            print('')
            print('')
            print('Следующий вопрос:')
            
            time.sleep(1) 
            
            print('4. Как называется серия книг, об ассасине Селене Сардотин?')
            
            time.sleep(1)
            print()
            print('1. Стеклянный Трон')
            print('2. Шолох')
            print('3. Орудия Смерти')
            print()
            
            bookvoprosik4 = input('Напишите номер варианта: ')
            print('')
            if bookvoprosik4.lower() == 'стеклянный трон' or bookvoprosik4 == '1':
                print('Верно! Это серия книг Стеклянный Трон! Ты получаешь балл!')
                pointsinbookq +=1
                
            else:
                print('Увы! Это неправильный ответ!')
                print('Правильный ответ - Стеклянный Трон. ')
            
            print('')    
            print('')
            print('Следующий вопрос:')
            
            time.sleep(1)
            
            print('5. Как называется книга, где 17-летняя бедная девушка неожиданно получает в наследство 46 миллиардов долларов?')
            time.sleep(1)
            print()
            print('1. Принцесса душ')
            print('2. Игры наследников')
            print('3. Золото в темной ночи')
            print()
            
            bookvoprosik5 = input('Напишите номер варианта: ')
            print('')
            if bookvoprosik5.lower() == 'игры наследников' or bookvoprosik5 == '2':
                print('Верно! Это книга - Игры Наследников! Ты получаешь балл!')
                pointsinbookq +=1
                
            else:
                print('Увы! Это неправильный ответ!')
                print('Правильный ответ - Игры наследников. ')
                
            print('')
            
            time.sleep(3)
            
            print('Это был последний вопрос!')
            
            time.sleep(2)
            
            print('Подсчитываем баллы...')
            print('')
            
            time.sleep(3)
            
            if pointsinbookq == 5:
                print('Поздравяем! Вы получили 5 из 5 баллов! Похоже вы настоящий книжный эксперт!')
                
            elif pointsinbookq == 4:
                print('Вы набрали 4 балла из 5! Это очень хороший результат!')
                
            elif pointsinbookq == 3:
                print('Вы набрали 3 балла из 5. Вы неплохо разбираетесь в литературе!')
                
            elif pointsinbookq == 2:
                print('Вы набрали 2 балла из 5. Надеюсь в следующий раз вам повезет!')    
                
            elif pointsinbookq == 1:
                print('Вы набрали 1 балл из 5. Видимо вы не очень хорошо знаете книги')
                
            elif pointsinbookq == 0:
                print('К сожалению, вы на все вопросы ответили неправильно! Но ничего страшного, вы всегда можете перепройти этот тест! ')
        
            print('')
            
            
            





        
        
                
            
    
        else:
            print('К сожалению, такого квиза пока что нет.')
            
            
            
     
    elif command.lower() == 'тесты' or command == '3':
        print('')
        print('Раздел в разработке...')
            
            
    
    
    elif command.lower() == 'рандомайзер' or command.lower() == 'рандом' or command == '4':
        print('')
        print('РАНДОМАЙЗЕР')
        print('')
        
        while True:
            number1forrandom = int(input('Выберите минимальное число для рандомайзера: '))
            number2forrandom = int(input('Выберите максимальное число для рандомайзера: '))
            
            
            
             
            number = random.randint(number1forrandom, number2forrandom)
            
            print()
            print('Рандом запущен!')
            print('')
            
            
            time.sleep(3)
            print('Ваше число:' ,number,)
            print('')
            break
        
        
    
    
    elif command.lower() == "советчик" or command == '5':
        print('Добро пожаловать в программу Советчик!')
        print("Здесь я буду тебе что-нибудь советовать исходя из твоих предпочтений!")
        time.sleep(2)
        print('')
        print('Вот список того, что я могу посоветовать: ')
        print('1. Игра')
        print('')
        time.sleep(1)
        
        
        viborvsovetchike = input('Введите номер нужной команды: ')
        
        if viborvsovetchike.lower() == 'игра' or viborvsovetchike == '1':
            print()
            print('Хорошо, запускаю программу Советчик - Игра!')
            print('Отвечай на мои вопросы и в конце я выберу самую подходящую игру именно для тебя!')
            print('')
            
            
            print('Какие игры вы предпочитаете: реалистичные(1) или фэнтези(2) ?')
            sovetchikproigri1 = input('Выберите 1 или 2: ')
            print()
            
            print('Выберите: игры с четким сюжетом(1) или игры с открытым миром(2) ')
            sovetchikproigri2 = input('Выберите 1 или 2: ')
            
            print('Вы любите играть с друзьями? Да(1) или Нет(2) ')
            sovetchikproigri3 = input('Выбери 1 или 2: ')
           
            print('') 
            
            if sovetchikproigri1 == '1' and sovetchikproigri2 == '1' and sovetchikproigri3 == '1':
                print('Вам стоит поиграть в Squad!')
                
            elif sovetchikproigri1 == '1' and sovetchikproigri2 == '1' and sovetchikproigri3 == '2' :
                print('Вам стоит поиграть в Arma 3!')    
                
            elif sovetchikproigri1 == '1' and sovetchikproigri2 == '2' and sovetchikproigri3 == '1':
                print('Вам стоит поиграть в GTA Online!')  
                
            elif sovetchikproigri1 == '1' and sovetchikproigri2 == '2' and sovetchikproigri3 == '2':
                print('Вам стоит поиграть в GTA 5')  
                
            elif sovetchikproigri1 == '2' and sovetchikproigri2 == '1' and sovetchikproigri3 == '2' :
                print('Вам стоит поиграть в World of Warcraft!') 
                
            elif sovetchikproigri1 == '2' and sovetchikproigri2 == '1' and sovetchikproigri3 == '1':
                print('Вам стоит поиграть в The Witcher!')  
                    
            elif sovetchikproigri1 == '2' and sovetchikproigri2 == '2' and sovetchikproigri3 == '1':
                print('Вам стоит поиграть в Genshin Impact!')  
                
            elif sovetchikproigri1 == '2' and sovetchikproigri2 == '2' and sovetchikproigri3 == '2':
                print('Вам стоит поиграть в Dark Souls III!') 
                
            else:
                print('Интересные у вас предпочтения...')
                time.sleep(1.5)
                print()
                print('Даже не знаю что посоветовать...')
                time.sleep(1)
                print()
                print('Знаю!')
                time.sleep(2)
                print('Поиграйте в Майнкрафт!')
                
            print('') 
            
        else:
            print('Такой команды еще нет.')
            
            
            
    
        
            
            
        
        
            
                
    elif command.lower() == 'предсказания' or command.lower() == 'предсказание' or command.lower() == 'предсказание на день' or command == '6':
        predskazanije2024 = random.choice(['Сегодня вам лучше не разминать пальцы на правой руке', 
            'Вас ждут проблемы, если вы забудете разморозить курицу', 
            'Сегодня лучше взять зонт, если будет дождь',
            'Лушче подумать, чем не подумать',
            'Сегодня вас ждут вкусности', 'В скором времени вас ждет успех!', 
            "Сегодня будет день, полный возможностей", "Не забывайте о здоровье", 
            "Сегодня может быть хороший день для начала новых проектов", 
            'Вам стоит поставить лайк этому виртуальному помощнику'])


    
        print('🔮🔮🔮  Приветствуем тебя в магическом шаре   🔮🔮🔮')
        
        print(' ')
        time.sleep(1)
        print('Твое  предсказание...')
        time.sleep(1)
        print('🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮')
        time.sleep(2)
        print('')
        print(predskazanije2024)
       
        
    elif command.lower() == 'калькулятор' or command == '7':
        time.sleep(1)
        print()

        print('Добро пожаловать в Калькулятор!')
        print()
        time.sleep(1)
        
        
        
        def add(x, y):
            return x + y
        
        def subtract(x, y):
            return x - y
        
        def multiply(x, y):
            return x * y
        
        def divide(x, y):
            if y == 0:
                return "Ошибка! Деление на ноль недопустимо."
            return x / y
        
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        
        
        time.sleep(2)
        print()
        choiceincalc = input("Введите номер операции (1, 2, 3, 4):")
        
        print()
        number1forcalc = float(input("Введите первое число: "))
        number2forcalc = float(input("Введите второе число: "))
        print()
        
        if choiceincalc == '1':
            print(number1forcalc, "+", number2forcalc, "=", add(number1forcalc, number2forcalc))
        
        elif choiceincalc == '2':
            print(number1forcalc, "-", number2forcalc, "=", subtract(number1forcalc, number2forcalc))
        
        elif choiceincalc == '3':
            print(number1forcalc, "*", number2forcalc, "=", multiply(number1forcalc, number2forcalc))
        
        elif choiceincalc == '4':
            print(number1forcalc, "/", number2forcalc, "=", divide(number1forcalc, number2forcalc))
        else:
            print("Некорректный ввод")
        


 
            
            

            
            
        
        
        
        
        

     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    elif command.lower() == 'техподдержка' or command.lower() == '8':
        time.sleep(1)
        print()
        print('Если вы нашли ошибку, или у вас есть идея по дополнению функционала VirtuAl,')
        print('то напишите мне в телеграм - @wdyh_meee')
        print()
        print()
        print()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    else:
        print("Неверная команда. Пожалуйста, выберите из списка команд.")
        
