#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
SYNOPSIS

    .

DESCRIPTION
    

EXAMPLES
    
    python inverse_document.py


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
import math

def main ():
    
    # Documents 
    D = {
        0 : "I am here on Twitter because my family is on Facebook",
        1 : "Missing Mexico youths identified http://bbc.in/18PTkHR",
        2 : "Mercantilism is one of the great whipping boys in the history of economics http://econ.st/14ph2Lp",
        3 : "On a runway at JFK waiting for a gate My daughter is playing with a Tinker Bell helium balloon http://4sq.com/18PSBXf"
    }

    tf_df = {}
    N = 0

    # Simple Tokenizer
    for i in D:
        D[i] = D[i].split()
        N += 1

    for i in D:
        for token in D[i]:
            if token not in tf_df:
                tf_df[token] = [i]
            else:
                tf_df[token] += [i]

    q = ['is']

    VS = np.zeros((N, len(tf_df.keys())))
    vq = np.zeros((1, len(tf_df.keys())))

    for i in range(N):
        for j, token in enumerate(tf_df.keys()):
            VS[i, j] = w(tf_df, token, i, N)
    
    for j, token in enumerate(tf_df.keys()):
        if token in q[0].split():
            vq[0,j] =  idf(tf_df, token, N)

    for i in range(N):
        print sim(VS[i], vq)

def sim(d, q):
    s = np.dot(q, d)
    n = np.linalg.norm(q, 2) * np.linalg.norm(d, 2)  
    return s[0] / n


def w(index, t, d, N):
    return tf(index, t, d) * idf(index, t, N)

def log2(x):
    return math.log(float(x)) / math.log(2.0)

def idf(index, t, N):
    return log2(N) - log2(df(index, t))

# get the df of a term
def df(tf_df, term):
    return len(set(tf_df[term]))

# get the tf of a term on ducument
def tf(tf_df, term, di):
    return len([i for i in tf_df[term] if i==di])

if __name__ == '__main__':
    main()