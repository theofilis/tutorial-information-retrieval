#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SYNOPSIS

    .

DESCRIPTION
    

EXAMPLES
    
    python zipf_plot.py


EXIT STATUS
    
    0 program exit normal
    1 program had problem on execution


AUTHOR

    Theofilis George <theofilis.g@gmail.com>

LICENSE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

VERSION

    1
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main ():
    df = pd.read_csv("data/index.csv")
    
    df = df.sort(['#word'], ascending=[0])

    ts = pd.Series(df['#word'].values, index=[i for i in range(df['#word'].count()) ])
    ps = pd.Series(df['#word'].values, index=[i for i in range(df['#word'].count()) ])

    N = ts.sum()
    plt.figure(9)
    ts = ts.apply(np.log10)
    ts.index = [ np.log10(i+1) for i in ts.index]
    ts.plot()
    
    z = np.polyfit( np.array(ts.index, np.float32), ts.values, 1)
    
    y = [ z[1] + z[0] * x for x in  np.array(ts.index, np.float32) ]
    plt.plot(np.array(ts.index, np.float32), y)

    #plt.show()

    print("H κλίση της ευθείας που προσαρμόζει τα σημεία (logr, logf) είναι a=%f" % (z[0]))

    k = 10 ** z[1]
    c = k / N
    print("Η συλλογή έχει c=%f και k=%f" % (c, k))

    N1 = ps[ps == 1].count()
    print("Όροι που εμφανίζονται μία μόνο φορά Ν1=%d" % ( N1 ))

    N1 = (c * N) / 2
    print("Όροι που εμφανίζονται μία μόνο φορά Ν1=%.0f (κατά προσέγγιση)" % ( N1 ))

    invM = (1/(-z[0]))
    N1 = (k ** invM) - ((k / 2)** invM)
    print("Όροι που εμφανίζονται μία μόνο φορά Ν1=%.0f (κατά προσέγγιση)" % ( N1 ))

    F = 100
    N1 = ps[ps > F].count()
    print("Όροι που εμφανίζονται με συχνότητα μεγαλύτερη του 1000 Ν1=%d" % ( N1 ))

    L = np.log10(k / F)
    N1 = 10 ** L
    print("Όροι που εμφανίζονται με συχνότητα μεγαλύτερη του 1000 Ν1=%.0f (κατά προσέγγιση)" % ( N1 ))


if __name__ == '__main__':
    main()
    
