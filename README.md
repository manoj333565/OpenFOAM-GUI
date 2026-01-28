# OpenFOAM-GUI

# FOSSEE Internship Screening Tasks – IIT BOMBAY 

This repository contains my solutions for the FOSSEE Internship screening tasks:  

1. **Task 1:** Binary Tree Implementation with YAML Integration (Python Package)  
2. **Task 2:** Blender Add-on for 2D Cube Array and Mesh Operations  

---

## Task 1: Binary Tree Python Package

### Overview
This Python package allows you to create and manipulate a Binary Tree. Features include:

- Node class for binary tree creation  
- CRUD operations:
  - Add a node  
  - Delete a node or the entire tree  
  - Edit a node value  
  - Print the tree (full or by range)  
- YAML integration:
  - Build a tree from a YAML file  
  - Export a tree to a YAML file  

**Bonus:** The Node class can be modified to support a general tree with multiple children.

### Installation

1. Clone the repository:

bash
git clone https://github.com/manoj333565/fossee-screening.git
cd fossee-screening/task1
git clone https://github.com/manoj333565/fossee-screening.git
cd fossee-screening/task1

 #### 2.(Optional) Create a virtual environment:
     python -m venv venv
    source venv/bin/activate 

### 3.Install dependencies:
  pip install -r requirements.txt

### Running the Test Script

Ensure you are in the task1/ folder.
Run the test script:  python test_script.py

 ### test_script.py demonstrates:

Creating a tree
Adding and deleting nodes
Editing node values
Building a tree from test.yaml
Printing the tree

# Task 2: Blender Add-on
Overview

This Blender add-on provides the following features:
1.UI Panel with input for a natural number N (<20). Out-of-range input triggers a pop-up.
2.Generate N cubes in a 2D array (m × n) in the 3D viewport.
3.Optional: Place cubes in a separate collection and prevent overlaps.
4.Delete selected cubes with a button.
5.Merge selected meshes sharing at least one face (merges vertices and deletes the shared face).

### Installation
Open Blender.
Go to Edit → Preferences → Add-ons → Install.
Select the blender_addon.py file (or zipped add-on folder).
Enable the add-on.

### Usage

1.Open the 3D viewport.
2.Access the add-on panel in the Sidebar (N key → Add-ons tab).
3.Enter a number N (<20) and use the buttons to:
      Generate a 2D cube array
      Delete selected cubes
      Merge selected meshes




