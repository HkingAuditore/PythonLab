def GetDamageExpectation():

    return 80.1132


def GetSpeedExpectation():
    return 0.9738


def GetWalkableExpectation():
    return 20


pg = 0.7
ps = 0.3

damageExpectation = GetDamageExpectation()
speedExpectation = GetSpeedExpectation()
walkableAreaExpectation = GetWalkableExpectation()
enemyAttackExpectation = 22.857 * 2
enemyNumberExpectation = 1.25


def GetStrengthCoefficient(areaCovered: float, hasAirDamage: bool, instantaneousDamage: float, buffDamage: float,
                           buffTime: float,
                           speedInfluence: float, DisplacementDistance: float, coldDownTime: float):
    """
    :param areaCovered:机关占地大小
    :param hasAirDamage:机关是否可以对空中怪物造成伤害
    :param instantaneousDamage:机关瞬时伤害
    :param buffDamage:机关带来的buff的单位时间伤害
    :param buffTime:机关带来的buff的持续时间
    :param speedInfluence:机关带来的buff给怪物赋予的速度变化率
    :param DisplacementDistance:机关对怪物造成的位移格数
    :param coldDownTime:机关的冷却时间
    :return:
    """

    enemyExpectation = pg + ps * hasAirDamage
    singleDamageExpectation = instantaneousDamage + buffDamage * buffTime + damageExpectation * ((
                                                                                                         1 - speedInfluence) * buffTime + DisplacementDistance / speedExpectation)
    coveringExpectation = coldDownTime * walkableAreaExpectation

    return areaCovered * enemyExpectation * singleDamageExpectation / coveringExpectation


print("地刺", GetStrengthCoefficient(1, False, 50, 0, 0, 1, 0, 3.5))

print("齿轮", GetStrengthCoefficient(1, False, 20, 0, 0, 1, 0, 1))

print("跳板", GetStrengthCoefficient(1, False, 0, 0, 0, 1, 2.05, 3.5))

print("拳头", GetStrengthCoefficient(1, True, 12, 0, 0, 1, 1.5, 4.5))

print("飞镖", GetStrengthCoefficient(walkableAreaExpectation * 0.2, True, 40, 0, 0, 1, 0, 3))

print("牢笼", GetStrengthCoefficient(4, True, 0, damageExpectation * 0.25, 300 / (enemyAttackExpectation *
                                                                                enemyNumberExpectation * 4), 1, 0, 1))
