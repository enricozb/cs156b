# Caltech CS 156b: The Netflix Competition ("Learning Systems")

#### Collaborators:
 - [Michelle Anthony](https://github.com/michelle-aa)
 - [Enrico Borba](https://github.com/enricozb)
 - [Julia Deacon](https://github.com/jcdeacon)
 - [Claire Goeckner-Wald](http://claire.work/)
 - [Bianca Yang](https://github.com/xrdt)


## Class Description

This is a projects course in Machine Learning (ML) based on the famous Net-
flix competition, considered the Super Bowl of ML at the time, for recommending
movies to different users. Teams will compete for creating the best 
recommender system by applying ML techniques to a huge data set of usermovie
ratings. The teams can explore different learning models and algorithms
(including novel ones) as well as techniques for regularization and validation, aggregation,
optimization, and other aspects of ML that are applicable to this particular
data set.

## Research

The "research" folder will be used to store research papers & other handouts that are of value to this project. If you can follow a URL to the project, list it in [Research.md](research/Research.md), also in that folder. Otherwise, simply upload the paper (preferably as a PDF). **This folder should be removed before the repository is made public.**

## C++ Style Guide

This project uses C++ 14, following the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html). 

## Structure

There will be an abstract model class, `model.cpp` and `model.h` that all models must inherit. The `model` class will include functions `train`, `predict`, `serialize` and `deserialize` functions that must be implemented in all subclasses.

## Tasks & Dates
These will change as we progress. Use the *mm/dd* to indicate the absolute last date to finish by.

 - [ ] *04/14:* Post a test install file (Borba)
 - [ ] *04/17:* Set-up MLPack, Boost, CMake, C++ 14 for everyone
 - [ ] *04/24:* Implement abstract model class
 - [ ] *mm/dd:* Parse data
 - [ ] *mm/dd:* Research models & techniques
 - [ ] *mm/dd:* Formalize code structure
 - [ ] *05/02:* Implement models assigned in week 2
 - [ ] *04/25:* Perform better than Netflix R&D team performed in 2005
 - [ ] *06/02:* Discover about 10 imaginative & novel models 
 - [ ] *mm/dd:* Decide on model(s) & technique(s)
 - [ ] *mm/dd:* Final submission
 - [ ] *mm/dd:* Make a project website to showcase work (optional)

## Weekly Assignments 
Keep it short.

| Week | Anthony   | Borba                                      | Deacon                     | Goeckner-Wald               | Yang                         |
|:----:|-----------|--------------------------------------------|----------------------------|-----------------------------|------------------------------|
|   1  | -         | Set up repo                                | Timelines & workloads      | Readme.md, Links.md         | Timelines & workloads        |
|   2  | SVM       | Create set-up test file. Parsing, SVD, RNN | Deep Learning, Neural Nets | k-NN, Boltzmann Machines    | Decision Trees (Boosted, RF) |
|   3  | -         | -                                          | -                          | -                           | -                            |
|   4  | -         | -                                          | -                          | -                           | -                            |
|   5  | -         | -                                          | -                          | -                           | -                            |
|   6  | -         | -                                          | -                          | -                           | -                            |
|   7  | -         | -                                          | -                          | -                           | -                            |
|   8  | -         | -                                          | -                          | -                           | -                            |
|   9  | -         | -                                          | -                          | -                           | -                            |
|   10 | -         | -                                          | -                          | -                           | -                            |


































