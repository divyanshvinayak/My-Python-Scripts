#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 12:00:00 2019

@author: divyanshvinayak
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def readData(filename):
    playerInfo = {'Runs': [], 'Mins': [], 'Balls Faced': [], 'Fours': [], 'Sixes': [], 'Strike Rate': [], 'Batting Position': [], 'Dismissal Type': [], 'Innings': [], 'Opposition': [], 'Ground': [], 'Date': [], 'ODI No': []}
    data = []
    with open(filename) as f:
        header = 1
        for record in f:
            if header != 1:
                data = record.strip().split(',')
                if data[7] == 'not out' or data[7] == 'retired notout':
                    data[0] = data[0].replace('*', '')
                playerInfo['Runs'].append(data[0])
                playerInfo['Mins'].append(data[1])
                playerInfo['Balls Faced'].append(data[2])
                playerInfo['Fours'].append(data[3])
                playerInfo['Sixes'].append(data[4])
                playerInfo['Strike Rate'].append(data[5])
                playerInfo['Batting Position'].append(data[6])
                playerInfo['Dismissal Type'].append(data[7])
                playerInfo['Innings'].append(data[8])
                playerInfo['Opposition'].append(data[9][2:])
                playerInfo['Ground'].append(data[10])
                playerInfo['Date'].append(data[11])
                playerInfo['ODI No'].append(data[12])
            header = 0
    return playerInfo

def readMatchData():
    matchInfo = {'Team 1': [], 'Team 2': [], 'Winner': [], 'Margin': [], 'Ground': [], 'Year': [], 'ODI No': []}
    mdata = []
    with open('mData.csv') as f:
        header = 1
        for record in f:
            if header != 1:
                mdata = record.strip().split(',')
                matchInfo['Team 1'].append(mdata[0])
                matchInfo['Team 2'].append(mdata[1])
                matchInfo['Winner'].append(mdata[2])
                matchInfo['Margin'].append(mdata[3])
                matchInfo['Ground'].append(mdata[4])
                matchInfo['Year'].append(mdata[6])
                matchInfo['ODI No'].append(mdata[7])
            header = 0
    return matchInfo

def findOpposition():
    global teams
    teams = list(set(data['Opposition']))
    teams.sort()
    df = pd.DataFrame({'Teams': teams})
    return df

def plotScore():
    scores = {}
    for team in teams:
        scores[team] = 0
        for i in range(len(data['Runs'])):
            if team == data['Opposition'][i]:
                if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
                    scores[team] += int(data['Runs'][i])
    plt.bar(scores.keys(), scores.values())
    plt.title('Total Runs Scored vs Teams')
    plt.xlabel('Team')
    plt.ylabel('Total Runs Scored')
    plt.show()

def plotAvg():
    avg = {}
    for team in teams:
        scores = [0, 0]
        for i in range(len(data['Runs'])):
            if team == data['Opposition'][i]:
                if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
                    scores[1] += int(data['Runs'][i])
                    if data['Dismissal Type'][i] != 'not out' and data['Dismissal Type'][i] != 'retired notout':
                        scores[0] += 1
        if scores[0] != 0:
            avg[team] = scores[1]/scores[0]
        if scores[0] == 0:
            avg[team] = scores[1]
    plt.bar(avg.keys(), avg.values())
    plt.title('Average vs Teams')
    plt.xlabel('Team')
    plt.ylabel('Average')
    plt.show()
    
def plotMilestones():
    runs = 0
    matches = {}
    j = 1
    k = 0
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
                runs += int(data['Runs'][i])
        if runs >= j*1000:
            matches[str(j*1000)] = i-k
            k = i
            j+=1
    plt.bar(matches.keys(), matches.values())
    plt.title('Number of Matches vs Milestones')
    plt.xlabel('Milestone')
    plt.ylabel('Number of Matches')
    plt.show()

def plotStrikeRate():
    runs = {}
    balls = {}
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            if data['Date'][i][-2:] in runs.keys():
                runs[data['Date'][i][-2:]] += int(data['Runs'][i])
                balls[data['Date'][i][-2:]] += int(data['Balls Faced'][i])
            else:
                runs[data['Date'][i][-2:]] = int(data['Runs'][i])
                balls[data['Date'][i][-2:]] = int(data['Balls Faced'][i])
    strikerate = runs.copy()
    for i in strikerate.keys():
        strikerate[i] /= balls[i]/100
    plt.bar(strikerate.keys(), strikerate.values())
    plt.title('Strike Rate vs Year')
    plt.xlabel('Year')
    plt.ylabel('Strike Rate')
    plt.show()

