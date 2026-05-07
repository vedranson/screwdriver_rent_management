{
    "name": "Screwdriver Rental Management",
    "version": "17.0.1.0",
    "category": "Inventory",
    "summary": "Manage screwdriver rentals and inventory",
    "description": "A module to manage screwdriver rentals and inventory in Odoo",
    "author": "Vedran S",
    "depends": [
        "base",
        "mail",
        "contacts",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/screwdriver_menu.xml",
        "views/screwdriver_type_views.xml",
        "views/screwdriver_views.xml",
        "views/res_partner_views.xml",
        "views/screwdriver_rental_views.xml",
        "data/screwdriver_type_data.xml",
        "data/screwdriver_data.xml"
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}