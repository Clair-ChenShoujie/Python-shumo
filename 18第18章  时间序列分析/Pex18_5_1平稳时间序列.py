#程序文件Pex18_5_2.py
#平稳时间序列通常用于分析和预测那些具有稳定统计特性的数据，例如股票收益率、汇率波动等。

import pandas as pd, numpy as np
import statsmodels.api as sm
import matplotlib.pylab as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plt.rc('axes',unicode_minus=False)
plt.rc('font',family='SimHei'); plt.rc('font',size=16)
d=pd.read_csv('E:/数学/数模/Python-MEM-PD-master/18第18章  时间序列分析/sunspots.csv'); dd=d['counts']
years=d['year'].values.astype(int)
plt.plot(years,dd.values,'-*'); plt.figure()
ax1=plt.subplot(121); plot_acf(dd,ax=ax1,title='自相关')
ax2=plt.subplot(122); plot_pacf(dd,ax=ax2,title='偏自相关')

for i in range(1,6):
    for j in range(1,6):
        md=sm.tsa.ARIMA(dd, order=(i, 0, j), trend='n').fit()
        print([i,j,md.aic,md.bic])
zmd=sm.tsa.ARIMA(dd, order=(4, 0, 2), trend='n').fit()
print(zmd.summary())  #显示模型的所有信息

residuals = pd.DataFrame(zmd.resid)
fig, ax = plt.subplots(1,2)
residuals.plot(title="残差", ax=ax[0])
residuals.plot(kind='kde', title='密度', ax=ax[1])
plt.legend(''); plt.ylabel('') 

dhat=zmd.predict(); plt.figure()
plt.plot(years[-20:],dd.values[-20:],'o-k')
plt.plot(years[-20:],dhat.values[-20:],'P--')
plt.legend(('原始观测值','预测值'))
dnext=zmd.predict(d.shape[0],d.shape[0])
print(dnext)  #显示下一期的预测值
plt.show()