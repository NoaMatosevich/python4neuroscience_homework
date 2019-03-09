def compare_subjects_within_student(subj1, subj2):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    # turn each dictionary to a dict containing mean scores for each student    
    for n in subj1:
        subj1[n]=(subj1[n][1]+subj1[n][0])/2.0
    for m in subj2:
        subj2[m]=(subj2[m][1]+subj2[m][0])/2.0
    result_dic={}
    for i in subj1:
        try:
            if subj2[i]>subj1[i]:
                result_dic[i]='subj2'
            elif subj2[i]<subj1[i]:
                result_dic[i]='subj1'
        except:
            continue
    return result_dic
    


art={'Yoni':(80, 67),'Maya':(92, 100), 'Shira':(97, 88), 'Moo':(79, 68), 'Dana':(65,87)}
physics={'Moo':(97, 56),'Maya':(63, 92),'Shira':(99, 75), 'Yoni':(96, 100), 'Yossi':(98, 87)}
results=compare_subjects_within_student(art, physics)
for k in results:
    if results[k]=='subj1':
        results[k]='art'
    else:
        results[k]='physics'
print(results)
