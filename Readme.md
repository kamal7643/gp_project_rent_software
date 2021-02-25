#str
main => start page

1      start page => customer page<br/>
1.1 customer page => rent page<br/>
1.2 customer page => return page<br/>
2      start page => admin page<br/>
2.1    admin page => add/remove page<br/>
2.2    admin page => static data<br/>

#file intro<br/>
##src
1.loading.py if fetch takes a while<br/>
2.clear.py clear tk<br/>
3.start.py (home page)<br/>
4.customer.py (for customer purpose)<br/>
5.get_rent.py customer wants a rent car<br/>
6.return_frame.py customer wants to return car<br/>
7.admin.py for admin access<br/>
8.admin_action.py admin want to add or remove <br/>
9.admin_show.py overview on gain <br/>
<br/><br/>
10.__init__.py it enables importing from src folder<br/>
11.RentalSoftware.py whole software is object of this class<br/>
12.vehical.py class for car<br/>
13.update_cache.py when user want to quit <br/>

##cache
1.all.xlsx maintains car objects<br/>
2.general.xlsx has general info<br/>

##main
head for software<br/>

#problems<br/>
y puri window tatti si lag rahi h<br/>

#next<br/>
1. add home button at middle bottom in every page<br/>
2. data management<br/>

## required packages<br/>
1. pip install pillow<br/>
2. pip install pandas<br/>
3. pip install openpyxl xlsxwriter xlrd<br/>
