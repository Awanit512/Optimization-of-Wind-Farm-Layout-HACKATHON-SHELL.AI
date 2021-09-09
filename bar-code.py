from barcode import EAN13
from barcode.writer import ImageWriter
import pyautogui as p
def genrerator(number):
	my_code=EAN13(number,writer=ImageWriter())
	my_code.save("bar-coode")
	take_ss(input("Enter a number  > 0 :"))

def take_ss(stru):
	ss = p.screenshot()
	ss.save("ss"+str(stru)+".png")





if __name__ == "__main__" :
	genrerator(input("Enter 12 digit number : "))
	take_ss(input("Enter a number  > 0 :"))




#Note this programe has two features it generated bar code s wells as take the screenshots the problem is that it takes ssi.e screenshot nly
#for python version 2.x 
#on the other hand it geneated the bar-code for python vesrion 3.7 

#bs yhi problem h agar dono ko ek hi version me lado to badhiya hoga 
 