#!/usr/bin/python
# -*- coding: utf-8 -*-

import pydot
import os
import sys

def quadro_label(label_text):
    counter = 15
    words = label_text.split()
    new_label_text = ""
    for word in words:
        if len(new_label_text)+len(words)+1>counter:
            counter += 15
            new_label_text += "\n"

        new_label_text +=  word
        new_label_text += " "

    return new_label_text

def screen_only_start(node_name):
    os.system("clear")
    print("%s" % (node_name,))

def screen(node_name,transformation_name):
    os.system("clear")
    print("%s -> %s" % (node_name,transformation_name))


def transformation_chain(graph,prev_node,transformation,color):
    screen(prev_node.get_name(),transformation)
    result_node_name = input("Result of thinking: ")
    if result_node_name is "":
        return

    if color == 0:
        fillcolor_name = 'lightblue'
    if color == 1:
        fillcolor_name = 'lightgray'


    result_node_label = quadro_label(result_node_name)

    result_node = pydot.Node(result_node_name,shape="Mrecord",style='filled',fillcolor=fillcolor_name,label=result_node_label)
    graph.add_node(result_node)

    transformation_label = quadro_label(transformation)
    edge = pydot.Edge(prev_node,result_node,label=transformation_label)

    graph.add_edge(edge)
    prev_node = result_node

    main_loop(graph,prev_node,1-color)



def main_loop(graph,start_node,color):
    prev_node = start_node
    screen_only_start(prev_node.get_name())
    transformation = input("Transformation: ")
    if transformation is "":
        return

    list_tr = transformation.split(',')

    for tr in list_tr:
        transformation_chain(graph,prev_node,tr,color)


def main(export_path):
    os.system("clear")
    graph = pydot.Dot(graph_type='digraph')
    """graph = pydot.Dot(prog='neato',mode="major",overlap="0", sep="0.01",dim="3", pack="True", ratio=".75")"""
    graph.set('compound','true')
    graph.set('ranksep',1.25)
    graph.set('nodesep',1.25)
    graph.set('fontname',"Helvetica-Oblique")
    graph.set('resolution',200)
    graph.set('fixedsize','true')

    start_node_name = input("Initial premise: ")
    start_node_label = quadro_label(start_node_name)

    start_node=pydot.Node(start_node_name,shape="Mrecord",fixedsize='true',width=3.0,label=start_node_label, style='filled', fillcolor='lightgray')

    prev_node = start_node
    prev_node_name="start"

    graph.add_node(start_node)

    main_loop(graph,start_node,0)

    graph.write_png(export_path+".png")
    file=open(export_path+'.dot','w+')
    file.write(graph.to_string())
    file.close()

if __name__ == '__main__':
    main(sys.argv[1])
