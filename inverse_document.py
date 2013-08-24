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
import math

class InvertedDocument:
    def __init__(self, D):
        self.data = {}
        self.N = 0
        self.normalize = {}

        for i in D:
            D[i] = D[i].split()
            self.N += 1

        for i in D:
            for token in D[i]:
                if token not in self.data:
                    self.data[token] = { i : 1}
                else:
                    if i in self.data[token]:
                        self.data[token][i] += 1
                    else:
                        self.data[token][i] = 1

        d = []
        for i in range(self.N):
            for j, token in enumerate(self.data.keys()):
                d += [self.w(token, i)]
            self.normalize[i] = np.linalg.norm(d, 2)
            d = []

    def tf(self, t, d):
        if d in self.data[t]:
            return self.data[t][d]
        else:
            return 0

    def df(self, t):
        return len(self.data[t])

    def idf(self, t):
        def log2(x):
            return math.log(float(x)) / math.log(2.0)
        return log2(self.N) - log2(self.df(t))

    def w(self, t, d):
        return self.tf(t, d) * self.idf(t)

    def dictionary(self):
        return self.data.keys()

    def norm(self, d):
        return self.normalize[d]

    def sim(self, q):
        q = q.split()

        Q = {}
        for token in q:
            if token in Q:
                Q[token] += 1
            else:
                Q[token] = 1

        n = np.linalg.norm(Q.values(), 2)

        for t in Q:
            Q[t] = Q[t] * self.idf(t) / n

        sim = {}
        for i in range(self.N):
            sim[i] = 0
            for t in Q:
                sim[i] += Q[t] * self.w(t, i) / self.norm(i)

        import operator
        sim = sorted(sim.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sim


def sim(self, d, q):
    s = np.dot(q, d)
    n = np.linalg.norm(q, 2) * np.linalg.norm(d, 2)  
    return s[0] / n

def main ():
    
    # Documents 
    D = {
        0 : "I am here on Twitter because my family is on Facebook",
        1 : "Missing Mexico youths identified http://bbc.in/18PTkHR",
        2 : "Mercantilism is one of the great whipping boys in the history of economics http://econ.st/14ph2Lp",
        3 : "On a runway at JFK waiting for a gate My daughter is playing with a Tinker Bell helium balloon http://4sq.com/18PSBXf"
    }

    index = InvertedDocument(D)

    print index.sim('JFK')

if __name__ == '__main__':
    main()