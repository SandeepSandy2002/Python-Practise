'''4. Student Grading System
   - Write a program to calculate and display student grades.
     - Input: Student's name and marks for 5 subjects.
     - Output: Total marks, percentage, grade (A/B/C/Fail based on percentage).'''

def main():
   student_name=input('enter student name: ')
   (a,b,c,d,e)=list(map(int,input('enter the marks of 5 subjects(out of 100 marks) with space: ').split()))
   subject_marks=int(input('enter total subject marks: '))
   total_marks_scored=a+b+c+d+e
   percentage=float(total_marks_scored/subject_marks*100)
   if percentage<50:
      print(f'{student_name} you got {percentage}% and got Failed,please stop scrolling insta and focus on studies.')
   elif percentage>50 and percentage<=60:
      print(f'{student_name} you got {percentage}% and secured C grade')
   elif percentage>60 and percentage<=70:
      print(f'{student_name} you got {percentage}% and secured B grade')
   else:
      print(f'{student_name} you got {percentage}% and secured A grade')
main()
