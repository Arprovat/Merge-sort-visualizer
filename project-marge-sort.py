from tkinter import *
from tkinter import ttk
import time
import random

root = Tk()
root.title("Sorting Algorithms Visualizer")
root.maxsize(1400, 900)
root.config(bg = "white")

algo_name = StringVar()
algo_list = ['Merge Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

arr = []



def displayArr(arr, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    width_x = canvas_width / (len(arr) + 1)
    ini = 4
    space = 2
    tempArr = [i / max(arr) for i in arr]

    for i in range(len(tempArr)):
        x1 = i * width_x + ini + space
        y1 = canvas_height - tempArr[i] * 390
        x2 = (i + 1) * width_x + ini
        y2 = canvas_height
        canvas.create_rectangle(x1, y1, x2, y2, fill=colorArray[i])

    root.update_idletasks()


def createArr():
    global arr

    array_size = 45  

    range_begin = 20

    range_end = 150

    arr = []
    for i in range(0, array_size):  
        random_integer = random.randint(range_begin, range_end) 
        arr.append(random_integer)

    displayArr(arr, ["blue" for x in range(len(arr))])




def set_speed():

    slow = 0.5
    medium = 0.05
    fast = 0.0000001

    if speed_comboBox.get() == 'Slow':
        return slow
    elif speed_comboBox.get() == 'Medium':
        return medium
    elif speed_comboBox.get() =="Fast":
        return fast



def merge(arr, begin, mid, end, displayArr):
    p = begin
    q = mid + 1
    tempArray = []

    for i in range(begin, end+1):
        if p > mid:
            tempArray.append(arr[q])
            q+=1
        elif q > end:
            tempArray.append(arr[p])
            p+=1
        elif arr[p] < arr[q]:
            tempArray.append(arr[p])
            p+=1
        else:
            tempArray.append(arr[q])
            q+=1

    for p in range(len(tempArray)):
        arr[begin] = tempArray[p]
        begin += 1

def merge_sort(arr, begin, end, displayArr, tym):
    if begin < end:
        mid = int((begin + end) / 2)
        merge_sort(arr, begin, mid, displayArr, tym)
        merge_sort(arr, mid+1, end, displayArr, tym)

        merge(arr, begin, mid, end, displayArr)

        displayArr(arr, ["#71189E" if x >= begin and x < mid else "#A225AD" if x == mid 
                        else "#F381FC" if x > mid and x <=end else "blue" for x in range(len(arr))])
        time.sleep(tym)

    displayArr(arr, ["blue" for x in range(len(arr))])




def sort():

    tym = set_speed()
    n = len(arr)

    if algo_comboBox.get()=='Merge Sort':
        merge_sort(arr, 0, len(arr)-1, displayArr, tym)
        
        
        displayArr(arr, ["orange" for x in range(len(arr))])



display_window = Frame(root, width= 900, height=300, bg="white")
display_window.grid(row=0, column=0, padx=10, pady=5)




lbl1 = Label(display_window, text="Algorithm: ", bg="white")
lbl1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_comboBox = ttk.Combobox(display_window, textvariable=algo_name, values=algo_list)
algo_comboBox.grid(row=0, column=1, padx=5, pady=5)
algo_comboBox.current(0)




lbl2 = Label(display_window, text="Sorting Speed: ", bg="white")
lbl2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_comboBox = ttk.Combobox(display_window, textvariable=speed_name, values=speed_list)
speed_comboBox.grid(row=1, column=1, padx=5, pady=5)
speed_comboBox.current(0)



btn1 = Button(display_window, text="Sort", command=sort, bg="gray")
btn1.grid(row=4, column=1, padx=5, pady=5)




btn2 = Button(display_window, text="Create Array", command=createArr, bg="gray")
btn2.grid(row=4, column=0, padx=5, pady=5)



canvas = Canvas(root, width=800, height=400, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)


root.mainloop()
