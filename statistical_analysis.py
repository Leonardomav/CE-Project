"""
Statistical analysis for EC project on the topic of PSO vs ACO
Base code from:
    stat_2016_alunos.py
    Descriptive and inferential statistics in Python.
    Use numpy, scipy and matplotlib.
    Author: Ernesto Costa
"""
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import scipy.stats as st

# obtain data
def get_data(filename):
    data = np.loadtxt(filename)
    return data

def get_data_many(filename):
    data_raw = np.loadtxt(filename)
    data = data_raw.transpose()
    #prfloat(data)
    return data

# describing data

def describe_data(data):
    """ data is a numpy array of values"""
    min_ = np.amin(data)
    max_ = np.amax(data)
    mean_ = np.mean(data)
    median_ = np.median(data)
    mode_ = st.mode(data)
    std_ = np.std(data)
    var_ = np.var(data)
    skew_ = st.skew(data)
    kurtosis_ = st.kurtosis(data)
    q_25, q_50, q_75 = np.percentile(data, [25,50,75])
    basic = 'Min: %s\nMax: %s\nMean: %s\nMedian: %s\nMode: %s\nVar: %s\nStd: %s'
    other = '\nSkew: %s\nKurtosis: %s\nQ25: %s\nQ50: %s\nQ75: %s'
    all_ = basic + other
    prfloat(all_ % (min_,max_,mean_,median_,mode_,var_,std_,skew_,kurtosis_,q_25,q_50,q_75))
    return (min_,max_,mean_,median_,mode_,var_,std_,skew_,kurtosis_,q_25,q_50,q_75)

# visualizing data
def histogram(data,title,xlabel,ylabel,bins=25):
    plt.hist(data,bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    
def histogram_norm(data,title,xlabel,ylabel,bins=20):
    plt.hist(data,normed=1,bins=bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    min_,max_,mean_,median_,mode_,var_,std_,*X = describe_data(data)
    x = np.linspace(min_,max_,1000)
    pdf = st.norm.pdf(x,mean_,std_)
    plt.plot(x,pdf,'r')    
    plt.show()

def box_plot(data, labels):
    plt.boxplot(data,labels=labels)
    plt.show()


# Parametric??
def test_normal_ks(data):
    """Kolgomorov-Smirnov"""
    norm_data = (data - np.mean(data))/(np.std(data)/np.sqrt(len(data)))
    return st.kstest(norm_data,'norm')

def test_normal_sw(data):
    """Shapiro-Wilk"""
    norm_data = (data - np.mean(data))/(np.std(data)/np.sqrt(len(data)))
    return st.shapiro(norm_data)

def levene(data):
    """Test of equal variance. H0 = same variance.
    @W: thev test statistics
    @pval: the p-value
    """
    W,pval = st.levene(*data)
    return(W,pval)

# hypothesis testing
# Parametric
def t_test_ind(data1,data2, eq_var=True):
    """
    parametric
    two samples
    independent
    """
    t,pval = st.ttest_ind(data1,data2, equal_var=eq_var)
    return (t,pval)

def t_test_dep(data1,data2):
    """
    parametric
    two samples
    dependent
    """
    t,pval = st.ttest_rel(data1,data2)
    return (t,pval)

def one_way_ind_anova(data):
    """
    parametric
    many samples
    independent
    """
    F,pval = st.f_oneway(*data)
    return (F,pval)


# Non Parametric
def mann_whitney(data1,data2):
    """
    non parametric
    two samples
    independent
    """    
    return st.mannwhitneyu(data1, data2, 'less')

def wilcoxon(data1,data2):
    """
    non parametric
    two samples
    dependent
    """     
    return st.wilcoxon(data1,data2)

def kruskal_wallis(data):
    """
    non parametric
    many samples
    independent
    """     
    H,pval = st.kruskal(*data)
    return (H,pval)

def friedman_chi(data):
    """
    non parametric
    many samples
    dependent
    """     
    F,pval = st.friedmanchisquare(*data)
    return (F,pval)    
    
# Effect size
def effect_size_t(stat,df):
    r = np.sqrt(stat**2/(stat**2 + df))
    return r

def effect_size_mw(stat,n1,n2):
    """
    n1: size of the first sample
    n2: size of the second sample
    n_ob: number of observations
    """
    n_ob = n1 + n2 
    mean = n1*n2/2
    std = np.sqrt(n1*n2*(n1+n2+1)/12)
    z_score = (stat - mean)/std
    prfloat(z_score)
    return z_score/np.sqrt(n_ob)

def effect_size_wx(stat,n, n_ob):
    """
    n: size of effective sample (zero differences are excluded!)
    n_ob: number of observations = size sample 1 + size sample 2
    """
    mean = n*(n+1)/4
    std = np.sqrt(n*(n+1)*(2*n+1)/24)
    z_score = (stat - mean)/std
    return z_score/np.sqrt(n_ob)
    
if __name__ == '__main__':
    pso_small = []
    pso_medium = []
    pso_large = []
    aco_small = []
    aco_medium = []
    aco_large = []
    for i in range(1,31):
        f = open('test_results/pso_small_w_0.6_cs_1_' + str(i) + '.csv')
        lines = f.readlines()
        f.close()
        pso_small.append(float(lines[-1].split(',')[-2]))

        f = open('test_results/pso_medium_w_0.6_cs_1_' + str(i) + '.csv')
        lines = f.readlines()
        f.close()
        pso_medium.append(float(lines[-1].split(',')[-2]))

        f = open('test_results/pso_large_w_0.6_cs_1_' + str(i) + '.csv')
        lines = f.readlines()
        f.close()
        pso_large.append(float(lines[-1].split(',')[-2]))
        
        f = open('test_results/aco_small_a_1_b_5_e_0.3_' + str(i) + '.csv')
        lines = f.readlines()
        f.close()
        aco_small.append(float(lines[-1].split(',')[-2]))
        
        f = open('test_results/aco_medium_a_1_b_5_e_0.6_' + str(i) + '.csv')
        lines = f.readlines()
        f.close()
        aco_medium.append(float(lines[-1].split(',')[-2]))

        f = open('test_results/aco_large_a_1_b_5_e_0.6_' + str(i) + '.csv')
        lines = f.readlines()
        f.close()
        aco_large.append(float(lines[-1].split(',')[-2]))
    print("Is this data parametric?")
    a, p = test_normal_sw(np.array(pso_small))
    print("pso small:", p < 0.05)
    a, p = test_normal_sw(np.array(pso_medium))
    print("pso medium:", p < 0.05)
    a, p = test_normal_sw(np.array(pso_large))
    print("pso large:", p < 0.05)
    a, p = test_normal_sw(np.array(aco_small))
    print("aco small:", p < 0.05)
    a, p = test_normal_sw(np.array(aco_medium))
    print("aco medium:", p < 0.05)
    a, p = test_normal_sw(np.array(aco_large))
    print("aco large:", p < 0.05)

    a, p = mann_whitney(np.array(pso_small), np.array(aco_small))
    print("Reject pso_small < aco_small:", p < 0.01)
    a, p = mann_whitney(np.array(pso_medium), np.array(aco_medium))
    print("Reject pso_medium < aco_medium:", p < 0.01)
    a, p = mann_whitney(np.array(pso_large), np.array(aco_large))
    print("Reject pso_large < aco_large:", p < 0.01)
