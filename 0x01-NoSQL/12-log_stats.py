#!/usr/bin/env python3

"""
This module contains a function that displays stats about Nginx logs stored
in MongoDB.
"""

from pymongo import MongoClient


def display_log_stats():
    """
    Display statistics of different HTTP methods in the nginx logs.

    This function connects to a MongoDB database, retrieves the nginx logs
    collection, and prints the count of each HTTP method (GET, POST, PUT,
    PATCH, DELETE) present in the logs.
    """

    client = MongoClient()
    nginx = client.logs.nginx

    print(nginx.count_documents({}), "logs")
    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print(
            f"\tmethod {method}: {nginx.count_documents({'method': method})}"
        )

    print(f"{nginx.count_documents({'path': '/status'})} status check")


if __name__ == "__main__":
    display_log_stats()
