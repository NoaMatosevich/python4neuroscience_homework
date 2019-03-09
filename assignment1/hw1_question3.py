def compare_subjects_within_student(subj1_all_students,
                                     subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    # turn each dictionary to a dict containing mean scores for each student    
    for n in subj1_all_students:
        if n=='subject_name':
            continue
        subj1_all_students[n]=(subj1_all_students[n][1]+subj1_all_students[n][0])/2.0
    for m in subj2_all_students:
        if m=='subject_name':
            continue
        subj2_all_students[m]=(subj2_all_students[m][1]+subj2_all_students[m][0])/2.0
    # the result dictionary contains the better subject next to each student name
    result_dic={}
    for i in subj1_all_students:
        if i=='subject_name':
            continue
        try: #the try command allows to test the possibility that there is no corresponding student name in subject 2.
            if subj2_all_students[i]>subj1_all_students[i]:
                result_dic[i]=subj2_all_students['subject_name']
            elif subj2_all_students[i]<subj1_all_students[i]:
                result_dic[i]=subj1_all_students['subject_name']
        except: #this will be triggered when there is no corresponding student name in the 2 lists, that name will be skipped. 
            continue
    print(result_dic)

if __name__ == '__main__':
# Question 3
#each subject is a dictionary containing the subject name, and for each student name there is a 
# tupple containing the 2 test scores
    art={'subject_name':'art', 'Yoni':(80, 67),'Maya':(92, 100), 'Shira':(97, 88), 'Moo':(79, 68), 'Dana':(65,87)}
    physics={'subject_name':'physics', 'Moo':(97, 56),'Maya':(63, 92),'Shira':(99, 75), 'Yoni':(96, 100), 'Yossi':(98, 87)}
    print('Question 3 solution:')
    compare_subjects_within_student(art, physics)
