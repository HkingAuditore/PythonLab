tmpThickness = 0.1
qomolangmaHeight = 8844 * 1000
foldTimes = 0
while tmpThickness < qomolangmaHeight:
    tmpThickness *= 2
    foldTimes += 1
print('当前高度:%.2f米;折叠次数:%d.' % (tmpThickness / 1000.0, foldTimes))
