import openmc
import openmc.mgxs as mgxs
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_beta(sp_file):
    beta_tally = sp_file.get_tally(name='beta')
    df_b = beta_tally.get_pandas_dataframe()
    beta = df_b['mean'][0] / df_b['mean'][1]
    return beta

def get_flux_dict(sp_file, k, P):
    tally_flux = sp_file.get_tally(name='flux')
    flux = tally_flux.get_slice(scores=['flux'])
    nu_fission = tally_flux.get_slice(scores=['nu-fission'])
    fission = tally_flux.get_slice(scores=['fission'])
    flux_conv_dict = {}
    eg_names = ['eg4', 'eg3', 'eg2', 'eg1']
    egs = [(1e-6, 1.8554), (1.8554, 2.9023e1), (2.9023e1, 9.1188e3), (9.1188e3, 2.0e7)]
    Q = 200 * 1.6022e-13
    V = 27.1 * 3.25 / (100 * 20)
    for x in range(4):
        flux_eg = flux.get_slice(
            filters=[
                openmc.EnergyFilter], filter_bins=[
                (egs[x],)])
        nu_fiss_eg = nu_fission.get_slice(
            filters=[
                openmc.EnergyFilter], filter_bins=[
                (egs[x],)])
        fiss_eg = fission.get_slice(
            filters=[
                openmc.EnergyFilter], filter_bins=[
                (egs[x],)])
        nu = sum(nu_fiss_eg.mean) / sum(fiss_eg.mean)
        N = P * nu / (Q * k)
        flux_conv_dict[eg_names[x]] = flux_eg.mean * 1 / V * N
        flux_conv_dict[eg_names[x]].shape = (20, 100)
        flux_conv_dict[eg_names[x]][np.isnan(flux_conv_dict[eg_names[x]])] = 0
    return flux_conv_dict

def flux_conv(df, k, P):
    Q = 200 * 1.6022e-13  # J/fission
    nu_fission = np.array(
        df[df['score'].str.match('nu-fission')]['mean'])  # n/src
    fission = np.array(df[df['score'] == 'fission']['mean'])  # fission/src
    og_flux = np.array(df[df['score'].str.match('flux')]['mean'])  # n*cm/src
    nu = nu_fission / fission  # n/fission
    N = P * nu / (Q * k)  # src/s
    V = 27.1 * 3.25 #* 1.85
    flux = 1 / V * N * og_flux  # n/(cm2*s)
    return flux

engs = [1.00E-11, 1.00E-10, 5.00E-10, 7.50E-10, 1.00E-09, 1.20E-09,
        1.50E-09, 2.00E-09, 2.50E-09, 3.00E-09, 4.00E-09, 5.00E-09,
        7.50E-09, 1.00E-08, 2.53E-08, 3.00E-08, 4.00E-08, 5.00E-08,
        6.00E-08, 7.00E-08, 8.00E-08, 9.00E-08, 1.00E-07, 1.25E-07,
        1.50E-07, 1.75E-07, 2.00E-07, 2.25E-07, 2.50E-07, 2.75E-07,
        3.00E-07, 3.25E-07, 3.50E-07, 3.75E-07, 4.00E-07, 4.50E-07,
        5.00E-07, 5.50E-07, 6.00E-07, 6.25E-07, 6.50E-07, 7.00E-07,
        7.50E-07, 8.00E-07, 8.50E-07, 9.00E-07, 9.25E-07, 9.50E-07,
        9.75E-07, 1.00E-06, 1.01E-06, 1.02E-06, 1.03E-06, 1.04E-06,
        1.05E-06, 1.06E-06, 1.07E-06, 1.08E-06, 1.09E-06, 1.10E-06,
        1.11E-06, 1.12E-06, 1.13E-06, 1.14E-06, 1.15E-06, 1.18E-06,
        1.20E-06, 1.23E-06, 1.25E-06, 1.30E-06, 1.35E-06, 1.40E-06,
        1.45E-06, 1.50E-06, 1.59E-06, 1.68E-06, 1.77E-06, 1.86E-06,
        1.94E-06, 2.00E-06, 2.12E-06, 2.21E-06, 2.30E-06, 2.38E-06,
        2.47E-06, 2.57E-06, 2.67E-06, 2.77E-06, 2.87E-06, 2.97E-06,
        3.00E-06, 3.10E-06, 3.20E-06, 3.50E-06, 3.73E-06, 4.10E-06,
        4.70E-06, 5.00E-06, 5.40E-06, 6.00E-06, 6.25E-06, 6.50E-06,
        6.75E-06, 6.88E-06, 7.00E-06, 7.15E-06, 8.10E-06, 9.10E-06,
        1.00E-05, 1.15E-05, 1.19E-05, 1.29E-05, 1.44E-05, 1.60E-05,
        1.70E-05, 1.85E-05, 1.94E-05, 2.00E-05, 2.05E-05, 2.12E-05,
        2.18E-05, 2.25E-05, 2.50E-05, 2.75E-05, 3.00E-05, 3.13E-05,
        3.18E-05, 3.33E-05, 3.38E-05, 3.50E-05, 3.55E-05, 3.60E-05,
        3.70E-05, 3.71E-05, 3.73E-05, 3.76E-05, 3.80E-05, 3.91E-05,
        3.96E-05, 4.10E-05, 4.24E-05, 4.40E-05, 4.52E-05, 4.83E-05,
        5.06E-05, 5.34E-05, 5.80E-05, 6.10E-05, 6.30E-05, 6.50E-05,
        6.75E-05, 7.20E-05, 7.60E-05, 8.00E-05, 8.17E-05, 9.00E-05,
        9.70E-05, 1.01E-04, 1.05E-04, 1.08E-04, 1.13E-04, 1.16E-04,
        1.18E-04, 1.19E-04, 1.22E-04, 1.43E-04, 1.70E-04, 1.80E-04,
        1.88E-04, 1.89E-04, 1.92E-04, 1.93E-04, 2.02E-04, 2.07E-04,
        2.10E-04, 2.20E-04, 2.40E-04, 2.85E-04, 3.05E-04, 5.50E-04,
        6.70E-04, 6.83E-04, 9.50E-04, 1.15E-03, 1.50E-03, 1.55E-03,
        1.80E-03, 2.20E-03, 2.25E-03, 2.50E-03, 3.00E-03, 3.74E-03,
        3.90E-03, 5.70E-03, 8.03E-03, 9.50E-03, 1.30E-02, 1.70E-02,
        2.00E-02, 3.00E-02, 4.50E-02, 5.00E-02, 5.20E-02, 6.00E-02,
        7.30E-02, 7.50E-02, 8.20E-02, 8.50E-02, 1.00E-01, 1.28E-01,
        1.49E-01, 2.00E-01, 2.70E-01, 3.30E-01, 4.00E-01, 4.20E-01,
        4.40E-01, 4.70E-01, 4.92E-01, 5.50E-01, 5.73E-01, 6.00E-01,
        6.70E-01, 6.79E-01, 7.50E-01, 8.20E-01, 8.61E-01, 8.75E-01,
        9.00E-01, 9.20E-01, 1.01E+00, 1.10E+00, 1.20E+00, 1.25E+00,
        1.32E+00, 1.36E+00, 1.40E+00, 1.50E+00, 1.85E+00, 2.35E+00,
        2.48E+00, 3.00E+00, 4.30E+00, 4.80E+00, 6.43E+00, 8.19E+00,
        1.00E+01, 1.28E+01, 1.38E+01, 1.46E+01, 1.57E+01, 1.73E+01,
        2.00E+01]
