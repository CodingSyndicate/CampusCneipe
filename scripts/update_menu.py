#!/usr/bin/env python3

import requests
import pprint
import json
import os

pp = pprint.PrettyPrinter()
API_KEY = os.environ["R2O_API_KEY"]

BLACKLISTED_PRODUCTGROUPS = [
    "Cocktailzutaten",
    "Pasta Tuesday",
    "Pasta-Tuesday",
    "Special shit",
    "Grillen",
    "Teure Getränke",
    "Favoriten",
    "Specials",
    "TO GO"
]

BLACKLISTED_PRODUCTS = [
    "" #Platzhalter
    ]

def build_tree(tree, pgs):
    tree = [e for e in tree if e["productgroup_name"] not in BLACKLISTED_PRODUCTGROUPS]
    pgs = [e for e in pgs if e["productgroup_name"] not in BLACKLISTED_PRODUCTGROUPS]
    tree = sorted(tree, key=lambda pg: int(pg["productgroup_sortIndex"]))
    for e in tree:
        childs_of_e = [c for c in pgs if c["productgroup_parent"] == e["productgroup_id"]]
        e["child_group"] = childs_of_e
        product_request = requests.get(
            "https://api.ready2order.com/v1/products",
            params={"productgroup_id": e["productgroup_id"], "includeProductIngredients": True},
            headers={"Authorization": API_KEY},
        )
        products = product_request.json()
        products = sorted(products, key=lambda p: int(p["product_sortIndex"]))
        e["child_products"] = [p for p in products if p["product_name"] not in BLACKLISTED_PRODUCTS]
        build_tree(e["child_group"], pgs)
    return tree

product_group_request = requests.get("https://api.ready2order.com/v1/productgroups", headers={"Authorization": API_KEY})
product_groups = product_group_request.json()

root_elements = [pg for pg in product_groups if pg["productgroup_parent"] is None]
other_elements = [pg for pg in product_groups if pg["productgroup_parent"] is not None]

tree = build_tree(root_elements, other_elements)


def build_json_menu(tree, level=1):
    data = []
    for pg in tree:
        pg_data = {"name": pg["productgroup_name"]}
        if "child_products" in pg:
            pg_data["products"] = []
            for p in pg["child_products"]:
                ingredients = []
                amount = ""
                if "productingredient" in p:
                    # list ingredient sorted by quantity, in descending order
                    if len(p["productingredient"]) > 0:
                        p["productingredient"].sort(key=lambda e: e["ingredient_quantity"])
                    for ingredient in p["productingredient"]:
                        if ingredient["ingredient_name"] == "Liter":
                            amount = "{:0,.2f}".format(float(ingredient["ingredient_quantity"])).rstrip("0").rstrip(".")
                        else:
                            continue
                            #ingredients.append(ingredient["ingredient_name"])
                    #ingredients = ", ".join(ingredients)
                pg_data["products"].append(
                    {"name": p["product_name"],
                     "price": "{:0,.2f}".format(float(p["product_price"])),
                     "ingredients": p["product_description"].lstrip("Zutaten").lstrip(":").lstrip(),
                     "amount": amount}
                )
        if "child_group" in pg:
            pg_data["childs"] = build_json_menu(pg["child_group"], level + 1)
        data.append(pg_data)
    return data


data = build_json_menu(tree)
print(json.dumps(data, sort_keys=True, indent=4))
