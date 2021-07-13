s = []
si = int(input('How many students are in this class? Answer : '))
while si < 1:
    print('No class has no students, please try again')
    si = int(input('How many students are in this class? Answer : '))
si2 = si
sic = 1
while si >= 1:
    print('score', str(sic), ': ')
    cs = int(input())
    while cs > 100 or cs < 0:
        print('No score can be among 100 or below 0. score', str(sic), ': ')
        cs = cs 
        cs = input()
        cs = int(cs)
    s.append(cs)
    si = si - 1
    sic = sic + 1

print('Do you want to average the', str(si2), \
          'scores, find the highest and lowest score among them, or both?  (a / m / b)')
amb = str(input())

if amb == 'a':
    s = sum(s)
    s = s / si2
    print('The average of the', str(si2), 'students is', str(s), '.')

if amb == 'm':
    s2 = max(s)
    s3 = min(s)
    print('The highest of the', str(si2), 'scores is', str(s2) + \
                  ', and the lowest score among them is', str(s3) + '.')

if amb == 'b':
    s2 = max(s)
    s3 = min(s)
    s = sum(s)
    s = s / si2
    print('The average of the', str(si2), 'students is', str(s), '.', \
              'The highest of the', str(si2), 'scores is', str(s2) + \
                  ', and the lowest score among them is', str(s3) + '.')
