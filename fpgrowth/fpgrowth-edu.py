from fpgrowth_py import fpgrowth

itemSetList = [['tomatoes','apples', 'oranges'],
                ['chips'],
                ['chips', 'beer', 'apples','oranges'],
                ['apples', 'oranges', 'chips', 'beer', 'tomatoes'],
                ['apples', 'tomatoes','oranges'],
                ['apples', 'oranges', 'chips', 'beer'],
                ['apples', 'oranges','beer', 'chips'],
                ['beer', 'chips','oranges','apples'],
                ['chips', 'beer'],
                ['apples', 'chips', 'beer'],
                ['chips','beer'],
                ['tomatoes'],
                ['oranges', 'apples'],
                ['oranges','apples','beer'],
                ['apples', 'beer', 'tomatoes'],
                ['apples', 'oranges'],
                ['beer'],
                ['apples', 'oranges', 'chips', 'beer', 'tomatoes'],
                ['apples', 'beer','chips'],
                ['chips', 'beer', 'tomatoes'],
                ['chips','beer'],
                ['tomatoes', 'apples'],
                ['oranges', 'apples'],
                ['oranges','apples','tomatoes'],
                ['apples', 'beer', 'tomatoes'],
                ['apples', 'oranges', 'chips'],
                ['beer', 'chips'],
                ['apples', 'oranges', 'chips', 'beer', 'tomatoes'],
                ['apples', 'oranges'],
                ['chips', 'beer', 'tomatoes']]

freqItemSet, rules = fpgrowth(itemSetList, minSupRatio = 0.5, minConf = 0.6)
i = 1
for item in rules:
    print(i, end='. ')
    print(item, end=',\n')
    i += 1
