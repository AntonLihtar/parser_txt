"""

"""

a1 = {'a': 1, 'b': 2}
a2 = dict([('a', 1), ('b', 1)])
a3 = dict(a='1', b=2)
a4 = {k: v for k, v in [('a', 1), ('b', 1)]}
a5 = {}
a5['a'] = 1

d = {
    'a': 1,
    'b': 2,
    'c': 13,
    'd': 4,
    'e': 7
}

# def get_max(sl: dict) -> dict:
#     ob = list(sorted(sl.items(), key=lambda x: x[1]))
#     ob2 = dict(ob[:1])
#     ob3 = dict([ob[-1]])
#     ob2.update(ob3)
#     return ob2
# 
# print(get_max(d))

# def set_max(sl: dict) -> dict:
#     # max_value = sorted(sl.values())[-1]
#     max_value = max(sl.values())
#
#     def get_num(num):
#         res = num / max_value
#         return round(res, 2)
#
#     ob = {k: v / max_value for k, v in sl.items()}
#     print(ob)
#
#
# set_max(d)


# d1 = {
#     "MSFT": 1,
#     "IBM": 2,
#     "TXN": 3
# }
# d2 = {
#     "MSFT": 10,
#     "IBM": 20,
#     "TXN": 30,
#     "AIR": 4,
#     "D": 5
# }
#
# def join_sl(sl1, sl2):
#     set1 = set(sl1.keys()) | set(sl2.keys())
#     ob ={}
#     for key in set1:
#         ob[key] = 0
#         if key in sl1:
#             ob[key] += sl1[key]
#         if key in sl2:
#             ob[key] += sl2[key]
#     return ob
#
# print(join_sl(d1, d2))

# prices = {
#     'MSFT': 100,
#     'IBM': 200,
#     'TXN': 30,
#     'ROSN': 15,
#     'T': 40,
#     'AMEX': 16,
#     'DELT': 50
# }
#
# stocks = {
#     'TXN': 2,
#     'T': 3,
#     'DELT': 4
# }
#
# def get_ob(stoks, prices):
#     summ = 0
#     for key, value in stoks.items():
#         price = prices[key]
#         summ += price * value
#     return summ
#
# print(get_ob(stocks, prices))
