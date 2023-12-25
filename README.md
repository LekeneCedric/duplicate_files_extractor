# no-more-duplicates-files
---

## Project Goal

The goal of this project is to help us to:

- List all duplicates files base on a parent directory

- Delete all duplicates files base on a parent directory

## what remains to be done ?
- [ ] integration of a cli interface allowing:
  - execute commands (duplicate search, selection, deletion)
  - visualization of the directory tree (just towards duplicates)
  - selection of duplicates to delete
## How its work ? :

To fully understand how this project works, we all need to first understand this

- ### What is a Hash Function ?

  A hash function is a mathematical algorithm that takes an input (or 'message') and produces a fixed-size string of characters, which is typically a hash code.

- ### What is a file Hashing ?

  When it comes to files, the contents of the file are the input to the hash function. The hash function then produces a fixed-length hash value (often represented as a hexadecimal number). Even a small change in the file content should result in a substantially different hash value.

- ### Duplicate File Detection

  By comparing the hash values of files, you can quickly determine whether the file contents are identical. If two files have the same hash value, they are highly likely to be duplicates. This is because, for practical purposes, it's extremely rare for different files to produce the same hash.


## Implementation :

1. We browse the parent directory, and save its entire tree in a data structure **(n-ary tree)**

2. Next time , for each **n-ary tree** node ( correspoding to sub_folders ) we browse his files and save hash in another datastructure (**dictionary**) like key = file_hash and value = array of files that have same hash

3. Finally , we browse her dictionary to show / delete all duplicates files in tree


## How to run source code locally ?

- ### RUN TESTS :
```make test```

- ### RUN PROJECT :
```make run```

- ### CLEAN PROJECT :
```make clean```
