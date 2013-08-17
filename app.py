#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SYNOPSIS

    .

DESCRIPTION
    

EXAMPLES
    
    python app.py


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

# Basic CSV IO
def read_data(file_name):
    import pandas as pd

    df = pd.read_csv(file_name)
    df = df.sort([' #word'], ascending=[0])

    ts = pd.Series(df[' #word'].values, index=[i for i in range(df[' #word'].count()) ])

    plt.figure(1)
    ts.plot()
    plt.show()

    plt.figure(2)
    ts.cumsum().plot()
    plt.show()

    plt.figure(3)
    def percent(x):
        return (float(x) / ts.sum()) * 100
    ts.cumsum().apply(percent).plot()
    plt.show()

    plt.figure(4)
    for i, f in ts.iteritems():
        ts[i] = (float(f * i * 100) / ts.sum() )   
    ts.plot()
    plt.show()

    plt.figure(5)
    ts[0:100].plot()
    plt.show()

    plt.figure(6)
    ts[0:100].cumsum().plot()
    plt.show()

    plt.figure(7)
    def percent(x):
        return (float(x) / ts.sum()) * 100
    ts[0:100].cumsum().apply(percent).plot()
    plt.show()

    plt.figure(8)
    for i, f in ts.iteritems():
        ts[i] = (float(f * i * 100) / ts.sum() )   
    ts[0:100].plot()
    plt.show()

    plt.figure(9)
    ts = ts.apply(np.log)
    ts.index = [ np.log(i) for i in ts.index]
    ts.plot()
    plt.show()

def main ():
    read_data("data/index.csv")

if __name__ == '__main__':
    main()
    