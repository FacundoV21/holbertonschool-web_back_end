#!/usr/bin/env python3
"""
    list a document
"""

def schools_by_topic(mongo_collection, topic):
    """ lists schools by topic """
    lista = mongo_collection.find({"topics": topic})
    if not lista:
        return []
    return lista
