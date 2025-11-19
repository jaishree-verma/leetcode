import openpyxl as xl
wb = xl.load_workbook(r'C:\leetcode\Python\Project1\transaction.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1']
# print(cell.value)
# print("_________")
# output : Transaction
# print(sheet.max_row)      # to get max rows = 4
# print("_________")
for row in range(2, sheet.max_row + 1):   # iterate through each row to get column c values
    # print(row)
    cell = sheet.cell(row, 3)            # row,column = 3
    corrected_price = cell.value * 0.9       # multiply that column with 0.9
    corrected_price_cell = sheet.cell(row,4) # now we add 4th column and store there in col 4
    corrected_price_cell.value = corrected_price
    # print(cell.value)                        # we got values from 3rd column

wb.save('transaction2.xlsx')
# we create and save it in a new file
