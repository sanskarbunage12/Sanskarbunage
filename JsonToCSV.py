def count_rows(csv_filename):
 
  try:
      with open(csv_filename,"r",newline=")as file:
reader=csv.reader(file)

   row_count=sum(1 for row in reader)
   print("Total number of rows:{row_count}")
except fileNotfoundError:
  print("file not found.")
expect Exception as e:
  print(f"An error occurred:{e)")
  
  
  
# Example usage
if__name__=="__main__":
  count_rows(filename)
  
OUTPUT:
Name,Age
ABC,20
XYZ,22
Total number of rows: 3

          