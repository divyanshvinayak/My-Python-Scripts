from datetime import datetime
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Question 1
df = pd.read_excel('Covid19IndiaData_30032020.xlsx')
MAX = max(df['Age']) + 1
infected = [0] * MAX
recovered = [0] * MAX
dead = [0] * MAX
infected_males = [0] * MAX
infected_females = [0] * MAX
avg_inf = var_inf = avg_recd = var_recd = avg_dead = var_dead = 0

for i in df.index:
    infected[df['Age'][i]] += 1
    if df['StatusCode'][i] == 'Recovered':
        recovered[df['Age'][i]] += 1
    elif df['StatusCode'][i] == 'Dead':
        dead[df['Age'][i]] += 1
    if df['GenderCode0F1M'][i] == 1:
        infected_males[df['Age'][i]] += 1
    else:
        infected_females[df['Age'][i]] += 1

sinc = sum(infected)
srec = sum(recovered)
sd = sum(dead)
sim = sum(infected_males)
sif = sum(infected_females)

for i in range(MAX):
    infected[i] /= sinc
    recovered[i] /= srec
    dead[i] /= sd
    infected_males[i] /= sim
    infected_females[i] /= sif
    avg_inf += infected[i] * i
    avg_recd += recovered[i] * i
    avg_dead += dead[i] * i
    var_inf += infected[i] * i ** 2
    var_recd += recovered[i] * i ** 2
    var_dead += dead[i] * i ** 2

var_inf -= avg_inf ** 2
var_recd -= avg_recd ** 2
var_dead -= avg_dead ** 2

print('Expected Age of Infected Patients =', avg_inf, 'years')
print('Variance of Age of Infected Patients =', var_inf)
print('Expected Age of Recovered Patients =', avg_recd, 'years')
print('Variance of Age of Recovered Patients =', var_recd)
print('Expected Age of Dead Patients =', avg_dead, 'years')
print('Variance of Age of Dead Patients =', var_dead)

plt.bar(range(MAX), infected)
plt.title('Infected Cases')
plt.xlabel('Age')
plt.ylabel('P(Infected Cases)')
plt.show()

plt.bar(range(MAX), recovered)
plt.title('Recovered Cases')
plt.xlabel('Age')
plt.ylabel('P(Recovered Cases)')
plt.show()

plt.bar(range(MAX), dead)
plt.title('Death Cases')
plt.xlabel('Age')
plt.ylabel('P(Death Cases)')
plt.show()

fig, ax = plt.subplots()
X = np.arange(MAX)
W = 0.5
ax.bar(X - W / 2, infected_males, W, label='Male')
ax.bar(X + W / 2, infected_females, W, label='Female')
ax.set_title('Infected Cases w.r.t Gender')
ax.set_xlabel('Age')
ax.set_ylabel('P(Infected Cases)')
ax.legend()
plt.show()

# Question 2
df = pd.read_excel('linton_supp_tableS1_S2_8Feb2020.xlsx')
df.columns = df.iloc[0]
df = df.reindex(df.index.drop(0)).reset_index(drop=True)
df.columns.name = None

incubation_period = {}
excluded_incubation = {}
onset_hospitalization = {}
hospitalization_death = {}
onset_death = {}
avg_inc = 0
var_inc = 0
avg_inc_ex = 0
var_inc_ex = 0

for i in df.index:
    if type(df['Onset'][i]) is datetime:
        if type(df['ExposureL'][i]) is datetime:
            try:
                incubation_period[(df['Onset'][i] - df['ExposureL'][i]).days] += 1
            except KeyError:
                incubation_period[(df['Onset'][i] - df['ExposureL'][i]).days] = 1
            if df['ExposureType'][i] in {'Contact with Hubei', 'Contact with case', 'Travel to Hubei',
                                         'Travel to Wuhan', 'Contact with Wuhan resident'}:
                try:
                    excluded_incubation[(df['Onset'][i] - df['ExposureL'][i]).days] += 1
                except KeyError:
                    excluded_incubation[(df['Onset'][i] - df['ExposureL'][i]).days] = 1
        if type(df['DateHospitalizedIsolated'][i]) is datetime:
            try:
                onset_hospitalization[(df['DateHospitalizedIsolated'][i] - df['Onset'][i]).days] += 1
            except KeyError:
                onset_hospitalization[(df['DateHospitalizedIsolated'][i] - df['Onset'][i]).days] = 1
            if type(df['DateReportedConfirmed'][i]) is datetime:
                try:
                    onset_death[(df['DateReportedConfirmed'][i] - df['Onset'][i]).days] += 1
                except KeyError:
                    onset_death[(df['DateReportedConfirmed'][i] - df['Onset'][i]).days] = 1
                try:
                    hospitalization_death[
                        (df['DateReportedConfirmed'][i] - df['DateHospitalizedIsolated'][i]).days] += 1
                except KeyError:
                    hospitalization_death[(df['DateReportedConfirmed'][i] - df['DateHospitalizedIsolated'][i]).days] = 1

sinp = sum(incubation_period.values())
sine = sum(excluded_incubation.values())
soh = sum(onset_hospitalization.values())
sod = sum(onset_death.values())
shd = sum(hospitalization_death.values())

for i in incubation_period:
    incubation_period[i] /= sinp
    avg_inc += incubation_period[i] * i
    var_inc += incubation_period[i] * i ** 2

for i in excluded_incubation:
    excluded_incubation[i] /= sine
    avg_inc_ex += excluded_incubation[i] * i
    var_inc_ex += excluded_incubation[i] * i ** 2

for i in onset_hospitalization:
    onset_hospitalization[i] /= soh

for i in onset_death:
    onset_death[i] /= sod

for i in hospitalization_death:
    hospitalization_death[i] /= shd

var_inc -= avg_inc ** 2
var_inc_ex -= avg_inc_ex ** 2

print('Expected Incubation Period =', avg_inc, 'days')
print('Variance of Incubation Period =', var_inc)
print('Expected Incubation Period by Excluding Wuhan Residents =', avg_inc_ex, 'days')
print('Variance of Incubation Period by Excluding Wuhan Residents =', var_inc_ex)

plt.bar(incubation_period.keys(), incubation_period.values())
plt.title('Incubation Period')
plt.xlabel('Incubation Period')
plt.ylabel('P(Incubation Period)')
plt.show()

plt.bar(onset_hospitalization.keys(), onset_hospitalization.values())
plt.title('Onset to Hospitalization')
plt.xlabel('Days')
plt.ylabel('P(Onset to Hospitalization)')
plt.show()

plt.bar(onset_death.keys(), onset_death.values())
plt.title('Onset to Death')
plt.xlabel('Days')
plt.ylabel('P(Onset to Death)')
plt.show()

plt.bar(hospitalization_death.keys(), hospitalization_death.values())
plt.title('Hospitalization to Death')
plt.xlabel('Days')
plt.ylabel('P(Hospitalization to Death)')
plt.show()
