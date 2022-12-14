import ast

def comparison(left_elem,right_elem):
    check='tie'
    if (isinstance(left_elem, list))&(isinstance(right_elem, list)):
        for i in range(0,max([len(left_elem),len(right_elem)])):
            
            try:
                left_subelem=left_elem[i]
            except:
                return 'right order'
            try: 
                right_subelem=right_elem[i]
            except:
                return 'bad order'
    
            check=comparison(left_elem[i],right_elem[i])
            if check=='bad order':
                return 'bad order'
            elif check=='right order':
                return 'right order'
            elif check=='tie':
                continue
            else:
                print('error')

    elif (isinstance(left_elem, list))&(isinstance(right_elem, int)):
        check=comparison(left_elem,[right_elem])
    elif (isinstance(left_elem, int))&(isinstance(right_elem, list)):
        check=comparison([left_elem],right_elem)
    elif (isinstance(left_elem, int))&(isinstance(right_elem, int)):
        if left_elem<right_elem:
            return 'right order'
        elif left_elem>right_elem:
            return 'bad order'
        else:
            return 'tie'
    
    return check

left=[[], [0, [[7, 8, 4, 1], 9, 0, 2]], [[2, 7, [], [1, 6], [4, 6]], [7, []], 0, [[1, 0, 5]], 1], [5, [6, [9, 4, 2, 6, 4], 10, [7, 7, 8, 8, 1]], [7, 9, [7]]], []]
right=[[], [9, 3, [[2, 8, 6, 3, 9], 1, 6, [6, 8]]]]
comparison(left,right)

# correct_pairs=[]
# f=open('day13_v1_input.txt','r')
# content=f.readlines()
# paired_content=[content[x:x+3] for x in range(0, len(content), 3)]

# for pair_no,pair in enumerate(paired_content,1):
#     left=pair[0]
#     left=ast.literal_eval(left[:-1])
#     right=pair[1]
#     right=ast.literal_eval(right[:-1])
#     try:
#         response=comparison(left,right)
#     except:
#         print('left',left)
#         print('right',right)
#         break

#     if response=='right order':
#         correct_pairs.append(pair_no)

# print(sum(correct_pairs))