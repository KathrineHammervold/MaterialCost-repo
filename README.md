# SkjellesvikMaterialCost-repo
A web page that tracks the material and labor costs for the new house in Skjellesvik

The web page calls a javascript function that in turn calls an API hosted on a Flask server

The function behind the API reads material choices from an Excel file using the pandas library

The web page currently only displays material choices for different house parts.
The plan is to extend the page so after you make the material choices it will calculate the total price for the materials, based on the data in the Excel file

Each row in the table shows a different part of the house (roof, external walls etc)
In the column called materials, the user can select from a drowdown of materials

The quantity needed for each house part is know and is populated initially. 

This is the structure of the JSON that has the quantities and type of unit
[{"Part":"Roof","Unit":"sqm","Quantity":"20"},
{"Part":"External Walls","Unit":"sqm","Quantity":"100"}]

This is the structure of the JSON that contains the different material choices for each house part
[{"Material 1":"Shingles","Material 2":"Metal","Material 3":"Tiles","Part":"Roof"},{"Material 1":"Brick","Material 2":"Concrete","Material 3":"Wood","Part":"External Walls"},{"Material 1":"Concrete","Material 2":"Stone","Material 3":"Pavers","Part":"Foundation"}]

This is the structure of the JSON that is read from the Excel for supplieres
[{"Material":"Shingles","Supplier":"ABC Shingles","Cost per unit":"10},
{"Material":"Brick","Supplier":"ABC Bricks","Cost per unit":"20"}]
WORKS

When a particular material is selected, the Supplier column shows the available suppliers for the material and their cost per unit. The user can now select a supplier and the Cost per unit column is updated. 
