## Задача

Построим retrieve-based чат-бота, который будет построен на основе реплик Стэна Марша из South Park.

## Данные

Датасет с репликами взят с Kaggle: https://www.kaggle.com/tovarischsukhov/southparklines

## Baseline-модель

### Подготовка данных

Загрузим в датафрейм CSV с репликами. Каждую строчку очистим от лишних пробельных символов и обрежем.

С помощью Spacy лемматизируем тексты, удалим стоп-слова и пунктуацию.

### Обучение модели

Используем TfidfVectorizer для векторизации текстов.

Для генерации ответов будем использовать косинусный коэффициент между векторами вопроса и всех реплик.

### Оценка результатов

Не впечатляют.

    Q: What's your favorite thing to do with your friends after school?
    A: Yeah, dude. That's my favorite toy.
    Score: 0.4703949944239866

    Q: How do you feel about Wendy?
    A: How are you feeling?
    Score: 0.735900739202231

    Q: What do you think about Eric Cartman?
    A: I didn't think so.
    Score: 0.40745856183234935

    Q: Do you like living in South Park?
    A: What other crime in South Park?
    Score: 0.6029543543540647

    Q: I need to leave now, bye!
    A: No, they're leaving.
    Score: 0.5343109095614417

## BERT для генерации эмбеддингов

### Подготовка данных

Используем предобученную модель `sentence-transformers/all-MiniLM-L6-v2` для токенизации и генерации эмбеддингов.

Загрузим в датафрейм CSV с репликами. Каждую строчку очистим от лишних пробельных символов и обрежем.

### Обучение модели

Для генерации ответов будем использовать косинусный коэффициент между векторами вопроса и всех реплик.

### Оценка результатов

Мы видим большое улучшение в качестве ответов.

    Q: What's your favorite thing to do with your friends after school?
    A: So today we went to the amusement park with all our possible friends. It was a really fun time. We rode all the rides and everyone got along great.
    Score: 0.471310019493103

    Q: How do you feel about Wendy?
    A: Wendy, why is it such a big deal?
    Score: 0.760873019695282

    Q: What do you think about Eric Cartman?
    A: What the hell's wrong with Cartman?!
    Score: 0.6942796111106873

    Q: Do you like living in South Park?
    A: What other crime in South Park?
    Score: 0.5700172185897827

    Q: I need to leave now, bye!
    A: You're leaving already?
    Score: 0.5960509181022644
