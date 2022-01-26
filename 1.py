flatten_list = []
def flatten(liste):
    for eleman in liste:
        if type(eleman) == list:
            flatten(eleman)
        else:
            flatten_list.append(eleman)
flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(flatten_list)
        