def calcOverallStrikeRate():
    runs = 0
    balls = 0
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            runs += int(data['Runs'][i])
            balls += int(data['Balls Faced'][i])
    return '%.2f' % (runs/balls*100)

def calcOverallAvg():
    runs = 0
    innings = 0
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            runs += int(data['Runs'][i])
            if data['Dismissal Type'][i] != 'not out' and data['Dismissal Type'][i] != 'retired notout':
                innings += 1
    return '%.2f' % (runs/innings)

def plotDismissalType():
    dismissal = {'Not Out': 0, 'LBW': 0, 'Bowled Out': 0, 'Caught Out': 0, 'Run Out': 0, 'Stumped': 0}
    for i in range(len(data['Dismissal Type'])):
        if data['Dismissal Type'][i] == 'not out' or data['Dismissal Type'][i] == 'retired notout':
            dismissal['Not Out'] += 1
        elif data['Dismissal Type'][i] == 'lbw':
            dismissal['LBW'] += 1
        elif data['Dismissal Type'][i] == 'bowled':
            dismissal['Bowled Out'] += 1
        elif data['Dismissal Type'][i] == 'run out':
            dismissal['Run Out'] += 1
        elif data['Dismissal Type'][i] == 'caught':
            dismissal['Caught Out'] += 1
        elif data['Dismissal Type'][i] == 'stumped':
            dismissal['Stumped'] += 1
    plt.bar(dismissal.keys(), dismissal.values())
    plt.title('Number of Matches vs Dismissal Type')
    plt.xlabel('Dismissal Type')
    plt.ylabel('Number of Matches')
    plt.show()

def plotHScores():
    scores = {}
    hscore = {}
    hsscore = {}
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            if data['Date'][i][-2:] in scores.keys():
                scores[data['Date'][i][-2:]].append(int(data['Runs'][i]))
            else:
                scores[data['Date'][i][-2:]] = [int(data['Runs'][i])]
    for i in scores.keys():
        scores[i].sort()
        hscore[i] = scores[i][-1]
        hsscore[i] = 0
        if len(scores[i]) >= 2: 
            hsscore[i] = scores[i][-2]
    fig, ax = plt.subplots()
    X = np.arange(len(hscore.keys()))
    W = 0.35
    ax.bar(X - W/2, hscore.values(), W, label = 'Highest Score')
    ax.bar(X + W/2, hsscore.values(), W, label = 'Second Highest Score')
    ax.set_title('Highest Scores vs Year')
    ax.set_xticks(X)
    ax.set_xticklabels(hscore.keys())
    ax.set_xlabel('Year')
    ax.set_ylabel('Score')
    ax.legend()
    plt.show()

def plotOverallHScores():
    scores = []
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            scores.append(int(data['Runs'][i]))
    scores.sort()
    hscores = {'Highest': scores[-1], 'Second Highest': scores[-2]} 
    plt.bar(hscores.keys(), hscores.values())
    plt.title('Overall Highest Scores')
    plt.ylabel('Score')
    plt.show()

def calcMaxInnFours():
    fours = []
    for i in data['Fours']:
        if i.isnumeric() == True:
            fours.append(int(i))
    return max(fours)

def plotFours():
    fours = {}
    for i in range(len(data['Fours'])):
        if data['Fours'][i].isnumeric() == True:
            if data['Date'][i][-2:] in fours.keys():
                fours[data['Date'][i][-2:]] += int(data['Fours'][i])
            else:
                fours[data['Date'][i][-2:]] = int(data['Fours'][i])
    plt.bar(fours.keys(), fours.values())
    plt.title('4s vs Year')
    plt.xlabel('Year')
    plt.ylabel('4s')
    plt.show()

def calcOverallFours():
    fours = 0
    for i in range(len(data['Fours'])):
        if data['Fours'][i].isnumeric() == True:
            fours += int(data['Fours'][i])
    return fours

def calcMaxInnSixes():
    sixes = []
    for i in data['Sixes']:
        if i.isnumeric() == True:
            sixes.append(int(i))
    return max(sixes)

def plotSixes():
    sixes = {}
    for i in range(len(data['Sixes'])):
        if data['Sixes'][i].isnumeric() == True:
            if data['Date'][i][-2:] in sixes.keys():
                sixes[data['Date'][i][-2:]] += int(data['Sixes'][i])
            else:
                sixes[data['Date'][i][-2:]] = int(data['Sixes'][i])
    plt.bar(sixes.keys(), sixes.values())
    plt.title('6s vs Year')
    plt.xlabel('Year')
    plt.ylabel('6s')
    plt.show()

