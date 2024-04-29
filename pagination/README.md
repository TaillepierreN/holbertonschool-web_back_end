# Pagination Project Overview

This project explores the concept of pagination in APIs, crucial for handling large datasets effectively. You'll learn to paginate responses, making them more manageable and providing a better user experience by loading data incrementally. This technique is fundamental in real-world applications where extensive datasets are common.

## Resources

- [REST API Design: Pagination](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

## Learning Objectives

- Understanding basic pagination using page numbers and sizes.
- Implementing hypermedia pagination with metadata.
- Creating deletion-resilient pagination to ensure consistency across paginated lists despite underlying data changes.

## Requirements

- All scripts must run on Ubuntu 18.04 using Python 3.7.
- Scripts should be written in compliance with PEP 8 style guidelines.
- Functions and modules must be fully documented and type-annotated.
- Data file: `Popular_Baby_Names.csv`

## Tasks

### 0. Simple helper function
Implement a function `index_range` that computes a range of indexes for pagination given `page` and `page_size` parameters. This utility will help in slicing the dataset appropriately.

### 1. Simple pagination
Using the previously created helper function, implement a pagination method in the `Server` class that retrieves a specific page of baby names from a CSV file.

### 2. Hypermedia pagination
Enhance the simple pagination method to return metadata along with page data, including information about page size, current page, next/previous pages, and total pages.

### 3. Deletion-resilient hypermedia pagination
Modify the pagination logic to handle data deletion gracefully, ensuring users do not miss data when navigating paginated results despite deletions.

## Data Handling

This project uses `Popular_Baby_Names.csv`, a dataset that provides insights into various names' popularity. You will perform pagination operations on this dataset, handling scenarios where data might be queried frequently and modified occasionally.

## Practical Applications

These tasks simulate real-world backend operations, where data integrity and user experience are paramount. You will learn to implement features that are critical for web APIs, enhancing your ability to manage large datasets efficiently.

This project not only teaches you about pagination techniques but also involves handling potential data inconsistencies caused by deletions, preparing you for complex backend development challenges.
