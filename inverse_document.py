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

def main ():
    
    # Documents 
    D = {
        0 : "I am here on Twitter because my family is on Facebook",
        1 : "Missing Mexico youths identified http://bbc.in/18PTkHR",
        2 : "Mercantilism is one of the great whipping boys in the history of economics http://econ.st/14ph2Lp",
        3 : "On a runway at JFK waiting for a gate My daughter is playing with a Tinker Bell helium balloon http://4sq.com/18PSBXf"
    }

    tf_df = {}

    # Simple Tokenizer
    for i in D:
        D[i] = D[i].split()

    for i in D:
        for token in D[i]:
            if token not in tf_df:
                tf_df[token] = [i]
            else:
                tf_df[token] += [i]

    
    for term in tf_df:
        print " df(%s) = %d" % df(tf_df, term)

    print " tf(%s, %d) = %d" %  tf(tf_df, 'on', 0)

# get the df of a term
def df(tf_df, term):
    return (term, len(set(tf_df[term])))

# get the tf of a term on ducument
def tf(tf_df, term, di):
    return term, di, len([i for i in tf_df[term] if i==di])


if __name__ == '__main__':
    main()
    
