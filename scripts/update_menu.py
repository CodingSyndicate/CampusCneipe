#!/usr/bin/env python3

import requests
import pprint
import json
import os
import sys

pp = pprint.PrettyPrinter()
API_KEY = os.environ["R2O_API_KEY"]
INHALTSSTOFFE_ID = 1831828
ALLERGENE_ID = 1843540

BLACKLISTED_PRODUCTGROUPS = [
    "Cocktailzutaten",
    "Pasta Tuesday",
    "Pasta-Tuesday",
    "Special shit",
    "Grillen",
    "Teure Getränke",
    "Favoriten",
    "Specials",
    "TO GO",
    "Deklarationspflichtige Inhaltsstoffe",
    "Deklarationspflichtige Allergene"
]

BLACKLISTED_PRODUCTS = [
    "" #Platzhalter
    ]

FOOTNOTES = {'Allergene': [], 'Inhaltsstoffe': []}
FOOTNOTES_REF = []

def request_pg(productgroup_id):
    product_request = requests.get(
        "https://api.ready2order.com/v1/products",
        params={"productgroup_id": productgroup_id, "includeProductIngredients": True},
        headers={"Authorization": API_KEY},
    )
    products = product_request.json()
    products = sorted(products, key=lambda p: int(p["product_sortIndex"]))
    return products

def build_tree(tree, pgs):
    tree = [e for e in tree if e["productgroup_name"] not in BLACKLISTED_PRODUCTGROUPS]
    pgs = [e for e in pgs if e["productgroup_name"] not in BLACKLISTED_PRODUCTGROUPS]
    tree = sorted(tree, key=lambda pg: int(pg["productgroup_sortIndex"]))
    for e in tree:
        childs_of_e = [c for c in pgs if c["productgroup_parent"] == e["productgroup_id"]]
        e["child_group"] = childs_of_e
        products = request_pg(e['productgroup_id'])
        e["child_products"] = [p for p in products if p["product_name"] not in BLACKLISTED_PRODUCTS]
        build_tree(e["child_group"], pgs)
    return tree

def build_json_menu(tree):
    data = []
    for pg in tree:
        pg_data = {"name": pg["productgroup_name"]}
        if "child_products" in pg:
            pg_data["products"] = []
            for p in pg["child_products"]:
                ingredients = []
                amount = ""
                footnote = []
                if "productingredient" in p:
                    # list ingredient sorted by quantity, in descending order
                    if len(p["productingredient"]) > 0:
                        p["productingredient"].sort(key=lambda e: e["ingredient_quantity"])
                    for ingredient in p["productingredient"]:
                        if ingredient["ingredient_name"] == "Liter":
                            amount = "{:0,.2f}".format(float(ingredient["ingredient_quantity"])).rstrip("0").rstrip(".")
                        else: #footnote
                            #print((p['product_name'], ingredient), file=sys.stderr)
                            footnote.append(ingredient['ingredient_id'])
                            reference_ingredient(ingredient['ingredient_id'])
#                            if ingredient['ingredient_name'] not in INHALTSSTOFFE:
#                                INHALTSSTOFFE.append(ingredient['ingredient_name'])
#                            footnote.append(str(INHALTSSTOFFE.index(ingredient['ingredient_name'])))
#                footnote.sort()
                pg_data["products"].append(
                    {"name": p["product_name"],
                     "price": "{:0,.2f}".format(float(p["product_price"])),
                     "ingredients": p["product_description"].lstrip("Zutaten").lstrip(":").lstrip(),
                     "amount": amount,
                     "ingredient_ids": footnote}
                )
        if "child_group" in pg:
            pg_data["childs"] = build_json_menu(pg["child_group"])
        data.append(pg_data)
    return data

def reference_ingredient(ingredient_id):
    FOOTNOTES_REF.append(ingredient_id)
    
def get_footnotes():
    return {
        'inhaltsstoffe': request_pg(INHALTSSTOFFE_ID),
        'allergene': request_pg(ALLERGENE_ID)
    }

def get_reference(Id):
    allergen_key = next((allergen['footnote_key'] for allergen in ALLERGENE if allergen['product_id'] == Id), None)
    inhaltsstoff_key = next((inhaltsstoff['footnote_key'] for inhaltsstoff in INHALTSSTOFFE if inhaltsstoff['product_id'] == Id), None)

    if allergen_key is not None:
        return allergen_key
    elif inhaltsstoff_key is not None:
        return inhaltsstoff_key
    else:
        raise Exception("should not happen")

def set_footnotes(menu):
    for pg in menu:
        if 'products' in pg:
            for p in pg['products']:
                p['footnote_keys'] = []
                for Id in p['ingredient_ids']:
                    # replace id with footnote key
                    p['footnote_keys'].append(get_reference(Id))
                del p['ingredient_ids']
        if "childs" in pg:
            set_footnotes(pg['childs'])
    return menu
                    

            
            
R2O_FOOTNOTE_DATA = get_footnotes()
#pprint.pprint(R2O_FOOTNOTE_DATA)
product_group_request = requests.get("https://api.ready2order.com/v1/productgroups", headers={"Authorization": API_KEY})
product_groups = product_group_request.json()
root_elements = [pg for pg in product_groups if pg["productgroup_parent"] is None]
other_elements = [pg for pg in product_groups if pg["productgroup_parent"] is not None]
tree = build_tree(root_elements, other_elements)
menu = build_json_menu(tree)

#deduplicate
FOOTNOTES_REF = list(dict.fromkeys(FOOTNOTES_REF))

#throw out inhaltsstoffe we don't need
ALLERGENE = list(
    filter(lambda allergen: allergen['product_id'] in FOOTNOTES_REF, R2O_FOOTNOTE_DATA['allergene']))
INHALTSSTOFFE = list(
    filter(lambda inhaltsstoff: inhaltsstoff['product_id'] in FOOTNOTES_REF, R2O_FOOTNOTE_DATA['inhaltsstoffe']))

# add key
for i, allergen in enumerate(ALLERGENE):
    allergen['footnote_key'] = str(i)
for i, inhaltsstoff in enumerate(INHALTSSTOFFE):
    inhaltsstoff['footnote_key'] = chr(ord('a') + i)

# fix tree
menu = set_footnotes(menu)

FOOTNOTES['Allergene'] = [{'key': allergen['footnote_key'],
                           'name': allergen['product_name']}
                          for allergen in ALLERGENE]
FOOTNOTES['Inhaltsstoffe'] = [{'key': inhaltsstoff['footnote_key'],
                               'name': inhaltsstoff['product_name']}
                              for inhaltsstoff in INHALTSSTOFFE]

data = { 'products': menu,
         'footnote_data': FOOTNOTES }
print(json.dumps(data, sort_keys=True, indent=4))
