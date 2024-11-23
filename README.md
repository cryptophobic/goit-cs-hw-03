## Завдання 1

Створіть базу даних для системи управління завданнями, використовуючи PostgreSQL. База даних має містити таблиці для користувачів, статусів завдань і самих завдань. Виконайте необхідні запити в базі даних системи управління завданнями.

Для завдання був використаний образ postgres з https://hub.docker.com/

команда для запуску виглядає наступним чином
```
docker run -d -e POSTGRES_PASSWORD=admin -p 5431:5432 postgres
```

Приклад роботи із консолі
```
(base) cryptophobic@MacBookPro ~ % psql -hlocalhost -Upostgres -p5431 postgres
Password for user postgres:
psql (14.14 (Homebrew), server 17.2 (Debian 17.2-1.pgdg120+1))
WARNING: psql major version 14, server major version 17.
         Some psql features might not work.
Type "help" for help.

postgres=# SELECT * FROM users;
 id |     fullname     |           email
----+------------------+----------------------------
  2 | Jennifer Smith   | ooliver@example.org
  3 | Laura Flores     | jason91@example.org
  4 | James Taylor     | changamanda@example.net
  5 | Taylor Glenn     | bryan93@example.com
  6 | Catherine Hansen | kelly73@example.net
  7 | Jessica Greene   | ronaldthompson@example.org
  8 | Noah Huang       | davisbobby@example.com
  9 | Jennifer Collins | powellkristin@example.org
 10 | Kevin Henry      | ericksonerin@example.org
  1 | Fedir Ivanovych  | kathyortega@example.net
(10 rows)

postgres=# \dt
         List of relations
 Schema |  Name  | Type  |  Owner
--------+--------+-------+----------
 public | status | table | postgres
 public | tasks  | table | postgres
 public | users  | table | postgres
(3 rows)
```

Credentials для підʼєднання до BD

```
RDS_DB_NAME=postgres
RDS_USERNAME=postgres
RDS_PASSWORD=admin
RDS_HOST=localhost
RDS_PORT=5431
```

