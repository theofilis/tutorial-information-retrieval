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
import numpy.linalg as lg
import math

class LatentSematicIndex:

    def __init__(self, D, k):
        self.N = len(D.keys())

        for i in D:
            D[i] = D[i].split()

        self.dictionary = {}
        termId = 0
        for i in D:
            for token in D[i]:
                if token not in self.dictionary:
                    self.dictionary[token] = termId
                    termId = termId + 1

        self.data = np.zeros((len(self.dictionary.keys()), self.N))

        for i in D:
            for token in D[i]:
                self.data[self.dictionary[token], i] += 1

        self.U, self.s, self.V= lg.svd(self.data, full_matrices=False)

        try:
            self.error = self.s[k]
        except IndexError:
            self.error = 0

        self.U = self.U[:, 0:k]
        self.s = self.s[0:k]
        self.V = self.V[0:k, :]

        self.dataAppr = np.dot(self.U, lg.inv(np.diag(self.s)))

    def sim(self, q):
        Q = np.zeros((len(self.dictionary.keys()), 1))

        for token in q.split():
            Q[self.dictionary[token], 0] += 1

        qAppr = np.dot(Q.T, self.dataAppr)

        dAppr = {}
        similarity = {}
        for i in range(self.N):
            dAppr[i] = np.dot(self.data[:, i], self.dataAppr)
            similarity[i] =  np.dot(qAppr, dAppr[i]) / (np.linalg.norm(qAppr, 2) * np.linalg.norm(dAppr[i], 2))
            

        import operator
        sim = sorted(similarity.iteritems(), key=operator.itemgetter(1), reverse=True)
        return sim

def main ():
    
    # Documents 
    D = {
        0 : "I am here on Twitter because my family is on Facebook",
        1 : "Missing Mexico youths identified http://bbc.in/18PTkHR",
        2 : "Mercantilism is one of the great whipping boys in the history of economics http://econ.st/14ph2Lp",
        3 : "On a runway at JFK waiting for a gate My daughter is playing with a Tinker Bell helium balloon http://4sq.com/18PSBXf"
    }

    index = LatentSematicIndex(D, 2)

    print index.sim("Twitter Facebook")

if __name__ == '__main__':
    main()