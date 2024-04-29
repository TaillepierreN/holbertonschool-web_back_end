#!/usr/bin/env python3
"""Function that lists all documents in a collection"""
import pymongo


def list_all(mongo_collection):
    """list all documenti in collection"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
