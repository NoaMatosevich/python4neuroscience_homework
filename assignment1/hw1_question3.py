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
        subj1_all_students[n]=max(subj1_all_students[n])
    for m in subj2_all_students:
        if m=='subject_name':
            continue
        subj2_all_students[m]=max(subj2_all_students[m])
    # the result dictionary contains the better subject next to each student name
    result_dic={}
    key_1 = set(subj1_all_students.keys())
    key_2 = set(subj2_all_students.keys())
    key_set = set.intersection(key_1 , key_2) # the intersection command takes only the values that are common in both sets
    for i in key_set:
        if i=='subject_name': #skip the subject name
            continue
        if subj2_all_students[i]>subj1_all_students[i]: #average in subject 2 is higher
                result_dic[i]=subj2_all_students['subject_name']
        elif subj2_all_students[i]<subj1_all_students[i]: # average in subject 1 is higher
                result_dic[i]=subj1_all_students['subject_name']
    print(result_dic)


if __name__ == '__main__':
# Question 3
#each subject is a dictionary containing the subject name, and for each student name there is a 
# tupple containing the 2 test scores
    art={'subject_name':'art', 'Yoni':(80, 67),'Maya':(92, 100), 'Shira':(97, 88), 'Miri':(79, 98), 'Dana':(65,87)}
    physics={'subject_name':'physics', 'Miri':(97, 56),'Maya':(63, 92),'Shira':(99, 75), 'Yoni':(96, 100), 'Yossi':(98, 87)}
    print('Question 3 solution:')
    compare_subjects_within_student(art, physics)
