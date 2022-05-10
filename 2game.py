zag = int(input('загадай число: '))
print('\nЗАГАДАЛ '+str(zag)+'\n')
shot=50
i=0
sum1=0
de=50
while i==0:
    if shot<zag:
        print('проверяю '+str(shot)+'\nменьше загаданного')
        shot=round(shot+de)
        de/=2
        sum1+=1
    if shot>zag:
        print('проверяю '+str(shot)+'\nбольше загаданного')
        shot=round(shot-de)      
        de/=2
        sum1+=1
    if shot==zag:
        print('проверяю '+str(shot)+'\nравно загаданному'+'\n\nБЫЛО ЗАГАДАНО '+str(shot)+'\n\nнайдено с '+str(sum1)+' попытки')
        i+=1