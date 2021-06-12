import math
def Svg_Line_Graph(array, xlabel, ylabel, whole_label, lines, crosses, x_increment_start, x_increment_by, y_lineevery):
    #array: list of numbers to be graphed. each number advances along the x axis.
    #xlabel: what you want the graph x-axis to be called.
    #ylabel: what you want the graph y-axis to be called.
    #whole_label: what you want the graph title to be called.
    #xlabel: what you want the graph x-axis to be called.
    #lines: boolean, set to enable lines between plots
    #crosses: boolean, set to enable crosses to mark plots
    #x_increment_start: number, what's the smallest x-axis value in the data
    #x_increment_by: number, how far apart each plot is on the x-axis.
    #y_lineevery: number, how far apart between every graph paper line in y axis units

    svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" height="480" width="640">
<line x1="40" y1="40" x2="40" y2="440" style="stroke:rgb(0,0,255);stroke-width:1" />
<line x1="40" y1="440" x2="620" y2="440" style="stroke:rgb(0,0,255);stroke-width:1" />\n"""
    #add y label
    svg += """<text x="-60" y="255" fill="red" transform="rotate(90 20,240)">"""
    svg += ylabel
    svg += "</text>\n"
    #add x label
    svg += """<text x="320" y="475" fill="red" transform="rotate(0 0,0)">"""
    svg += xlabel
    svg += "</text>\n"
    #
    #Do calculations with data parameters
    #
    #
    #form a standalone svg xml with axis lower boundaries already drawn
    svg_x_boundaries = [40,620]
    svg_y_boundaries = [40,440]
    chart_plots = len(array)
    lowestvalue = array[0]
    for i in range(chart_plots): #find the lowest value in the array
        if array[i] < lowestvalue:
            lowestvalue = array[i]
    highestvalue = array[0]
    for i in range(chart_plots): #find the lowest value in the array
        if array[i] > highestvalue:
            highestvalue = array[i]    
    graph_friendly_range_y = highestvalue - lowestvalue
    #get difference between min and max of axes
    graph_friendly_range_x = chart_plots * x_increment_by
    #
    #
    #
    #Use calculations to add incremental lines to graph
    y_inc = math.ceil(graph_friendly_range_y/y_lineevery)
    svg_graph_height = svg_y_boundaries[1]-svg_y_boundaries[0]
    svg_line_distance = svg_graph_height/y_inc
    #draw horizontal lines
    hlinecount = 0
    for i in range(y_inc):
        line_height = (i)*svg_line_distance
        hlinecount = i
        svg += "<line x1=\"31\" y1=\""+str(440-line_height)+"\" x2=\"620\" y2=\""+str(440-line_height)+"\" style=\"stroke:rgb(127,127,127);stroke-width:1\" />\n"
        svg += "<text x=\"20\" y=\""+str(440-line_height)+"\" fill=\"red\" transform=\"rotate(0 0,0)\">"+str((i*y_lineevery)+lowestvalue)+"</text>\n"
    svg += "<text x=\"20\" y=\""+str(40)+"\" fill=\"red\" transform=\"rotate(0 0,0)\">"+str(highestvalue)+"</text>\n"
    #draw vertical lines
    svg_graph_width = svg_x_boundaries[1]-svg_x_boundaries[0]
    svg_line_distance = svg_graph_width/chart_plots
    for i in range(chart_plots):
        friendly_index = i*x_increment_by
        friendly_index += x_increment_start
        line_pos = i*svg_line_distance
        line_pos += 40
        svg += "<line x1=\""+str(line_pos)+"\" y1=\"40\" x2=\""+str(line_pos)+"\" y2=\"449\" style=\"stroke:rgb(127,127,127);stroke-width:1\" />\n"
        svg += "<text x=\""+str(line_pos)+"\" y=\"460\" fill=\"red\" transform=\"rotate(0 0,0)\">"+str(friendly_index)+"</text>\n"
    #
    #draw plots
    svg_pointsx = []
    svg_pointsy = []
    for i in range(chart_plots):

        graphunit_y = svg_graph_height/y_inc
        graphunit_x = svg_graph_width/chart_plots
        pointx = graphunit_x * i #stretch it to the bounds of the graph
        pointx += 40 #heigher x in svg means further right screen so i have to add it to the min
        pointy = 440
        pointy -= (graphunit_y * (array[i]-lowestvalue)) #heigher y in svg means lower on screen so i have to subtract it from the max
        svg_pointsx.append(pointx) #map all data values to coords applicable to the the svg
        svg_pointsy.append(pointy)
        #print(i)
        #print(pointx)
        #print(pointy)
    #print(svg_pointsx)
    #print(svg_pointsy)
    #print("graphing")
    for i in range(len(svg_pointsy)):
        #print(svg_pointsy[i])
        if lines and i!=0:
            x1=svg_pointsx[i-1]
            y1=svg_pointsy[i-1]
            x2=svg_pointsx[i]
            y2=svg_pointsy[i]
            svg += "<line x1=\""+str(x1)+"\" y1=\""+str(y1)+"\" x2=\""+str(x2)+"\" y2=\""+str(y2)+"\" style=\"stroke:rgb(0,127,0);stroke-width:1\" />\n"
        if crosses:
            x1=svg_pointsx[i]
            y1=svg_pointsy[i]
            svg += "<line x1=\""+str(x1+4)+"\" y1=\""+str(y1+4)+"\" x2=\""+str(x1-4)+"\" y2=\""+str(y1-4)+"\" style=\"stroke:rgb(127,0,0);stroke-width:1\" />\n"
            svg += "<line x1=\""+str(x1+4)+"\" y1=\""+str(y1-4)+"\" x2=\""+str(x1-4)+"\" y2=\""+str(y1+4)+"\" style=\"stroke:rgb(127,0,0);stroke-width:1\" />\n"
    svg += """<text x="200" y="25" fill="red" font-size="1.5em" transform="rotate(0 0,0)">"""
    svg += whole_label
    svg += "</text>\n"
    #
    #end
    svg += "</svg>"
    return svg

if __name__ == "__main__":
    sines = []
    for i in range(30):
        sines.append(10*math.sin(math.radians(i*12)))
        #print(i)
    #print(sines)
    print(Svg_Line_Graph(sines, "degrees/6", "sin*10", "SineWave", True, True, 0, 1, 1))

