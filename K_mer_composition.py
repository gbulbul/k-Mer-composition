
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:15:37 2024

@author: gbulb
"""

class updated_k_mers_:
    def get_all_possible_4_mers(comb):
        list_of_alternatives=[]
        for i in list(comb): 
            if ''.join(i) not in list_of_alternatives:
               list_of_alternatives.append(''.join(i))    
        return list_of_alternatives
    def updated_k_mers(dict_,k):  
        dict_for_counts={}
        counter=0
        for value in dict_.values():
            for i in range(0,len(value)-k+1,1):
                if 'A' in value[i:i+k]:
                    value[i:i+k][0].replace(value[i:i+k][0],'A')
                    if 'C' in value[i:i+k]:
                        value[i:i+k][1].replace(value[i:i+k][1],'C')
                        if 'CC' in value[i:i+k]:
                            value[i:i+k][1:3].replace(value[i:i+k][1:3],'CC')
                            if 'G' in value[i:i+k]:
                                value[i:i+k][3].replace(value[i:i+k][3],'G')
                                counter=value.count(value[i:i+k])
                                dict_for_counts[value[i:i+k]]=counter
                            elif 'CCC' in value[i:i+k]:
                                value[i:i+k][1:4].replace(value[i:i+k][1:4],'CCC')
                                counter=value.count(value[i:i+k])
                                dict_for_counts[value[i:i+k]]=counter
                        elif 'G' in value[i:i+k]:
                            value[i:i+k][2].replace(value[i:i+k][2],'G')
                            if 'GG' in value[i:i+k]:
                                value[i:i+k][2:4].replace(value[i:i+k][2:4],'GG')
                                counter=value.count(value[i:i+k])
                                dict_for_counts[value[i:i+k]]=counter
                            elif 'T' in value[i:i+k]:
                                value[i:i+k][3].replace(value[i:i+k][3],'T')
                                counter=value.count(value[i:i+k])
                                dict_for_counts[value[i:i+k]]=counter
                        elif 'T' in value[i:i+k]:
                            value[i:i+k][2].replace(value[i:i+k][2],'T')
                            if 'T' in value[i:i+k]:
                                value[i:i+k][3].replace(value[i:i+k][3],'T')
                                counter=value.count(value[i:i+k])
                                dict_for_counts[value[i:i+k]]=counter
                    if 'G' in value[i:i+k]:
                        value[i:i+k][1].replace(value[i:i+k][1],'G')
                        if 'GG' in value[i:i+k]:
                            value[i:i+k][1:3].replace(value[i:i+k][1:3],'GG')
                            if 'GGG' in value[i:i+k]:
                                value[i:i+k][1:4].replace(value[i:i+k][1:4],'GGG')
                                counter=value.count(value[i:i+k])
                                dict_for_counts[value[i:i+k]]=counter
                            if 'T' in value[i:i+k]:
                                value[i:i+k][3].replace(value[i:i+k][3],'T')
                                counter=value.count(value[i:i+k])
                                dict_for_counts[value[i:i+k]]=counter
                        elif 'T' in value[i:i+k]:
                            value[i:i+k][2].replace(value[i:i+k][2],'T')
                            if 'TT' in value[i:i+k]:
                                value[i:i+k][2:4].replace(value[i:i+k][2:4],'TT')
                                counter=value.count(value[i:i+k])
                                dict_for_counts[value[i:i+k]]=counter
                    if 'T' in value[i:i+k]:
                        value[i:i+k][1].replace(value[i:i+k][1],'T')
                        if 'TTT' in value[i:i+k]:
                            value[i:i+k][1:4].replace(value[i:i+k][1:4],'TTT')   
                            counter=value.count(value[i:i+k])
                            dict_for_counts[value[i:i+k]]=counter
                elif 'AA' in value[i:i+k]:
                    value[i:i+k][:1].replace(value[i:i+k][:1],'AA')
                    if 'C' in value[i:i+k]:
                        value[i:i+k][2].replace(value[i:i+k][2],'C')
                        if 'CC' in value[i:i+k]:
                            value[i:i+k][2:4].replace(value[i:i+k][2:4],'CC')   
                            counter=value.count(value[i:i+k])
                            dict_for_counts[value[i:i+k]]=counter
                        elif 'G' in value[i:i+k]:
                            value[i:i+k][3].replace(value[i:i+k][3],'G')
                            counter=value.count(value[i:i+k])
                            dict_for_counts[value[i:i+k]]=counter
                        elif 'T' in value[i:i+k]:
                            value[i:i+k][3].replace(value[i:i+k][3],'T')
                            counter=value.count(value[i:i+k])
                            dict_for_counts[value[i:i+k]]=counter
                    if 'G' in value[i:i+k]:
                        value[i:i+k][2].replace(value[i:i+k][2],'G')
                        if 'GG' in value[i:i+k]:
                            value[i:i+k][2:4].replace(value[i:i+k][2:4],'GG') 
                            counter=value.count(value[i:i+k])
                            dict_for_counts[value[i:i+k]]=counter
                        elif 'T' in value[i:i+k]:
                            value[i:i+k][3].replace(value[i:i+k][3],'T')   
                            counter=value.count(value[i:i+k])
                            dict_for_counts[value[i:i+k]]=counter
                    if 'T' in value[i:i+k]:
                        value[i:i+k][2].replace(value[i:i+k][2],'T')
                        if 'TT' in value[i:i+k]:
                            value[i:i+k][2:4].replace(value[i:i+k][2:4],'TT')
                            counter=value.count(value[i:i+k])
                            dict_for_counts[value[i:i+k]]=counter
                elif 'AAA' in value[i:i+k]:
                    value[i:i+k][:2].replace(value[i:i+k][:2],'AAA')
                    if 'C' in value[i:i+k]:
                        value[i:i+k][3].replace(value[i:i+k][3],'C') 
                        counter=value.count(value[i:i+k])
                        dict_for_counts[value[i:i+k]]=counter
                    elif 'G' in value[i:i+k]:
                         value[i:i+k][3].replace(value[i:i+k][3],'G')
                         counter=value.count(value[i:i+k])
                         dict_for_counts[value[i:i+k]]=counter
                    elif 'T' in value[i:i+k]:
                          value[i:i+k][3].replace(value[i:i+k][3],'T')
                          counter=value.count(value[i:i+k])
                          dict_for_counts[value[i:i+k]]=counter
                elif 'AAAA' in value[i:i+k]:
                    value[i:i+k][:4].replace(value[i:i+k][:4],'AAAA')
                    counter=value.count(value[i:i+k])
                    dict_for_counts[value[i:i+k]]=counter

                if 'C' in value[i:i+k]:
                    value[i:i+k][0].replace(value[i:i+k][0],'C')
                    if 'CC' in value[i:i+k]:
                        value[i:i+k][0:2].replace(value[i:i+k][0:2],'CC')
                        if 'CCC' in value[i:i+k]:
                            value[i:i+k][0:3].replace(value[i:i+k][0:3],'CCC')
                            if 'C' in value[i:i+k]:
                                value[i:i+k][3].replace(value[i:i+k][3],'C') 
                                counter=value.count(value[i:i+k])
                                dict_for_counts[value[i:i+k]]=counter
                            elif 'G' in value[i:i+k]:
                                 value[i:i+k][3].replace(value[i:i+k][3],'G')
                                 counter=value.count(value[i:i+k])
                                 dict_for_counts[value[i:i+k]]=counter
                            elif 'T' in value[i:i+k]:
                                  value[i:i+k][3].replace(value[i:i+k][3],'T')
                                  counter=value.count(value[i:i+k])
                                  dict_for_counts[value[i:i+k]]=counter
                    elif 'G' in value[i:i+k]:
                        value[i:i+k][1].replace(value[i:i+k][1],'G')
                        if 'G' in value[i:i+k]:
                            value[i:i+k][2].replace(value[i:i+k][2],'G')
                            if 'G' in value[i:i+k]:
                                 value[i:i+k][3].replace(value[i:i+k][3],'G')
                                 counter=value.count(value[i:i+k])
                                 dict_for_counts[value[i:i+k]]=counter
                            elif 'T' in value[i:i+k]:
                                  value[i:i+k][3].replace(value[i:i+k][3],'T')
                                  counter=value.count(value[i:i+k])
                                  dict_for_counts[value[i:i+k]]=counter
                            counter=value.count(value[i:i+k])
                            dict_for_counts[value[i:i+k]]=counter
                        elif 'TT' in value[i:i+k]:
                            value[i:i+k][1:4].replace(value[i:i+k][1:4],'T')
                            counter=value.count(value[i:i+k])
                            dict_for_counts[value[i:i+k]]=counter
                    elif 'T' in value[i:i+k]:
                        value[i:i+k][1].replace(value[i:i+k][1],'T')
                        if 'T' in value[i:i+k]:
                            value[i:i+k][2].replace(value[i:i+k][2],'T')
                            if 'T' in value[i:i+k]:
                                value[i:i+k][3].replace(value[i:i+k][3],'T')
                                counter=value.count(value[i:i+k])
                                dict_for_counts[value[i:i+k]]=counter

                if 'G' in value[i:i+k]:
                    value[i:i+k][0].replace(value[i:i+k][0],'G')
                    if 'G' in value[i:i+k]:
                        value[i:i+k][1].replace(value[i:i+k][1],'G')
                        if 'TT' in value[i:i+k]:
                            value[i:i+k][2:4].replace(value[i:i+k][2:4],'TT')
                            counter=value.count(value[i:i+k])
                            dict_for_counts[value[i:i+k]]=counter
                        elif 'G' in value[i:i+k]:
                             value[i:i+k][2].replace(value[i:i+k][2],'G')
                             if 'G' in value[i:i+k]:
                                  value[i:i+k][3].replace(value[i:i+k][3],'G')
                                  counter=value.count(value[i:i+k])
                                  dict_for_counts[value[i:i+k]]=counter
                             elif 'T' in value[i:i+k]:
                                  value[i:i+k][3].replace(value[i:i+k][3],'T')
                                  counter=value.count(value[i:i+k])
                                  dict_for_counts[value[i:i+k]]=counter
                                  
                    elif 'TTT' in value[i:i+k]:
                          value[i:i+k][1:4].replace(value[i:i+k][1:4],'TTT')
                          counter=value.count(value[i:i+k])
                          dict_for_counts[value[i:i+k]]=counter
                          
                              
                ###{TTTT}####        
                if 'TTTT' in value[i:i+k]:
                    value[i:i+k][0:4].replace(value[i:i+k][0:4],'TTTT')
                    counter=value.count(value[i:i+k])
                    dict_for_counts[value[i:i+k]]=counter              
        return dict_for_counts
    
    def match_all_alternatives_with_frequencies(all_alternative_4ways,dict_for_counts):
         dict_for_matches={}
         for idx,i in enumerate(all_alternative_4ways):
             counter=0
             for key in dict_for_counts.keys():
                 if i == key:
                    counter+=dict_for_counts[key]
                    dict_for_matches[i]=counter
                 else:
                     dict_for_matches[i]=counter            
         return list(dict_for_matches.values())
      
if __name__=="__main__":
    from itertools import combinations_with_replacement  
    k=4
    comb = combinations_with_replacement(['A','C','G','T']*k, k)
    all_alternative_4ways=updated_k_mers_.get_all_possible_4_mers(comb)
    #print(all_alternative_4ways)
    dict_={}
    DNA_string='CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGGCCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGTTTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCAAATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCGGGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGACTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTACCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG'
    dict_['Rosalind_6431']=DNA_string
    dict_for_counts=updated_k_mers_.updated_k_mers(dict_,k)       
    print(updated_k_mers_.match_all_alternatives_with_frequencies(all_alternative_4ways,dict_for_counts))
