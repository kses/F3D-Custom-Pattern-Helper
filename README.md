# Finale3D Custom Pattern Helper

Finale3D(F3D) has a greatway of creating effects called VDL. This is the best way to create effects in F3D, but it also has an effect editor for doing effects not possible to do with VDL.

## Shapes Supported
- Azimuth Slices
- Cartesian Bands
- Six sided peony

### Azimuth Slices
Azimuth slice option splits the sphere in parts same way as slices in a orange. 4 slices creates a 1/4 Peony

![1/4 Peony](./images/quarter_peony.jpg)

### Cartesian Bands
Cartesian Bands splits the sphere evenly along one axis.

![Ghost Blue to 4 Colors](./images/ghost_blue_to_4colors.jpg)

### Six Sided Peony
It splits the peony in six parts like the sides on a dice but projected on a sphere. The option to select the number of parts is not possible with this shape.

![Six sided peony](./images/six_sided.png)

## How to use the tool:

### Run it at your computer
- Install Python3
- Use pip/pip3 to install the required packages
- Run the tool and answer on the questions.
- Copy the JSON list and paste into F3D effect editor.

### Run it online
- Go to https://repl.it/
- Start a python Repl
- Copy the code from the github to the repl
- Press Run
- Answer on the questions.
- Copy the JSON list and paste into F3D effect editor.

## How to import it into F3D:
Fastes way is to create a simple effect that has the colors you want. For example if you want to create a "1/4 Peony (Red, Green, Purple, Yellow)", with VDL create a "Red & Green & Purple & Yellow Peony" it is a multi color peony with the colors you want. Open the new effect in the editor. Open the "Petal", change the pattern to "custom JSON", paste the JSON list you got from the tool into the "Custom Break Pattern JSON" field.

![Effect Editor](./images/editor_w_comments.png)