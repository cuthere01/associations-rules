# associations-rules

Этот репозиторий содержит реализацию алгоритмов поиска ассоциативных правил на основе различных подходов: Apriori, Efficient-Apriori и FP-Growth.

## Установка зависимостей

#### apriori

```bash
pip install apriori_python
```

#### efficient-apriori

```bash
pip install efficient_apriori
```

#### fpgrowth

```bash
pip install fpgrowth_py
```

#### Для версии с датасетом

```bash
pip install pandas
```

## Теория

Подробнее [тут](https://habr.com/ru/companies/ods/articles/353502/) и [там](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B0%D1%81%D1%81%D0%BE%D1%86%D0%B8%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%BC_%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0%D0%BC)

Ассоциативные правила - это методы для нахождения взаимосвязей между элементами в транзакционных базах данных.
Ассоциативные правила позволяют выявлять взаимосвязи между элементами в больших наборах данных, что может быть полезно для анализа покупательского поведения, оптимизации ассортимента товаров и других задач. Примером таких правил может быть: "если покупатель купил молоко, то с высокой вероятностью он купит и хлеб". Основными метриками при анализе ассоциативных правил являются:

-   Поддержка (Support): вероятность того, что правило выполняется для случайной транзакции.
-   Достоверность (Confidence): вероятность того, что, если левая часть правила выполняется, выполняется и правая.
-   Подъем (Lift): отношение достоверности правила к ожидаемой вероятности выполнения правой части при условии независимости событий.

### Apriori

Алгоритм Apriori - это классический метод для нахождения частых наборов элементов и извлечения ассоциативных правил. Он итерируется по наборам данных, увеличивая размер частых наборов, пока не достигнет заданного минимального значения поддержки. Этот подход неэффективен для больших наборов данных из-за его высокой вычислительной сложности.

### Efficient-Apriori

Алгоритм Efficient-Apriori - это улучшенная версия Apriori, оптимизирующая процесс за счет уменьшения количества необходимых операций и обработки меньшего количества данных. Он сохраняет тот же базовый принцип, но работает быстрее за счет различных оптимизаций.

### FP-Growth

Алгоритм FP-Growth (Frequent Pattern Growth) предлагает другой подход, избегая создания большого количества кандидатов на каждом шаге. Вместо этого он строит FP-дерево, которое затем обходит, чтобы найти частые наборы элементов. Этот алгоритм быстрее, чем Apriori, и подходит для работы с большими наборами данных.
