# MaterialCost-repo
A web page that tracks the material and labor costs for a new farm house

The web page calls a javascript function that in turn calls an API hosted on a Flask server

The function behind the API reads material choices from an Excel file using the pandas library

The web page displays
1. The parts of the house
2. The size of the house part
3. The material choices for the house part
4. The suppliers for the selected material
5. The cost for the selected material from a specific supplier
6. The total cost for the house part given the selected material and supplier

For convenience, all the data is stored in an Excel file in different work sheets (tabs)

Initially, the table is populated with the house parts and their sizes. 
This is the structure of the JSON that has the house parts and their sizes
[{"Part":"Roof","Unit":"sqm","Quantity":"20"},
{"Part":"External Walls","Unit":"sqm","Quantity":"100"}]

This is the structure of the JSON that contains the different material choices for each house part
[{"Material 1":"Shingles","Material 2":"Metal","Material 3":"Tiles","Part":"Roof"},{"Material 1":"Brick","Material 2":"Concrete","Material 3":"Wood","Part":"External Walls"},{"Material 1":"Concrete","Material 2":"Stone","Material 3":"Pavers","Part":"Foundation"}]

This is the structure of the JSON that is read from the Excel for supplieres
[{"Material":"Shingles","Supplier":"ABC Shingles","Cost per unit":"10},
{"Material":"Brick","Supplier":"ABC Bricks","Cost per unit":"20"}]
WORKS

When a particular material is selected, the Supplier column shows the available suppliers for the material and their cost per unit. The user can now select a supplier and the Cost per unit column is updated. 
