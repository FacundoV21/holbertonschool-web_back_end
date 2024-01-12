#!/usr/bin/env python3
"""
    list a document
"""

def schools_by_topic(mongo_collection, topic):
    """ lists schools by topic """
    list = mongo_collection.find({"topics": topics})
    return list
