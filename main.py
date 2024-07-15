from tkinter import * 

window  = Tk()


def conversion() :
  miles = float(miles_input.get())
  km = miles * 1.609344
  result.config(text=km)


window.title("Miles to Kilometer Converter")
window.config(padx= 30 , pady= 30)

miles_input = Entry()
miles_input.grid(column=2 , row= 0)

label1 = Label(text="Miles" , font=("Bold" , 13))
label1.grid(column=3, row = 0 )


label2 = Label(text="is equal to" , font=("Bold" , 13) )
label2.grid(column=0 , row = 1 )

result  = Label(text= 0 , font=("Bold and Italic" , 14))
result.grid(column=2 , row = 1 )

label4 = Label(text = "km" , font=("Bold" , 13))
label4.grid(column=3 , row = 1 )

button = Button(text= "Calculate" , font=("Bold" , 13), command= conversion)
button.grid(column=2 , row = 2 )








window.mainloop()