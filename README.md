# CoBT: Collaborative Programming of Behaviour Trees from One Demonstration for Robot Manipulation

This repo includes demonstration data, segmented state variables and graphs, and generated BTs for all the 7 tasks discussed in the paper. Furthermore, the responses from the conducted user study are [here](User-study_Responses).

:point_right: For performance evaluation, several trials were conducted for each task, where the target and goal object’s start pose are changed within **80cmx40cm** (typo in the paper) area on the table between trials.

**Note**- 
* The demonstration data ([memory](Memory)) is in .pkl file format. To read the file refer to this [code](Memory/reader.py). 
* In the segmented variables table ([here](Segmented_state_Variables)), red color text represents the effect conditions that are added to the BT, and blue color text represents the pre-conditions for the the next action.
* The codes for segmentation and BT generation will be released upon acceptance.

## Pick-and-Place
![](/Segmentation_graphs/Segmented_graph_Cube.png)
<img src=/Segmented_state_Variables/P&P.png width="700">
<img src=/Generated_BTs/pick-and-place.png width="700">

## Insert
![](/Segmentation_graphs/Segmented_graph_Insert.png)
<img src=/Segmented_state_Variables/Insert.png width="700">
<img src=/Generated_BTs/insertion.png width="700">

## Erasing
![](/Segmentation_graphs/Segmented_graph_Duster.png)
<img src=/Segmented_state_Variables/Erasing.png width="700">
<img src=/Generated_BTs/duster.png width="700">

## Drawer
![](/Segmentation_graphs/Segmented_graph_Handle.png)
<img src=/Segmented_state_Variables/Drawer.png width="700">
<img src=/Generated_BTs/drawer.png width="700">

## Pouring
![](/Segmentation_graphs/Segmented_graph_Bottle.png)
<img src=/Segmented_state_Variables/Pouring.png width="700">
<img src=/Generated_BTs/pouring.png width="700">

## Kitting
<img src=/Generated_BTs/kitting.png width="700">

## Drawer Pick-and-Place 
<img src=/Generated_BTs/drawer_pp.png width="700">