ЗА допомогою Faker було створено 10 користувачів та 30 задач до них. 3 статуси були захардкожені заздалегідь при створенні таблиць.
Результат виконання запитів
```
[(4, 'Team know animal keep yourself important scientist.', 'Benefit serve break father far. Weight purpose movie nature.\nAlso seven office bar. Natural science three Mrs food middle our line.\nSo when service probably smile.', 2, 2), (18, 'That outside couple technology give.', 'Could degree drop person edge a similar your. Young bill reduce change.\nPut choose firm enough painting.\nShoulder great ok their act baby. Its trial like generation.', 1, 2)]
[(2, 'Save amount our team program.', 'Tend article certainly successful say. Suggest state range you likely of debate. Main safe government Democrat citizen development play.', 2, 4), (4, 'Team know animal keep yourself important scientist.', 'Benefit serve break father far. Weight purpose movie nature.\nAlso seven office bar. Natural science three Mrs food middle our line.\nSo when service probably smile.', 2, 2), (8, 'I it still reality represent you.', 'Place total debate officer try seven study. House in discuss white interview wind say maybe. Pressure however others politics.', 2, 6), (13, 'Message tough sure turn despite themselves once law.', 'Provide study office against want many star. Language fast total audience American let. Want economy special eight stand teacher.', 2, 10), (15, 'Provide today person choose bag music TV fact.', 'Two environmental central contain understand keep. Defense report trade indeed.', 2, 6), (24, 'Not particularly away experience show image method.', 'Defense deal day property important answer. College personal significant with activity leader put. Enough police some major involve.\nBag bag both natural yeah song. Center chair traditional site.', 2, 10), (25, 'May open southern government ball democratic.', 'Statement threat hope. Author star dark into power charge. Between also mention should.\nNews radio far teacher system soldier. Space catch record make.', 2, 6), (28, 'Nor low weight ever phone particularly money career.', 'Little individual fast court air. Resource value new campaign keep. Land learn throw us.\nStar certainly walk look its decade. Model test question dark care. Him trial positive economy read side red.', 2, 3), (1, 'When actually today charge.', 'Investment girl assume effect instead natural. Official with may indicate quite push. Trade simply east south specific much before artist.', 2, 4)]
None
[(7, 'Jessica Greene', 'ronaldthompson@example.org'), (9, 'Jennifer Collins', 'powellkristin@example.org')]
None
[(2, 'Save amount our team program.', 'Tend article certainly successful say. Suggest state range you likely of debate. Main safe government Democrat citizen development play.', 2, 4), (4, 'Team know animal keep yourself important scientist.', 'Benefit serve break father far. Weight purpose movie nature.\nAlso seven office bar. Natural science three Mrs food middle our line.\nSo when service probably smile.', 2, 2), (6, 'Voice minute try visit population month.', 'Western knowledge city federal manager. Day cup hope boy summer. Agreement hospital third.\nFather difficult glass. Power beyond fish pick board.', 1, 4), (7, 'Sort visit compare idea even.', 'Challenge blue high spring shoulder happy agree. Rise trouble become.', 1, 8), (8, 'I it still reality represent you.', 'Place total debate officer try seven study. House in discuss white interview wind say maybe. Pressure however others politics.', 2, 6), (11, 'Lead top father travel.', 'Buy end rise state fly free no.\nLoss performance later. Institution mouth owner attack prepare. Notice want none quite I ever tax.', 1, 3), (13, 'Message tough sure turn despite themselves once law.', 'Provide study office against want many star. Language fast total audience American let. Want economy special eight stand teacher.', 2, 10), (15, 'Provide today person choose bag music TV fact.', 'Two environmental central contain understand keep. Defense report trade indeed.', 2, 6), (18, 'That outside couple technology give.', 'Could degree drop person edge a similar your. Young bill reduce change.\nPut choose firm enough painting.\nShoulder great ok their act baby. Its trial like generation.', 1, 2), (19, 'Box order audience study.', 'Century cup wife almost model maintain develop. Plant tax large boy ground. Safe nation chance from community answer.\nClearly all fire movement. Third factor if pick.', 1, 8), (22, 'Open discover shake.', 'Institution pay prevent. Push certainly environment a.\nBill state impact upon suggest will.', 1, 1), (24, 'Not particularly away experience show image method.', 'Defense deal day property important answer. College personal significant with activity leader put. Enough police some major involve.\nBag bag both natural yeah song. Center chair traditional site.', 2, 10), (25, 'May open southern government ball democratic.', 'Statement threat hope. Author star dark into power charge. Between also mention should.\nNews radio far teacher system soldier. Space catch record make.', 2, 6), (28, 'Nor low weight ever phone particularly money career.', 'Little individual fast court air. Resource value new campaign keep. Land learn throw us.\nStar certainly walk look its decade. Model test question dark care. Him trial positive economy read side red.', 2, 3), (29, 'Arrive spring protect remember continue deal require drug.', 'Thing executive fear. Save often ask though news cause heavy.\nSystem provide ahead friend term.', 1, 3), (30, 'Tv letter issue development.', 'Reveal perform include executive least people. Guess final certain address author rule.\nMe somebody fish. Thought rule power relationship owner movie audience.', 1, 1), (33, 'Street next low family opportunity.', 'Too painting hand middle common response. Suffer necessary wide sing nothing environment write indicate. Cost keep scene argue. Price some rich follow Mrs.', 2, 1), (1, 'When actually today charge.', 'Investment girl assume effect instead natural. Official with may indicate quite push. Trade simply east south specific much before artist.', 2, 4)]
None
[(1, 'Fedir Ivanovych', 'kathyortega@example.net')]
None
[('completed', 13), ('new', 8), ('in progress', 10)]
[(2, 'Save amount our team program.', 'Tend article certainly successful say. Suggest state range you likely of debate. Main safe government Democrat citizen development play.', 2, 4), (3, 'Market without hit church home rate maintain.', 'Listen yet tonight popular hundred say. Again like bad. Per follow campaign civil nice him spring rock.\nAddress sea visit dinner most game eight. Investment American purpose body social number.', 3, 4), (6, 'Voice minute try visit population month.', 'Western knowledge city federal manager. Day cup hope boy summer. Agreement hospital third.\nFather difficult glass. Power beyond fish pick board.', 1, 4), (8, 'I it still reality represent you.', 'Place total debate officer try seven study. House in discuss white interview wind say maybe. Pressure however others politics.', 2, 6), (9, 'Research career get hotel foreign responsibility.', 'Worker eat food.\nUpon test painting similar act near. Capital risk try hear large yet do. Population adult campaign.', 3, 1), (14, 'Read east system raise age thousand.', 'Race house enough anything. Show once old rest his type plant like.\nEvidence even near continue owner themselves. Although cost ever mission. Life hear arm interview back right.', 3, 6), (15, 'Provide today person choose bag music TV fact.', 'Two environmental central contain understand keep. Defense report trade indeed.', 2, 6), (20, 'Rock growth TV management onto.', 'What itself cost painting. Rather whatever left piece season. Provide poor current without.\nCenter table real worker institution former question people. Painting difference increase work.', 3, 4), (22, 'Open discover shake.', 'Institution pay prevent. Push certainly environment a.\nBill state impact upon suggest will.', 1, 1), (25, 'May open southern government ball democratic.', 'Statement threat hope. Author star dark into power charge. Between also mention should.\nNews radio far teacher system soldier. Space catch record make.', 2, 6), (26, 'Improve how plant surface here point part.', 'Activity rock resource want.\nAccount series voice pull worry. Increase condition page simply seven enough.', 3, 4), (27, 'Positive thousand appear need let audience chance billion.', 'Tree everybody mention drug. Will party onto. Food energy send charge.\nLife office whose. Throughout picture professional wind American final can.', 3, 6), (30, 'Tv letter issue development.', 'Reveal perform include executive least people. Guess final certain address author rule.\nMe somebody fish. Thought rule power relationship owner movie audience.', 1, 1), (33, 'Street next low family opportunity.', 'Too painting hand middle common response. Suffer necessary wide sing nothing environment write indicate. Cost keep scene argue. Price some rich follow Mrs.', 2, 1), (1, 'When actually today charge.', 'Investment girl assume effect instead natural. Official with may indicate quite push. Trade simply east south specific much before artist.', 2, 4)]
[]
[('James Taylor', 'Save amount our team program.', 'Tend article certainly successful say. Suggest state range you likely of debate. Main safe government Democrat citizen development play.'), ('Jennifer Smith', 'Team know animal keep yourself important scientist.', 'Benefit serve break father far. Weight purpose movie nature.\nAlso seven office bar. Natural science three Mrs food middle our line.\nSo when service probably smile.'), ('Catherine Hansen', 'I it still reality represent you.', 'Place total debate officer try seven study. House in discuss white interview wind say maybe. Pressure however others politics.'), ('Kevin Henry', 'Message tough sure turn despite themselves once law.', 'Provide study office against want many star. Language fast total audience American let. Want economy special eight stand teacher.'), ('Catherine Hansen', 'Provide today person choose bag music TV fact.', 'Two environmental central contain understand keep. Defense report trade indeed.'), ('Kevin Henry', 'Not particularly away experience show image method.', 'Defense deal day property important answer. College personal significant with activity leader put. Enough police some major involve.\nBag bag both natural yeah song. Center chair traditional site.'), ('Catherine Hansen', 'May open southern government ball democratic.', 'Statement threat hope. Author star dark into power charge. Between also mention should.\nNews radio far teacher system soldier. Space catch record make.'), ('Laura Flores', 'Nor low weight ever phone particularly money career.', 'Little individual fast court air. Resource value new campaign keep. Land learn throw us.\nStar certainly walk look its decade. Model test question dark care. Him trial positive economy read side red.'), ('Fedir Ivanovych', 'Street next low family opportunity.', 'Too painting hand middle common response. Suffer necessary wide sing nothing environment write indicate. Cost keep scene argue. Price some rich follow Mrs.'), ('James Taylor', 'When actually today charge.', 'Investment girl assume effect instead natural. Official with may indicate quite push. Trade simply east south specific much before artist.')]
[('Jennifer Collins', 0), ('Laura Flores', 4), ('Taylor Glenn', 1), ('James Taylor', 6), ('Kevin Henry', 5), ('Catherine Hansen', 5), ('Jennifer Smith', 2), ('Jessica Greene', 0), ('Fedir Ivanovych', 4), ('Noah Huang', 4)]
```

