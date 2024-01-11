#!/usr/bin/env python3
"""
    inserts a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """ function """
    docs = mongo_collection.insert_one(kwargs)
    return docs.inserted_id
