#struture
main => landing page

1.landing page => customer page<br/>
    1.1.customer page => rent page<br/>
    1.2.customer page => return page<br/>

2.landing page => admin page<br/>
    2.1.admin page => add/remove page<br/>
    2.2.admin page => static data<br/>
        2.2.1.static data => gain vs cars<br/>
        2.2.2.static data => demand vs cars<br/>
        2.2.3.static data => spent vs cars<br/>
        2.2.4.stati data => price vs cars<br/>
    2.3.admin page => show info<br/>

#file intro<br/>
##src
1.loading.py if fetch takes a while<br/>
2.clear.py clear tk(not canvas background) <br/>
3.start.py (home page)<br/>
4.customer.py (customer home page)<br/>
5.get_rent.py customer wants a rent car<br/>
6.return_frame.py customer wants to return car<br/>
7.admin.py for admin access<br/>
8.admin_action.py admin want to add or remove <br/>
9.admin_show.py overview on gain <br/>
10.analyze.py static data <br/>
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



## required packages<br/>
1. pip install pillow<br/>
2. pip install pandas<br/>
3. pip install openpyxl xlsxwriter xlrd<br/>
4. pip install matplotlib <br/>