engs = [x * 1e6 for x in engs]

def get_252_spectrum(sp_file, k, P):
    tally_spectrum_all = sp_file.get_tally(name='spectrum all')
    df_spectrum_all = tally_spectrum_all.get_pandas_dataframe()
    index_list = []
    for x in range(252):
        index_list += ['E' + str(x + 1)]
    df_ff = pd.DataFrame(index=index_list)
    df_ff['flux'] = flux_conv(df_spectrum_all, k, P)
    fluxvals = np.append(np.array(df_ff['flux'])[0], np.array(df_ff['flux']))
    return fluxvals

E_4 = [1.8554, 2.9023e1, 9.1188e3, 2.0e7]
bins = []
x = 0
num = 0
for e in engs:
    if e <= E_4[x]:
        num += 1 
    else: 
        bins.append(num)
        x += 1
        num = 0
bins.append(num)
bins = np.array(bins)      

def get_4_spectrum(sp_file, k, P):
    tally_spectrum_4 = sp_file.get_tally(name='spectrum 4 groups')
    df_spectrum_4 = tally_spectrum_4.get_pandas_dataframe()
    index_list = []
    for x in range(4):
        index_list += ['E' + str(x + 1)]
    df_ff = pd.DataFrame(index=index_list)
    df_ff['flux'] = flux_conv(df_spectrum_4, k, P)
    fluxx = np.array(df_ff['flux'])/ bins
    fluxvals = np.append(fluxx[0], fluxx)
    return fluxvals

def reactivity_coefficient_b(
        keff_og,
        keff_og_unc,
        keff_new,
        keff_new_unc,
        temp_change):
    """Generates the reactivity coefficient and its uncertainty

    Parameters
    ----------
    keff_og: float
        original keff
    keff_og_unc: float
        original keff's uncertainty
    keff_new: float
        keff after temperature change
    keff_og_new: float
        keff's uncertainty after temperature change
    temp_change: float
        temperature change (be sure to include +/- sign)

    Returns
    -------
    coeff: float
        reactivity coefficient
    coeff_unc: float
        reactivity coefficient uncertainty
    """
    keff_new = keff_new * 1e-5
    keff_og = keff_og * 1e-5
    keff_new_unc = keff_new_unc * 1e-5
    keff_og_unc = keff_og_unc * 1e-5
    coeff = (keff_new - keff_og) / temp_change / keff_new / keff_og
    coeff_unc = np.sqrt((keff_og_unc / keff_og**2 / temp_change)
                        ** 2 + (keff_new_unc / keff_new**2 / temp_change)**2)

    return coeff, coeff_unc