def calcOverallSixes():
    sixes = 0
    for i in range(len(data['Sixes'])):
        if data['Sixes'][i].isnumeric() == True:
            sixes += int(data['Sixes'][i])
    return sixes

def plotFifties():
    fifties = {}
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            if int(data['Runs'][i]) >= 50 and int(data['Runs'][i]) < 100:
                if data['Date'][i][-2:] in fifties.keys():
                    fifties[data['Date'][i][-2:]] += 1
                else:
                    fifties[data['Date'][i][-2:]] = 1
    plt.bar(fifties.keys(), fifties.values())
    plt.title('50s vs Year')
    plt.xlabel('Year')
    plt.ylabel('50s')
    plt.show()

def calcAvgMatch2Fifty():
    fifty = 0
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            if int(data['Runs'][i]) >= 50 and int(data['Runs'][i]) < 100:
                fifty += 1
    return '%.2f' % (len(data['Runs'])/fifty)

def plotHundreds():
    hundreds = {}
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            if int(data['Runs'][i]) >= 100:
                if data['Date'][i][-2:] in hundreds.keys():
                    hundreds[data['Date'][i][-2:]] += 1
                else:
                    hundreds[data['Date'][i][-2:]] = 1
    plt.bar(hundreds.keys(), hundreds.values())
    plt.title('100s vs Year')
    plt.xlabel('Year')
    plt.ylabel('100s')
    plt.show()

def calcAvgMatch2Hundred():
    hundred = 0
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            if int(data['Runs'][i]) >= 100:
                hundred += 1
    return '%.2f' % (len(data['Runs'])/hundred)

def plotRuns():
    runs = {}
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            if data['Date'][i][-2:] in runs.keys():
                runs[data['Date'][i][-2:]] += int(data['Runs'][i])
            else:
                runs[data['Date'][i][-2:]] = int(data['Runs'][i])
    plt.plot(list(runs.keys()), list(runs.values()))
    plt.title('Runs vs Year')
    plt.xlabel('Year')
    plt.ylabel('Runs')
    plt.show()

def plotProbability():
    score = {'50+': [0, 0], '100+': [0, 0], '<10': [0, 0]}
    for i in range(len(data['Runs'])):
        if data['Runs'][i] != 'TDNB' and data['Runs'][i] != 'DNB':
            if int(data['Runs'][i]) >= 50 and int(data['Runs'][i]) < 100:
                score['50+'][1] += 1
                if mdata['Winner'][int(data['ODI No'][i][6:])-1] != data['Opposition'][i]:
                    score['50+'][0] += 1
            elif int(data['Runs'][i]) >= 100:
                score['100+'][1] += 1
                if mdata['Winner'][int(data['ODI No'][i][6:])-1] != data['Opposition'][i]:
                    score['100+'][0] += 1
            elif int(data['Runs'][i]) < 10:
                score['<10'][1] += 1
                if mdata['Winner'][int(data['ODI No'][i][6:])-1] != data['Opposition'][i]:
                    score['<10'][0] += 1
    probability = {'50+': score['50+'][0]/score['50+'][1], '100+': score['100+'][0]/score['100+'][1], '<10': score['<10'][0]/score['<10'][1]}
    plt.bar(probability.keys(), probability.values())
    plt.title('Win Probability vs Score')
    plt.xlabel('Score')
    plt.ylabel('Win Probability')
    plt.show()
    
if __name__ == '__main__':
    global data, mdata
    playername = input('Player Name: ').strip().title()
    data = readData(playername+'.csv')
    mdata = readMatchData()
    print(playername+'\'s ODI Career Stats')
    plotHScores()
    plotOverallHScores()
    plotFours()
    plotSixes()
    plotFifties()
    plotHundreds()
    plotRuns()
    findOpposition()
    plotScore()
    plotAvg()
    plotMilestones()
    plotStrikeRate()
    plotProbability()
    plotDismissalType()
    print('The maximum number of fours hit by '+playername+' in an inning among all the innings he has batted is', calcMaxInnFours())
    print('The number of fours hit by '+playername+' in his overall career are', calcOverallFours())
    print('The maximum number of sixes hit by '+playername+' in an inning among all the innings he has batted is', calcMaxInnSixes())
    print('The number of sixes hit by '+playername+' in his overall career are', calcOverallSixes())
    print(playername+' scores a fifty on an average after '+calcAvgMatch2Fifty()+' matches')
    print(playername+' scores a century on an average after '+calcAvgMatch2Hundred()+' matches')
    print('The overall career average of '+playername+' is', calcOverallAvg())
    print('The overall career strike rate of '+playername+' is', calcOverallStrikeRate())
