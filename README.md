# CoBT: Collaborative Programming of Behaviour Trees from One Demonstration for Robot Manipulation

Paper link: [arxiv.org/abs/2404.05870v1](https://arxiv.org/abs/2404.05870v1)

Short videos: [link](https://youtu.be/uz768FNIAgM)

Presentation: [link](https://youtu.be/qKNqNqpKtuU)

This repo includes demonstration data, segmented state variables and graphs, and generated BTs for all the 7 tasks discussed in the paper. Furthermore, the responses from the conducted user study are [here](User-study_Responses).

**Note**- 
* The demonstration data ([memory](Memory)) is in .pkl file format. To read the file refer to this [code](Memory/reader.py). 
* In the segmented variables table ([here](Segmented_state_Variables)), red color text represents the effect conditions that are added to the BT, and blue color text represents the pre-conditions for the the next action.

## Pilot-study details
**The pilot study has been approved by the Research Ethics Committee of Technological University Dublin under application id REC-20-52b**
1. General information about each participant was collected at the start. The information collected can be found [here](User-study_Responses/General_information.xlsx).
2. Introduction phase: Each participant was first demonstrated by the expert how to use free-drive mode (lead-through programming mode of the universal robots), gripper controls, and recorder start/stop controls, and then were given a chance to familiarize themselves with the system.
3. Pick-and-place Demonstration: First, an expert described and showed the pick-and-place task to the participant, and then the participant was allowed to record one demonstration. They were also allowed to re-try their demonstrations if dissatisfied.
4. Drawer Demonstration: Similarly, an expert first described and showed the opening of a drawer task to the participant and then the participant was allowed to record one demonstration. They were also allowed to re-try their demonstrations if dissatisfied.
5. Surveys: Finally, they were asked to fill the raw NASA-TLX and Systems Usability Scale (SUS) questionnaire, the responses for which could be found [here](User-study_Responses)
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


