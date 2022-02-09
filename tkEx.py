from tkinter import *

root = Tk()
root.title('JOB')
root.geometry('1000x500')

	
class person:
	def __init__(self,name,surname,age,country):
		self.name = name
		self.surname = surname
		self.age = age
		self.country = country

timer = 4

def assignName(firstName):
	global f_Name
	f_Name = firstName
def assignSurname(lastname):
	global l_Name
	l_Name = lastname
def assignAge(ageE):
	global e_Age
	e_Age = ageE
def assignCountry(cCountry):
	global c_Country
	c_Country = cCountry

def submit(x):
	p1 = person(f_Name.get(), l_Name.get(), e_Age.get(), c_Country.get())
	nameLabel = Label(root,text='Name = {}'.format(p1.name),font=('Arial',18))
	nameLabel.grid(column=2,row=6,columnspan=2)
	surnameLabel = Label(root,text='Surname = {}'.format(p1.surname),font=('Arial',18))
	surnameLabel.grid(column=2,row=7,columnspan=2)
	ageLabel = Label(root,text='Age = {}'.format(p1.age),font=('Arial',18))
	ageLabel.grid(column=2,row=8,columnspan=2)
	countryLabel = Label(root,text='Country = {}'.format(p1.country),font=('Arial',18))
	countryLabel.grid(column=2,row=9,columnspan=2)
	
	x.configure(state=DISABLED)

	Button(root,text='Add',width=10,command =lambda : add()).grid(column=4,row=5,columnspan=1)
	saveButton = Button(root,text='Save',width=10,command=lambda:saveIt()).grid(column=5,row=5,columnspan=1)

def add():
	global timer

	p2 = [0]*3
	for j in range(0,3):
		p2[j] = person(f_Name.get(),l_Name.get(),e_Age.get(),c_Country.get())
		nameLabel1 = Label(root,text='Name = {}'.format(p2[j].name),font=('Arial',18))
		nameLabel1.grid(column=timer,row=6,columnspan=1)
		nameLabel2 = Label(root,text='Surname = {}'.format(p2[j].surname),font=('Arial',18))
		nameLabel2.grid(column=timer,row=7,columnspan=1)
		nameLabel3 = Label(root,text='Age = {}'.format(p2[j].age),font=('Arial',18))
		nameLabel3.grid(column=timer,row=8,columnspan=1)
		nameLabel4 = Label(root,text='Country = {}'.format(p2[j].country),font=('Arial',18))
		nameLabel4.grid(column=timer,row=9,columnspan=1)
		timer += 6
		break

def saveIt():
	f = open('Saving.txt','a')
	f.write("Name = {}\n".format(f_Name.get()))
	f.write('Surname = {}\n'.format(l_Name.get()))
	f.write('Age = {}\n'.format(e_Age.get()))
	f.write('Country = {}\n'.format(c_Country.get()))
	f.write('*************\n')

	Label(root,text='Save is Successful!').grid(column=2,row=10)
	f.close()

Label(root, text='Name = ',font=('Arial',18)).grid(column=2,row=1,columnspan=1)
n = StringVar()
inpName = Entry(root,textvariable = n,width=30,command = assignName(n),borderwidth=5).grid(column=3,row=1,columnspan=1)

Label(root, text='Surname = ',font=('Arial',18)).grid(column=2,row=2,columnspan=1)
s = StringVar()
inpSurname = Entry(root,textvariable=s,width=30,command = assignSurname(s),borderwidth=5).grid(column=3,row=2,columnspan=1)

Label(root, text='Age = ',font=('Arial',18)).grid(column=2,row=3,columnspan=1)
a = StringVar()
inpAge = Entry(root,textvariable=a,width=30,command = assignAge(a),borderwidth=5).grid(column=3,row=3,columnspan=1)

Label(root, text='Country = ',font=('Arial',18)).grid(column=2,row=4,columnspan=1)
c = StringVar()
inpCountry = Entry(root,textvariable=c,width=30,command = assignCountry(c),borderwidth=5).grid(column=3,row=4,columnspan=1)

submitButton = Button(root,width=15,text='Submit',state=NORMAL,command = lambda : submit(submitButton))
submitButton.grid(column=3,row=5,columnspan=1)


root.mainloop()