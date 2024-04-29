#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
import pymongo

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def get_log_stats(nginx_collection):
    """print stat about Nginx logs"""

    total_logs = nginx_collection.count_documents({})
    print("{} logs".format(total_logs))

    print("Methods:")
    for method in METHODS:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_checks = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status_checks))


if __name__ == "__main__":
    nginx = pymongo.MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    get_log_stats(nginx)
