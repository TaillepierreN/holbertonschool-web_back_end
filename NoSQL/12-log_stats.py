#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
import pymongo

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def get_log_stats(nginx_collection):
    """print stat about Nginx logs"""

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    for method in METHODS:
        count = len(list(nginx_collection.find({'method': method})))
        print(f"\tmethod {method}: {count}")

    status_checks = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print(f"{status_checks} status check")


if __name__ == "__main__":
    nginx = pymongo.MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    get_log_stats(nginx)
