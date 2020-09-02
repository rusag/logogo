from lxml import etree
from lxml.builder import ElementMaker
import sys

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)





class SVG_LOGOGO:
    def __init__(self, brand, 
                        slogan,
                        industry='',
                        style='',
                        font_family="SpaceGrotesk-Bold, Space Grotesk",
                        tag='',
                        symbol='',
                        font_color="#464646",
                        line_color="#707070",
                        template='template2'):
        #texts
        self.brand = brand
        self.slogan = slogan
        #fonts
        self.industry = industry
        self.style =  style
        self.font_family = font_family
        self.tag = tag
        self.symbol = symbol
        #color groups
        self.font_color = font_color        
        self.line_color = line_color
        self.template = template

    def template1(self):
        svg = etree.Element("{http://www.w3.org/2000/svg}svg",attrib={"xlink":"http://www.w3.org/1999/xlink", 'width':"570", 'height':"345", "viewBox":"0 0 570 345"})
        defs = etree.SubElement(svg,"defs")
        clipPath = etree.SubElement(defs,"clipPath", attrib={"id":"clip-Icon_Typo_Long"})
        clipPath_rect = etree.SubElement(clipPath,"rect", attrib={"width":"570","height":"345"})

        g_icon = etree.SubElement(svg,"g", attrib={'id':"Icon_Typo_Long", 'data-name':"Icon + Typo Long", 'clip-path':"url(#clip-Icon_Typo_Long)"})
        g_icon_rect = etree.SubElement(g_icon,"rect", attrib={"width":"570","height":"345", "fill":"#fff"})
        g_icon_circle = etree.SubElement(g_icon,"circle", attrib={"id":"Icon_Placeholder","data-name":"Icon Placeholder","cx":"35","cy":"35","r":"35","transform":"translate(250 69)","fill":"#464646"})
        g_icon_slogan = etree.SubElement(g_icon,"text", attrib={"id":"Slogan Placeholder","data-name":"Slogan Placeholder","transform":"translate(214 273)","fill":self.font_color,"font-size":"18","font-family":self.font_family,"font-weight":"700"})
        g_icon_text_tspan = etree.SubElement(g_icon_slogan,"tspan", attrib={"x":"0","y":"0"}).text = self.slogan
        g_icon_text = etree.SubElement(g_icon,"text", attrib={"id":"Text Placeholder","data-name":"Text Placeholder","transform":"translate(285 196)","fill":self.font_color,"font-size":"57","font-family":self.font_family,"font-weight":"700"})
        g_icon_text_brand = etree.SubElement(g_icon_text,"tspan", attrib={"x":"-88.322","y":"0"}).text = self.brand[:len(self.brand)//2]
        g_icon_text_name = etree.SubElement(g_icon_text,"tspan", attrib={"x":"-76.665","y":"50"}).text = self.brand[len(self.brand)//2:]
        # g_icon_eclipse = etree.SubElement(g_icon,"ellipse", attrib={"id":"Icon_Placeholder","data-name":"Icon Placeholder","cx":"33.5","cy":"33","rx":"33.5","ry":"33","transform":"translate(72 140)","fill":"#464646"})
        g_area = etree.SubElement(g_icon,"g", attrib={"id":"Safe_Area_-_Don_t_Render","data-name":"Safe Area - Don&apos;t Render","transform":"translate(-0.5 -0.5)"})
        g_area_line_1 = etree.SubElement(g_area,"line", attrib={"id":"Line_1","data-name":"Line 1","y1":"345","transform":"translate(69.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
        g_area_line_2 = etree.SubElement(g_area,"line", attrib={"id":"Line_2","data-name":"Line 2","y1":"345","transform":"translate(500.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
        g_area_line_3 = etree.SubElement(g_area,"line", attrib={"id":"Line_3","data-name":"Line 3","x2":"570","transform":"translate(0.5 69.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
        g_area_line_4 = etree.SubElement(g_area,"line", attrib={"id":"Line_4","data-name":"Line 4","x2":"570","transform":"translate(0.5 276.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
        g_rectangle = etree.SubElement(g_area,"g", attrib={"id":"Rectangle_1","data-name":"Rectangle 1","transform":"translate(0.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
        g_rectangle_rect1 = etree.SubElement(g_rectangle,"rect", attrib={"width":"570","height":"345","stroke":"none"})
        g_rectangle_rect2 = etree.SubElement(g_rectangle,"rect", attrib={"x":"0.5","y":"0.5","width":"569","height":"344","fill":"none"})
        tree = svg.getroottree()
        logger.error(f"{tree} of type {type(tree)}") 
        svg_code = etree.tostring(tree)
        logger.error(f"{svg_code} of type {type(svg_code)}") 
        # svg2png(bytestring=svg_code,write_to= svg_path)
        return svg_code

    def template2(self):
        svg = etree.Element("{http://www.w3.org/2000/svg}svg",attrib={"xlink":"http://www.w3.org/1999/xlink", 'width':"570", 'height':"345", "viewBox":"0 0 570 345"})
        defs = etree.SubElement(svg,"defs")
        clipPath = etree.SubElement(defs,"clipPath", attrib={"id":"clip-Icon_Typo_Long"})
        clipPath_rect = etree.SubElement(clipPath,"rect", attrib={"width":"570","height":"345"})
        g_icon = etree.SubElement(svg,"g", attrib={'id':"Icon_Typo_Long", 'data-name':"Icon + Typo Long", 'clip-path':"url(#clip-Icon_Typo_Long)"})
        g_icon_rect = etree.SubElement(g_icon,"rect", attrib={"width":"570","height":"345", "fill":"#fff"})
        g_icon_text = etree.SubElement(g_icon,"text", attrib={"id":"Text_Placeholder","data-name":"Text Placeholder","transform":"translate(151 195)","fill":self.font_color,"font-size":"57","font-family":self.font_family,"font-weight":"700"})
        g_icon_text_tspan = etree.SubElement(g_icon_text,"tspan", attrib={"x":"0","y":"0"}).text = self.brand
        g_icon_eclipse = etree.SubElement(g_icon,"ellipse", attrib={"id":"Icon_Placeholder","data-name":"Icon Placeholder","cx":"33.5","cy":"33","rx":"33.5","ry":"33","transform":"translate(72 140)","fill":"#464646"})
        g_area = etree.SubElement(g_icon,"g", attrib={"id":"Safe_Area_-_Don_t_Render","data-name":"Safe Area - Don&apos;t Render","transform":"translate(-0.5 -0.5)"})
        g_area_line_1 = etree.SubElement(g_area,"line", attrib={"id":"Line_1","data-name":"Line 1","y1":"345","transform":"translate(69.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
        g_area_line_2 = etree.SubElement(g_area,"line", attrib={"id":"Line_2","data-name":"Line 2","y1":"345","transform":"translate(500.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
        g_area_line_3 = etree.SubElement(g_area,"line", attrib={"id":"Line_3","data-name":"Line 3","x2":"570","transform":"translate(0.5 69.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
        g_area_line_4 = etree.SubElement(g_area,"line", attrib={"id":"Line_4","data-name":"Line 4","x2":"570","transform":"translate(0.5 276.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
        g_rectangle = etree.SubElement(g_area,"g", attrib={"id":"Rectangle_1","data-name":"Rectangle 1","transform":"translate(0.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
        g_rectangle_rect1 = etree.SubElement(g_rectangle,"rect", attrib={"width":"570","height":"345","stroke":"none"})
        g_rectangle_rect2 = etree.SubElement(g_rectangle,"rect", attrib={"x":"0.5","y":"0.5","width":"569","height":"344","fill":"none"})
        tree = svg.getroottree()
        logger.error(f"{tree} of type {type(tree)}") 
        svg_code = etree.tostring(tree)
        logger.error(f"{svg_code} of type {type(svg_code)}") 
        # svg2png(bytestring=svg_code,write_to= svg_path)
        return svg_code

    # def template3(self):
    #     svg = etree.Element("{http://www.w3.org/2000/svg}svg",attrib={"xlink":"http://www.w3.org/1999/xlink", 'width':"570", 'height':"345", "viewBox":"0 0 570 345"})
    #     defs = etree.SubElement(svg,"defs")
    #     clipPath = etree.SubElement(defs,"clipPath", attrib={"id":"clip-Icon_Typo_Long"})
    #     clipPath_rect = etree.SubElement(clipPath,"rect", attrib={"width":"570","height":"345"})
    #     g_icon = etree.SubElement(svg,"g", attrib={'id':"Icon_Typo_Long", 'data-name':"Icon + Typo Long", 'clip-path':"url(#clip-Icon_Typo_Long)"})
    #     g_icon_rect = etree.SubElement(g_icon,"rect", attrib={"width":"570","height":"345", "fill":"#fff"})
    #     g_icon_text = etree.SubElement(g_icon,"text", attrib={"id":"Text_Placeholder","data-name":"Text Placeholder","transform":"translate(151 195)","fill":self.font_color,"font-size":"57","font-family":self.font_family,"font-weight":"700"})
    #     g_icon_text_tspan = etree.SubElement(g_icon_text,"tspan", attrib={"x":"0","y":"0"}).text = self.brand
    #     g_icon_eclipse = etree.SubElement(g_icon,"ellipse", attrib={"id":"Icon_Placeholder","data-name":"Icon Placeholder","cx":"33.5","cy":"33","rx":"33.5","ry":"33","transform":"translate(72 140)","fill":"#464646"})
    #     g_area = etree.SubElement(g_icon,"g", attrib={"id":"Safe_Area_-_Don_t_Render","data-name":"Safe Area - Don&apos;t Render","transform":"translate(-0.5 -0.5)"})
    #     g_area_line_1 = etree.SubElement(g_area,"line", attrib={"id":"Line_1","data-name":"Line 1","y1":"345","transform":"translate(69.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_2 = etree.SubElement(g_area,"line", attrib={"id":"Line_2","data-name":"Line 2","y1":"345","transform":"translate(500.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_3 = etree.SubElement(g_area,"line", attrib={"id":"Line_3","data-name":"Line 3","x2":"570","transform":"translate(0.5 69.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_4 = etree.SubElement(g_area,"line", attrib={"id":"Line_4","data-name":"Line 4","x2":"570","transform":"translate(0.5 276.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_rectangle = etree.SubElement(g_area,"g", attrib={"id":"Rectangle_1","data-name":"Rectangle 1","transform":"translate(0.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_rectangle_rect1 = etree.SubElement(g_rectangle,"rect", attrib={"width":"570","height":"345","stroke":"none"})
    #     g_rectangle_rect2 = etree.SubElement(g_rectangle,"rect", attrib={"x":"0.5","y":"0.5","width":"569","height":"344","fill":"none"})
    #     tree = svg.getroottree()
    #     logger.error(f"{tree} of type {type(tree)}") 
    #     svg_code = etree.tostring(tree)
    #     logger.error(f"{svg_code} of type {type(svg_code)}") 
    #     # svg2png(bytestring=svg_code,write_to= svg_path)
    #     return svg_code

    # def template4(self):
    #     svg = etree.Element("{http://www.w3.org/2000/svg}svg",attrib={"xlink":"http://www.w3.org/1999/xlink", 'width':"570", 'height':"345", "viewBox":"0 0 570 345"})
    #     defs = etree.SubElement(svg,"defs")
    #     clipPath = etree.SubElement(defs,"clipPath", attrib={"id":"clip-Icon_Typo_Long"})
    #     clipPath_rect = etree.SubElement(clipPath,"rect", attrib={"width":"570","height":"345"})
    #     g_icon = etree.SubElement(svg,"g", attrib={'id':"Icon_Typo_Long", 'data-name':"Icon + Typo Long", 'clip-path':"url(#clip-Icon_Typo_Long)"})
    #     g_icon_rect = etree.SubElement(g_icon,"rect", attrib={"width":"570","height":"345", "fill":"#fff"})
    #     g_icon_text = etree.SubElement(g_icon,"text", attrib={"id":"Text_Placeholder","data-name":"Text Placeholder","transform":"translate(151 195)","fill":self.font_color,"font-size":"57","font-family":self.font_family,"font-weight":"700"})
    #     g_icon_text_tspan = etree.SubElement(g_icon_text,"tspan", attrib={"x":"0","y":"0"}).text = self.brand
    #     g_icon_eclipse = etree.SubElement(g_icon,"ellipse", attrib={"id":"Icon_Placeholder","data-name":"Icon Placeholder","cx":"33.5","cy":"33","rx":"33.5","ry":"33","transform":"translate(72 140)","fill":"#464646"})
    #     g_area = etree.SubElement(g_icon,"g", attrib={"id":"Safe_Area_-_Don_t_Render","data-name":"Safe Area - Don&apos;t Render","transform":"translate(-0.5 -0.5)"})
    #     g_area_line_1 = etree.SubElement(g_area,"line", attrib={"id":"Line_1","data-name":"Line 1","y1":"345","transform":"translate(69.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_2 = etree.SubElement(g_area,"line", attrib={"id":"Line_2","data-name":"Line 2","y1":"345","transform":"translate(500.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_3 = etree.SubElement(g_area,"line", attrib={"id":"Line_3","data-name":"Line 3","x2":"570","transform":"translate(0.5 69.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_4 = etree.SubElement(g_area,"line", attrib={"id":"Line_4","data-name":"Line 4","x2":"570","transform":"translate(0.5 276.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_rectangle = etree.SubElement(g_area,"g", attrib={"id":"Rectangle_1","data-name":"Rectangle 1","transform":"translate(0.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_rectangle_rect1 = etree.SubElement(g_rectangle,"rect", attrib={"width":"570","height":"345","stroke":"none"})
    #     g_rectangle_rect2 = etree.SubElement(g_rectangle,"rect", attrib={"x":"0.5","y":"0.5","width":"569","height":"344","fill":"none"})
    #     tree = svg.getroottree()
    #     logger.error(f"{tree} of type {type(tree)}") 
    #     svg_code = etree.tostring(tree)
    #     logger.error(f"{svg_code} of type {type(svg_code)}") 
    #     # svg2png(bytestring=svg_code,write_to= svg_path)
    #     return svg_code

    # def template5(self):
    #     svg = etree.Element("{http://www.w3.org/2000/svg}svg",attrib={"xlink":"http://www.w3.org/1999/xlink", 'width':"570", 'height':"345", "viewBox":"0 0 570 345"})
    #     defs = etree.SubElement(svg,"defs")
    #     clipPath = etree.SubElement(defs,"clipPath", attrib={"id":"clip-Icon_Typo_Long"})
    #     clipPath_rect = etree.SubElement(clipPath,"rect", attrib={"width":"570","height":"345"})
    #     g_icon = etree.SubElement(svg,"g", attrib={'id':"Icon_Typo_Long", 'data-name':"Icon + Typo Long", 'clip-path':"url(#clip-Icon_Typo_Long)"})
    #     g_icon_rect = etree.SubElement(g_icon,"rect", attrib={"width":"570","height":"345", "fill":"#fff"})
    #     g_icon_text = etree.SubElement(g_icon,"text", attrib={"id":"Text_Placeholder","data-name":"Text Placeholder","transform":"translate(151 195)","fill":self.font_color,"font-size":"57","font-family":self.font_family,"font-weight":"700"})
    #     g_icon_text_tspan = etree.SubElement(g_icon_text,"tspan", attrib={"x":"0","y":"0"}).text = self.brand
    #     g_icon_eclipse = etree.SubElement(g_icon,"ellipse", attrib={"id":"Icon_Placeholder","data-name":"Icon Placeholder","cx":"33.5","cy":"33","rx":"33.5","ry":"33","transform":"translate(72 140)","fill":"#464646"})
    #     g_area = etree.SubElement(g_icon,"g", attrib={"id":"Safe_Area_-_Don_t_Render","data-name":"Safe Area - Don&apos;t Render","transform":"translate(-0.5 -0.5)"})
    #     g_area_line_1 = etree.SubElement(g_area,"line", attrib={"id":"Line_1","data-name":"Line 1","y1":"345","transform":"translate(69.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_2 = etree.SubElement(g_area,"line", attrib={"id":"Line_2","data-name":"Line 2","y1":"345","transform":"translate(500.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_3 = etree.SubElement(g_area,"line", attrib={"id":"Line_3","data-name":"Line 3","x2":"570","transform":"translate(0.5 69.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_4 = etree.SubElement(g_area,"line", attrib={"id":"Line_4","data-name":"Line 4","x2":"570","transform":"translate(0.5 276.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_rectangle = etree.SubElement(g_area,"g", attrib={"id":"Rectangle_1","data-name":"Rectangle 1","transform":"translate(0.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_rectangle_rect1 = etree.SubElement(g_rectangle,"rect", attrib={"width":"570","height":"345","stroke":"none"})
    #     g_rectangle_rect2 = etree.SubElement(g_rectangle,"rect", attrib={"x":"0.5","y":"0.5","width":"569","height":"344","fill":"none"})
    #     tree = svg.getroottree()
    #     logger.error(f"{tree} of type {type(tree)}") 
    #     svg_code = etree.tostring(tree)
    #     logger.error(f"{svg_code} of type {type(svg_code)}") 
    #     # svg2png(bytestring=svg_code,write_to= svg_path)
    #     return svg_code

    # def template6(self):
    #     svg = etree.Element("{http://www.w3.org/2000/svg}svg",attrib={"xlink":"http://www.w3.org/1999/xlink", 'width':"570", 'height':"345", "viewBox":"0 0 570 345"})
    #     defs = etree.SubElement(svg,"defs")
    #     clipPath = etree.SubElement(defs,"clipPath", attrib={"id":"clip-Icon_Typo_Long"})
    #     clipPath_rect = etree.SubElement(clipPath,"rect", attrib={"width":"570","height":"345"})
    #     g_icon = etree.SubElement(svg,"g", attrib={'id':"Icon_Typo_Long", 'data-name':"Icon + Typo Long", 'clip-path':"url(#clip-Icon_Typo_Long)"})
    #     g_icon_rect = etree.SubElement(g_icon,"rect", attrib={"width":"570","height":"345", "fill":"#fff"})
    #     g_icon_text = etree.SubElement(g_icon,"text", attrib={"id":"Text_Placeholder","data-name":"Text Placeholder","transform":"translate(151 195)","fill":self.font_color,"font-size":"57","font-family":self.font_family,"font-weight":"700"})
    #     g_icon_text_tspan = etree.SubElement(g_icon_text,"tspan", attrib={"x":"0","y":"0"}).text = self.brand
    #     g_icon_eclipse = etree.SubElement(g_icon,"ellipse", attrib={"id":"Icon_Placeholder","data-name":"Icon Placeholder","cx":"33.5","cy":"33","rx":"33.5","ry":"33","transform":"translate(72 140)","fill":"#464646"})
    #     g_area = etree.SubElement(g_icon,"g", attrib={"id":"Safe_Area_-_Don_t_Render","data-name":"Safe Area - Don&apos;t Render","transform":"translate(-0.5 -0.5)"})
    #     g_area_line_1 = etree.SubElement(g_area,"line", attrib={"id":"Line_1","data-name":"Line 1","y1":"345","transform":"translate(69.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_2 = etree.SubElement(g_area,"line", attrib={"id":"Line_2","data-name":"Line 2","y1":"345","transform":"translate(500.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_3 = etree.SubElement(g_area,"line", attrib={"id":"Line_3","data-name":"Line 3","x2":"570","transform":"translate(0.5 69.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_4 = etree.SubElement(g_area,"line", attrib={"id":"Line_4","data-name":"Line 4","x2":"570","transform":"translate(0.5 276.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_rectangle = etree.SubElement(g_area,"g", attrib={"id":"Rectangle_1","data-name":"Rectangle 1","transform":"translate(0.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_rectangle_rect1 = etree.SubElement(g_rectangle,"rect", attrib={"width":"570","height":"345","stroke":"none"})
    #     g_rectangle_rect2 = etree.SubElement(g_rectangle,"rect", attrib={"x":"0.5","y":"0.5","width":"569","height":"344","fill":"none"})
    #     tree = svg.getroottree()
    #     logger.error(f"{tree} of type {type(tree)}") 
    #     svg_code = etree.tostring(tree)
    #     logger.error(f"{svg_code} of type {type(svg_code)}") 
    #     # svg2png(bytestring=svg_code,write_to= svg_path)
    #     return svg_code

    # def template7(self):
    #     svg = etree.Element("{http://www.w3.org/2000/svg}svg",attrib={"xlink":"http://www.w3.org/1999/xlink", 'width':"570", 'height':"345", "viewBox":"0 0 570 345"})
    #     defs = etree.SubElement(svg,"defs")
    #     clipPath = etree.SubElement(defs,"clipPath", attrib={"id":"clip-Icon_Typo_Long"})
    #     clipPath_rect = etree.SubElement(clipPath,"rect", attrib={"width":"570","height":"345"})
    #     g_icon = etree.SubElement(svg,"g", attrib={'id':"Icon_Typo_Long", 'data-name':"Icon + Typo Long", 'clip-path':"url(#clip-Icon_Typo_Long)"})
    #     g_icon_rect = etree.SubElement(g_icon,"rect", attrib={"width":"570","height":"345", "fill":"#fff"})
    #     g_icon_text = etree.SubElement(g_icon,"text", attrib={"id":"Text_Placeholder","data-name":"Text Placeholder","transform":"translate(151 195)","fill":self.font_color,"font-size":"57","font-family":self.font_family,"font-weight":"700"})
    #     g_icon_text_tspan = etree.SubElement(g_icon_text,"tspan", attrib={"x":"0","y":"0"}).text = self.brand
    #     g_icon_eclipse = etree.SubElement(g_icon,"ellipse", attrib={"id":"Icon_Placeholder","data-name":"Icon Placeholder","cx":"33.5","cy":"33","rx":"33.5","ry":"33","transform":"translate(72 140)","fill":"#464646"})
    #     g_area = etree.SubElement(g_icon,"g", attrib={"id":"Safe_Area_-_Don_t_Render","data-name":"Safe Area - Don&apos;t Render","transform":"translate(-0.5 -0.5)"})
    #     g_area_line_1 = etree.SubElement(g_area,"line", attrib={"id":"Line_1","data-name":"Line 1","y1":"345","transform":"translate(69.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_2 = etree.SubElement(g_area,"line", attrib={"id":"Line_2","data-name":"Line 2","y1":"345","transform":"translate(500.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_3 = etree.SubElement(g_area,"line", attrib={"id":"Line_3","data-name":"Line 3","x2":"570","transform":"translate(0.5 69.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_area_line_4 = etree.SubElement(g_area,"line", attrib={"id":"Line_4","data-name":"Line 4","x2":"570","transform":"translate(0.5 276.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_rectangle = etree.SubElement(g_area,"g", attrib={"id":"Rectangle_1","data-name":"Rectangle 1","transform":"translate(0.5 0.5)","fill":"none","stroke":self.line_color,"stroke-width":"1"})
    #     g_rectangle_rect1 = etree.SubElement(g_rectangle,"rect", attrib={"width":"570","height":"345","stroke":"none"})
    #     g_rectangle_rect2 = etree.SubElement(g_rectangle,"rect", attrib={"x":"0.5","y":"0.5","width":"569","height":"344","fill":"none"})
    #     tree = svg.getroottree()
    #     logger.error(f"{tree} of type {type(tree)}") 
    #     svg_code = etree.tostring(tree)
    #     logger.error(f"{svg_code} of type {type(svg_code)}") 
    #     # svg2png(bytestring=svg_code,write_to= svg_path)
    #     return svg_code