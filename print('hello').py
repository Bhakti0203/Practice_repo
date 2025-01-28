# lst=[['r',3],['a',4],['rr',9],['e',1]]

#     sorted_lst= (sorted(lister))
#     print(sorted_lst)
#     sec_low = sorted_lst[1]
#     print(sec_low)
      
#     second_lowest=[]
#     for name in name_scores:
#         if name[1]==sec_low:
#             second_lowest.append(name[0])
#     print(second_lowest)



# sec_lowest(lst)

# def sec_lowest(name_scores):
#     lister=[]
#     for name in name_scores:
        
   
#         lister.append(name[1])
# lst=[2,3,5,6,3,3,5,3,5,]
# total=0
# for n in lst:
#     total+=n
# print(total)
    
# print(sum(lst))


# def div_num(num,deno):
#     try:
#         res=num/deno
#     except ZeroDivisionError:
#         print('error: division by zero')
#         return None
#     else:
#         print(res)
# div_num(2,0)
# div_num(6,10)
# div_num(34,0)
# div_num(2,33)




# def issubstr(string,substring):
#     i=0
#     j=0
#     while i<len(substring) and j<len(string):
#         if substring[i]==string[j]:
#             i+=1
#         j+=1
#     return i==len(substring)

# print(issubstr('abc','abcdefghij'))


# def issubstr(string,substring):
#     sub=list(substring)
#     stri=list(string)
#     for char in sub:
#         if char  in stri:
#             return True
        
#     return False

# print(issubstr('iii','hello world'))
            
            
            
            
            
# with open('practice.txt','r') as file:
#     content=file.read()
# word=content.split()
# first_four_words=' '.join(word[:4])
# print(first_four_words)

# data='this is extra data'
# with open('practice.txt','w') as file:
#     file.write(data)
# print('successfully writen')


# with open('p2.txt','r') as source_file:
#     with open('practice.txt','w') as destination_file:
#         for line in source_file:
#             destination_file.write(line)


import pandas as pd
df=pd.read_csv('nn.csv')
print(df)
