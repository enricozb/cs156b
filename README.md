# Caltech CS 156b: The Netflix Competition ("Learning Systems")

#### Collaborators:
 - [Michelle Anthony](https://github.com/michelle-aa)
 - [Enrico Borba](https://github.com/enricozb)
 - Julia Deacon
 - [Claire Goeckner-Wald](https://github.com/cgoecknerwald)
 - Bianca Yang


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

The "research" folder will be used to store research papers & other handouts that are of value to this project. If you can follow a URL to the project, list it in [Links.md](research/Links.md), also in that folder. Otherwise, simply upload the paper (preferably as a PDF). **This folder should be removed before the repository is made public.**

## C++ Style Guide

This project uses C++ 14, following the [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html). 

## Structure

There will be an abstract model class, `model.cc` and `model.h` that all models must inherit. The `model` class will include functions `train`, `predict`, `serialize` and `deserialize` functions that must be implemented in all subclasses.

## Tasks & Goals
These will change as we progress.

 - [ ] Set-up MLPack, Boost, CMake, C++ 14 for everyone
 - [ ] Parse data
 - [ ] Research models & techniques
 - [ ] Formalize code structure
 - [ ] Implement code
 - [ ] Perform better than Netflix R&D team performed in 2005
 - [ ] Decide on model(s) & technique(s)
 - [ ] Final submission
 - [ ] Make a project website to showcase work (optional)



