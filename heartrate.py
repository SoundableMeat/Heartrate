import numpy as np
import matplotlib.pyplot as plt

def heart(fil, filename):
    letters = []
    hr = []
    hra = []

    with fil as f:
        for line in f:
            for letter in line:
                letters.append(letter)

    for i in range(len(letters)-10):
        if letters[i]==":" and letters[i+3]==":":
            if letters[i+9] != ",":
                hr.append(letters[i+7]+letters[i+8]+letters[i+9])
            else:
                hr.append(letters[i+7]+letters[i+8])

    del(hr[0],hr[len(hr)-1])
    for i in range(len(hr)):
        hr[i] = float(hr[i])

    for i in range(len(hr)-4):
        temp=0
        for k in range(-3,4):
            temp+=1/7*hr[i-k]
        hra.append(temp)

    return hra

SMALL_SIZE = 10
MEDIUM_SIZE = 15
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

fil = open("hr.txt","r+")
hr=heart(fil,"hrsorted.txt")

combat = [138,806,1027,1286,1717]
dialogue = [29,83,278,458,709,762,1202,1398,1872,1999,2081,2601,2807,3026,3053]
exploring = [0,330,598,1614,1815,1921,2313,2383,2937]
death = [992,1178]
cgd = [210,909,1119,1372,1774]
combined = combat+dialogue+exploring+death
combined.sort()

hrs=[]
ts=[]
colors=[]
avarages=np.zeros(2)
size=np.zeros(2)

for i in range(len(combined)-1):
    hrs.append([])
    ts.append([])
    if combined[i] in combat:
        colors.append('red')
    elif combined[i] in dialogue:
        colors.append('darkorange')
    elif combined[i] in exploring:
        colors.append('limegreen')
    else:
        colors.append('blue')
    for j in range(combined[i],combined[i+1]+1):
        if combined[i+1]+1>len(hr):
            break
        hrs[i].append(hr[j])
        ts[i].append(j)
        if colors[i]=='red':
            avarages[0]+=hr[j]
            size[0]+=1
        elif colors[i]=='darkorange':
            avarages[1]+=hr[j]
            size[1]+=1
        elif colors[i]=='limegreen':
            avarages[1]+=hr[j]
            size[1]+=1
        else:
            avarages[0]+=hr[j]
            size[0]+=1

for array in ts:
    for i in range(len(array)):
        array[i]=array[i]/60

for i in range(len(avarages)):
    avarages[i]=avarages[i]/size[i]

for i in range(len(hrs)):
    plt.plot(ts[i],hrs[i],c=colors[i])
plt.xlabel("Time / m")
plt.ylabel("Heart Rate / bpm")
plt.title("Heart rate while playing Witcher")
plt.text(2, max(hr), "Combat")
plt.plot(1,max(hr)+1/2,marker='o',c='r')
plt.text(2, max(hr)-3/2, "Exploring")
plt.plot(1,max(hr)-2/2,marker='o',c='limegreen')
plt.text(2, max(hr)-6/2, "Dialogue")
plt.plot(1,max(hr)-5/2,marker='o',c='darkorange')
plt.text(2, max(hr)-9/2, "Dead")
plt.plot(1,max(hr)-8/2,marker='o',c='blue')
plt.axhline(avarages[0],linestyle=':',color='orangered')
plt.axhline(avarages[1],linestyle=':',color='green')
plt.axhline(65,linestyle=':',color='black')
plt.annotate('Avarage combat and death heart rate', xy=((len(hr)-50)/60, avarages[0]), xytext=((len(hr)-1000)/60,  avarages[0]+10),arrowprops=dict(facecolor='red', arrowstyle="-"))
plt.annotate('Avarage exploring and dialoge heart rate', xy=((len(hr)-400)/60, avarages[1]), xytext=((len(hr)-1000)/60,  avarages[1]-11),arrowprops=dict(facecolor='red', arrowstyle="-"))
plt.annotate('Avarage resting heart rate', xy=(10, 65), xytext=(12,  65+3),arrowprops=dict(facecolor='black', arrowstyle="-"))
plt.show()
