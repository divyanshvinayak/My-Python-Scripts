import pandas as pd


def correlate(x, y):
    n = len(x)
    ex = sum(x) / n
    ey = sum(y) / n
    sx2 = sum(i ** 2 for i in x)
    sy2 = sum(i ** 2 for i in y)
    sxy = sum(x[i] * y[i] for i in range(n))
    return ((sx2 - ex ** 2 * n) / (n - 1)) ** 0.5, ((sy2 - ey ** 2 * n) / (n - 1)) ** 0.5, (
            sxy - ex * ey * n) / (n - 1)


def interpret(r):
    if r == 0:
        return "None"
    if abs(r) <= 0.1:
        return "Weak"
    if abs(r) <= 0.3:
        return "Moderate"
    if abs(r) <= 0.5:
        return "Strong"
    if abs(r) < 1:
        return "Very Strong"
    if abs(r) == 1:
        return "Perfect"


# Question 1 & 2
X = list(map(int, input('X : ').split()))
Y = list(map(int, input('Y : ').split()))
SDX, SDY, COVXY = correlate(X, Y)
print('Cov(X,Y) = {:.6f}'.format(COVXY))
print('r(X,Y) = {:.6f}'.format(COVXY / (SDX * SDY)))

# Question 3
df = pd.read_csv('BNG-Device.csv').dropna().reset_index(drop=True)
SDX, SDY, COVXY = correlate(df['Active-Count'], df['CPU-Utilization'])
print('r(Active-Count,CPU-Utilization) = {:.6f} ({})'.format(COVXY / (SDX * SDY), interpret(COVXY / (SDX * SDY))))
SDX, SDY, COVXY = correlate(df['CPU-Utilization'], df['Total-Memory-Usage'])
print('r(CPU-Utilization,Total-Memory-Usage) = {:.6f} ({})'.format(COVXY / (SDX * SDY), interpret(COVXY / (SDX * SDY))))
SDX, SDY, COVXY = correlate(df['CPU-Utilization'], df['Average-Temperature'])
print(
    'r(CPU-Utilization,Average-Temperature) = {:.6f} ({})'.format(COVXY / (SDX * SDY), interpret(COVXY / (SDX * SDY))))
SDX, SDY, COVXY = correlate(df['Active-Count'], df['Average-Temperature'])
print('r(Active-Count,Average-Temperature) = {:.6f} ({})'.format(COVXY / (SDX * SDY), interpret(COVXY / (SDX * SDY))))
SDX, SDY, COVXY = correlate(df['Total-Memory-Usage'], df['Average-Temperature'])
print('r(Total-Memory-Usage,Average-Temperature) = {:.6f} ({})'.format(COVXY / (SDX * SDY),
                                                                       interpret(COVXY / (SDX * SDY))))
SDX, SDY, COVXY = correlate(df['Active-Count'], df['Total-Memory-Usage'])
print('r(Active-Count,Total-Memory-Usage) = {:.6f} ({})'.format(COVXY / (SDX * SDY),
                                                                interpret(COVXY / (SDX * SDY))))
