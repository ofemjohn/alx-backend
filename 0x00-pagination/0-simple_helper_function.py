#!/usr/bin/env python3
'''
return in a list for those 
particular pagination parameters.
'''

def index_range(page, page_size):
    '''return a turple '''
    start_index = (page -1) * page_size
    ending_index = start_index + page_size
    return (start_index, ending_index)