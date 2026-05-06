{
    "name": "Screwdriver Rent Management",
    "version": "17.0.1.0",
    "category": "Inventory",
    "summary": "Manage screwdriver rentals and inventory",
    "description": "A module to manage screwdriver rentals and inventory in Odoo",
    "author": "Vedran S",
    "depends": [
        "base"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/screwdriver_menu.xml",
        "views/screwdriver_type_views.xml",
        "data/screwdriver_type_data.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}