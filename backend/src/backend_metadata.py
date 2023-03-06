""" This file contains all the **Metadata** information for the *Backend*. """

# The Backend description
DESCRIPTION = """ **Jean Cloud Vinyl API** is the *Backend* of the main Web Site. """

TAGS_METADATA = [
    {
        'name': 'Health Check',
        'description': 'This route **checks** if the *Backend is running*.',
    },
    {
        'name': 'Search Engine',
        'description': 'This route uses the **Algolia search engine**.'
    },
    {
        'name': 'Create Database',
        'description': 'This route **creates** the *Backend database*.',
    },
    {
        'name': 'Sign Up',
        'description': 'This route **adds** a *new user* in the database.',
    },
    {
        'name': 'Add Admin',
        'description': 'This route **adds** a *new admin* in the database.',
    },
    {
        'name': 'Token',
        'description': 'This route takes an *email*, a *password*, and it returns a **token**.',
    },
    {
        'name': 'Token BackOffice',
        'description': 'This route takes a *name*, a *password*, and it returns a **token**.',
    },
    {
        'name': 'Get Users',
        'description': 'This route **gets** *all the users* from the database.',
    },
    {
        'name': 'Get Current User',
        'description': 'This route **gets** all the information of the *current user*.',
    },
    {
        'name': 'Get Orders',
        'description': 'This route **gets** all the orders of a *user*.',
    },
    {
        'name': 'Get Current Admin',
        'description': 'This route **gets** all the information of the *current admin*.',
    },
    {
        'name': 'Add Artist',
        'description': 'This route **adds** a new *artist* in the database.',
    },
    {
        'name': 'Add Album',
        'description': 'This route **adds** a new *album* in the database.',
    },
    {
        'name': 'Add Song',
        'description': 'This route **adds** a new *song* in the database.',
    },
    {
        'name': 'Add Item',
        'description': 'This route **adds** a new *item* in the database.',
    },
    {
        'name': 'Get Artists',
        'description': 'This route **gets** *all the artists* from the database.',
    },
    {
        'name': 'Get Albums',
        'description': 'This route **gets** *all the albums* of an *artist* from the database.',
    },
    {
        'name': 'Get Album',
        'description': 'This route **gets** an *album* from the database.',
    },
    {
        'name': 'Get Songs',
        'description': 'This route **gets** *all the songs* of an *album* from the database.',
    },
    {
        'name': 'Remove Album',
        'description': 'This route allows the *user* to **remove** an *album* from the database.',
    },
    {
        'name': 'Get Items',
        'description': 'This route **gets** *all the items* of an *user* from the database.',
    },
    {
        'name': 'Buy Item',
        'description': 'This route allows the *user* to **buy** an *item* from the database.',
    },
    {
        'name': 'Remove Item',
        'description': 'This route allows the *user* to **remove** an *item* from the database.',
    },
    {
        'name': 'Update Item',
        'description': 'This route allows the *admin* to **update** an *item* from the database.',
    },
]
