from btree import matrixTree 

#英雄配置
heros = [
    { 'name' : 'mengqi',      'life' : 10000, 'attack' : 100  },
    { 'name' : 'chengyaojin', 'life' : 5000,  'attack' : 200  },
    { 'name' : 'yase' ,       'life' : 2000,  'attack' : 500  },
    { 'name' : 'kai',         'life' : 1000,  'attack' : 1000 },
    { 'name' : 'direnjie',    'life' : 100,   'attack' : 2000 }
]

#地图配置
gameMap = [
    [133  , -523 , -558 , 846  , -907 , -1224, -1346, 787  , -411 , -1826],
    [-1478, -853 , -1401, 341  , -26  , 759  , -444 , 174  , -1594, -2000],
    [861  , -584 , 670  , 696  , 676  , -1674, -1737, -1407, -484 , 248  ],
    [458  , -1669, -419 , -382 , -895 , 732  , -1278, -1802, -527 , 862  ],
    [-1297, 544  , -1943, 563  , -380 , -1268, 266  , -1309, -1946, 85   ],
    [-1981, -1631, -168 , 741  , -211 , -1070, -1873, -554 , 243  , -901 ],
    [849  , 971  , -21  , -1111, 463  , 944  , -124 , -1414, -1463, -1287],
    [70   , -1886, -1159, -73  , 555  , -426 , -190 , -1750, -1028, -188 ],
    [-1220, -1654, -931 , -1100, -433 , -1643, -1281, -455 , 904  , -126 ],
    [-1494, -632 , 243  , 90   , 993  , 322  , 32   , -388 , -225 , 952  ]
]

#遍历地图二叉树，生产英雄能赢得游戏所走过的路径，并算的最终血量, 利用栈进行深度遍历
def btreepaths(hero, gameTree):
    if not gameTree:
        return []

    #路劲数组，根节点入栈
    res, stack = [], [(gameTree, [])]
    while stack:
        #栈弹出
        node, ls = stack.pop()
        #计算根节点沿当前路径到当前节点的数值之和，并且加上英雄初始血量，为英雄当前血量，若该值不大于0，则英雄死亡，跳出当前分支，遍历其他路径
        if sum(map(lambda item : item['data'], ls)) <= - node.val['data'] - hero['life']:
            continue
        if not node.left and not node.right:
            #此时英雄到达叶子节点即敌方基地，往路径数据中添加一条路径并记录英雄血量
            res.append({'path' : ls + [node.val], 'life' : sum(map(lambda item : item['data'], ls)) + node.val['data'] + hero['life']})
        if node.left:
            stack.append((node.left, ls + [ node.val ]))
        if node.right:
            stack.append((node.right, ls + [ node.val ]))
            
    return res

def heroChoice(heros, gameMap):
    result = {}
    #按英雄攻击力从大到小排序
    heros.sort(key = lambda item : item['attack'], reverse = True)
    for hero in heros:
        #由游戏地图生产二叉树，并搜索英雄通关路径,按英雄血量从大到小排序
        paths = btreepaths(hero, matrixTree(gameMap))
        paths.sort(key = lambda item : item['life'], reverse = True)

        #若有通关路经，则选该英雄，并取最终血最多的路径为最优路径
        if paths:
            result['hero'] = hero
            result['path'] = paths[0] 
            break
    return result 

print(heroChoice(heros, gameMap))
