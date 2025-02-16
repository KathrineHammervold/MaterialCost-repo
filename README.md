# SkjellesvikMaterialCost-repo
A web page that tracks the material and labor costs for the new house in Skjellesvik

The web page calls a javascript function that in turn calls an API hosted on a Flask server

The function behind the API reads material choices from an Excel file using the pandas library

The web page currently only displays material choices for different house parts.
The plan is to extend the page so after you make the material choices it will calculate the total price for the materials, based on the data in the Excel file

