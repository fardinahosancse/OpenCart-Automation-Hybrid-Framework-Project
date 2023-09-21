from Utility import excelReader as XOP

def get_data(sheetname,excel_location):
    path = excel_location
    rows = XOP.get_row(path,sheetname)
    column = XOP.get_column(path,sheetname)
    data=[]

    for r in range(2,rows+1):
        maindata=[]
        for c in range(1,column+1):
            dataAsset = XOP.read_excel(path,sheetname,r,c)
            maindata.insert(c,dataAsset)
        data.insert(r,maindata)
    return data
