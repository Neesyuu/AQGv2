from django.shortcuts import render, HttpResponse
from django.utils.timezone import now
from django.contrib import messages
from Dashboard.models import PerQuestionForCertificates
from question.models import AllQues, PhysicsQues, MathQues,EnglishQues,ChemistryQues
from T_Dashboard.views import timeCal

# Create your views here.

def mathCount():
    allMathQues = MathQues.objects.all()
    count = allMathQues.count()
    print(count)
    return count+1


# -------------------- used in ExpertV1 ----------------------------------
def reCalculate(mark, time):
    nTime = round(time)
    if mark == 2:
        if nTime > 2:
            return 3
        elif nTime > 1:
            return 2
        else:
            return 1
    else:
        if nTime > 1:
            return 3
        elif nTime > 0.5:
            return 2
        else:
            return 1


# -------------------- used in ExpertV1 ----------------------------------
def reLeveling(mySub, id, level, avgTime):
    AllQues.objects.filter(pk=id).update(level=level, timeToSolve=avgTime)
    if mySub == 'P':
        PhysicsQues.objects.filter(intQuesID=id).update(level=level, timeToSolve=avgTime)
    elif mySub == 'C':
        ChemistryQues.objects.filter(intQuesID=id).update(level=level, timeToSolve=avgTime)
    elif mySub == 'M':
        MathQues.objects.filter(intQuesID=id).update(level=level, timeToSolve=avgTime)
    elif mySub == 'E':
        EnglishQues.objects.filter(intQuesID=id).update(level=level, timeToSolve=avgTime)


# ----------------- used in direct website -------------------------------
def expertV1(request):
    print('Expert v1.1')
    data1 = PerQuestionForCertificates.objects.all()
    data2 = AllQues.objects.all()
    for i in data2:
        #print('Expert v1.1.data2')
        moreTime = 0
        lessTime = 0
        mtt = 0
        ltt = 0
        timeToSolve = i.timeToSolve
        myMark = int(i.mark)
        myLevel = int(i.level)
        mySub = i.subID
        #print(i.pk)
        idi = i.pk
        data3 = data1.filter(IntQuesID=idi)
        data5 = data1.filter(IntQuesID=idi, Solved=True)
        data4 = data1.filter(IntQuesID=idi, Solved=False)
        totalNoData = len(data3)
        #print('Total')
        #print(totalNoData)
        FalseNoData = len(data4)
        #print('False')
        #print(FalseNoData)
        if totalNoData and FalseNoData:
            FalsePercent = (FalseNoData/totalNoData)*100
            if FalseNoData > 2 and FalsePercent > 70:
                #print('Expert v1.1.False')
                if myLevel == 3:
                    pass
                else:
                    myLevel = myLevel + 1
                    avgTTime = timeCal(myMark, myLevel)
                    reLeveling(mySub, idi, myLevel, avgTTime)
                    print(f'False: reLevel Done of {idi}')


        for j in data5:
            #print('Expert v1.1.data5')
            if j.TimeTaken:
                #print('TimeTaken')
                test1 = round(float(j.TimeTaken))
                # print(test1)
                # print(test1/60)
                # print(float(timeToSolve))
                if (test1/60) > float(timeToSolve):
                    moreTime = moreTime + 1
                    mtt = mtt + (test1/60)
                    #PerQuestionForCertificates.objects.filter(IntQuesID=i.IntQuesID).update(TimeTaken=i.TimeTaken)

                elif (test1/60) < float(timeToSolve):
                    lessTime = lessTime + 1
                    ltt = ltt + (test1 / 60)

        AllQues.objects.filter(pk=idi).update(moreTimeTaken= moreTime, lessTimeTaken= lessTime)

        if moreTime > 2:
            #print('Expert v1.1.moreTIme')
            percent = round((moreTime/totalNoData)*100)
            if percent > 70:
                avgTime = mtt/moreTime
                #print('avgTime')
                print(avgTime)
                newLevel = reCalculate(myMark, avgTime)
                #print('done')

                reLeveling(mySub, i.pk, newLevel, avgTime)
                print(f'MoreTime: reLevel Done of {idi}')

        if lessTime > 2:
            #print('Expert v1.1.lessTime')
            percent = round((lessTime / totalNoData) * 100)
            if percent > 70:
                avgTime = ltt / lessTime
                newLevel = reCalculate(myMark, avgTime)
                reLeveling(mySub, i.pk, newLevel, avgTime)
                print(f'LessTime: reLevel Done of {idi}')

    return HttpResponse('Done')


