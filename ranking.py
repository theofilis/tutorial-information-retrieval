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
import networkx as nx

class Ranker:

    def __init__(self, G, a):
        self.A = nx.to_numpy_matrix(G)
        self.N = len(G.nodes())

        for i in range(self.N):
            d = np.sum(self.A[i, :])
            for j in range(self.N):
                if d == 0:
                    self.A[i,j] = 1.0 / float(self.N)
                else:
                    self.A[i,j] = (self.A[i,j] * a * (1.0 / float(d))) + (float(1-a) / float(self.N))

        p0 = np.zeros((self.N, ))
        p0[0] = 1
        
        while(True):
            pn = p0.dot(self.A)
            
            if np.allclose(p0, pn):
                break
            p0 = pn[0]

        self.p = pn


def main ():
    G = nx.Graph()

    G=nx.random_geometric_graph(100,0.125)

    # position is stored as node attribute data for random_geometric_graph
    pos=nx.get_node_attributes(G,'pos')

    # find node near center (0.5,0.5)
    dmin=1
    ncenter=0
    for n in pos:
        x,y=pos[n]
        d=(x-0.5)**2+(y-0.5)**2
        if d<dmin:
            ncenter=n
            dmin=d

    ranker = Ranker(G, 0.1)

    color = []
    for i in range(ranker.N):
        color += [ranker.p[0,i] * 100]

    plt.figure(figsize=(8,8))
    nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.4)
    nx.draw_networkx_nodes(G,pos,nodelist=[i for i in range(ranker.N)],
                           node_size=100,
                           node_color=color,
                           cmap=plt.cm.Reds_r,
                           label=True)

    plt.xlim(-0.05,1.05)
    plt.ylim(-0.05,1.05)
    plt.axis('off')
    plt.savefig('random_geometric_graph.png')
    
    for i in range(ranker.N):
        print(i, ranker.p[0,i] )


if __name__ == '__main__':
    main()
    
