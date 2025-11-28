try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That wasn’t a number.")
else:
    print("You entered", x)
finally:
    print("Done.")

try:
    result = int(input()) / 2
except ValueError:
    print("That wasn't a number.")
except ZeroDivisionError:
    print("Division by zero?")
else:
    print("jciwocj")

try:
    print(x)
except:
    print("An exception hes occurred")

try:
   print(1/int(input()))
except ZeroDivisionError:
   print("You cannot divide a value with zero")
except:
   print("Something else went wrong")

try:
   with open('data.csv') as file:
       read_data = file.read()
except FileNotFoundError as fnf_error:
   print(fnf_error)
   print("Explanation: We cannot load the 'data.csv' file")

try:
   result = 1/int(input("Enter a number: "))
except ZeroDivisionError as err:
   print(err) #what is written after "ZeroDivisionError" ---> (division by zero)
except:
    print("Something else went wrong!")
else:
   print(f"Your answer is {result}")


x = [5,8,9,13]
def find_nth_value(x,n):
    try:
        result = x[n]
    except IndexError as err:
        print(err)
    else:
        print("Your answer is ", result)
find_nth_value(x,0)

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Please change 'y' argument to non-zero value")
    except:
        print("Something went wrong")
    else:
        print(f"Your answer is {result}")
    finally: #No matter what the outcome is, it will always run finally to print “Code by DataCamp”.
        print("\033[92m Code by DataCamp\033[00m")
divide(1, "h")

def file_editor(path,text):
    try:
      data = open(path)
      try:
        data.write(text)
      except:
        print("Unable to write the data. Please add an append: 'a' or write: 'w' parameter to the open() function.")
      finally:
        data.close()
    except:
      print(f"{path} file is not found!!")

path = "data.txt"
text = "DataLab: Share your data analysis in a cloud-based environment--no installation required."
file_editor(path,text)

def file_reader(file_name):
    try:
        with open(file_name) as f: #име на файловия обект
            print(f.read())
    except FileNotFoundError:
        print("Invalid input")
file_reader("file2")
# ако не ползваме with трябва сами да затваряме файла после ---------------->
def file_reader(file_name):
    try:
        f = open(file_name) #име на файловия обект
        print(f.read())
        f.close()
    except FileNotFoundError:
        print("Invalid input")
file_reader("file2")