## Завдання 2
Розробіть Python скрипт, який використовує бібліотеку PyMongo для реалізації основних CRUD (Create, Read, Update, Delete) операцій у MongoDB.

Для завдання був використаний образ mongo з https://hub.docker.com/

команда для запуску виглядає наступним чмнос
```
docker run -p 27017:27017 -d mongo
```

Credentials для підʼєднання до BD

```
MONGO_HOST=localhost
MONGO_PORT=27017
```


```
Меню:
1. Додати кота
2. Показати всіх котів
3. Показати кота за ім'ям
4. Оновити вік кота за ім'ям
5. Додати характеристику коту за ім'ям
6. Видалити кота за ім'ям
7. Видалити всіх котів
0. Вийти
Ваш вибір: 1
Введіть ім'я кота: Оґюст
Введіть вік кота: 37
Введіть характеристики кота через кому: наймудріший
Кіт доданий з _id: 67420109c7cb47be6b2a718d

Меню:
1. Додати кота
2. Показати всіх котів
3. Показати кота за ім'ям
4. Оновити вік кота за ім'ям
5. Додати характеристику коту за ім'ям
6. Видалити кота за ім'ям
7. Видалити всіх котів
0. Вийти
Ваш вибір: 2
{'_id': ObjectId('6741f8a653a6dfff8743f9ed'), 'name': 'Eric', 'age': 11, 'features': ['рудий', 'сцить де попало']}
{'_id': ObjectId('6741fcc9fdfcfb791bbd2796'), 'name': 'Мурзік', 'age': 10, 'features': ['чорний', 'лінивий']}
{'_id': ObjectId('67420109c7cb47be6b2a718d'), 'name': 'Оґюст', 'age': 37, 'features': ['наймудріший']}

Меню:
1. Додати кота
2. Показати всіх котів
3. Показати кота за ім'ям
4. Оновити вік кота за ім'ям
5. Додати характеристику коту за ім'ям
6. Видалити кота за ім'ям
7. Видалити всіх котів
0. Вийти
Ваш вибір: 6
Введіть ім'я кота: Мурзік
Кіт із ім'ям 'Мурзік' видалений.

Меню:
1. Додати кота
2. Показати всіх котів
3. Показати кота за ім'ям
4. Оновити вік кота за ім'ям
5. Додати характеристику коту за ім'ям
6. Видалити кота за ім'ям
7. Видалити всіх котів
0. Вийти
Ваш вибір: 2
{'_id': ObjectId('6741f8a653a6dfff8743f9ed'), 'name': 'Eric', 'age': 11, 'features': ['рудий', 'сцить де попало']}
{'_id': ObjectId('67420109c7cb47be6b2a718d'), 'name': 'Оґюст', 'age': 37, 'features': ['наймудріший']}

Меню:
1. Додати кота
2. Показати всіх котів
3. Показати кота за ім'ям
4. Оновити вік кота за ім'ям
5. Додати характеристику коту за ім'ям
6. Видалити кота за ім'ям
7. Видалити всіх котів
0. Вийти
```
