def herd_the_babies(string):

    # if single or no elements in the supplied string
    if (len(string) <= 1): return string

    # prepare a sorted list of the argument to work upon
    sorted_list = sorted(string)

    # herded_list = [find_children(sorted_list[i], sorted_list[i + 1:])  for i in range(len(sorted_list) - 1)] 

    sorted_herd = ''
    for i in range(len(sorted_list) - 1):
        parent_child =  find_children(sorted_list[i], sorted_list[i + 1:])
        sorted_herd += parent_child if not parent_child in sorted_herd else ''


    sorted_herd += sorted_list[-1] if len(sorted_herd) < len(sorted_list) else ''

    return sorted_herd
    
# get the children of the given parent
def find_children(parent, herd):
    parent_child = parent + ''.join([key for key in herd if parent.lower() == key.lower()])
    return parent_child

