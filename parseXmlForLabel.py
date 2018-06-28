import xml.etree.ElementTree as ET
import glob
from xmlAttribution import XmlAttr

'''
注：labelImg打标出来的bbox,是xmin, ymin, xmax, ymax,分别是横轴和纵轴，所以，对于上下朝向的烟图片，就应该用xmin或者xmax进行列队划分
而左右朝向的用ymin或者ymax，对于标志物，因为太小了，所以，他和其他的烟应该是距离挺大的，应该判断他是否在xmin和xmax之间
'''

def parse_all_xml(xml_glob):
    if len(xml_glob) < 1:
        raise Exception('xml_glob has no element!')
    attr_list = []
    for xml_file in xml_glob:
        xml_attr = XmlAttr()
        tree = ET.parse(xml_file)
        parse_single_xml(tree, xml_attr)
        attr_list.append(xml_attr)
    return attr_list

def parse_single_xml(tree, xml_attr):
    root = tree.getroot()
    xml_attr.set_filename(root.find('filename').text)

    filesize = root.find('size')
    shape = []
    for child in filesize:
        shape.append(child.text)
    xml_attr.set_fileshape(shape)

    bboxes = []
    objs = root.findall('object')
    for obj in objs:
        obj_name = obj.find('name').text
        obj_bbox = obj.find('bndbox')
        bbox = []
        for child in obj_bbox:
            bbox.append(child.text)
        bboxes.append(bbox)
    xml_attr.set_bbox(bboxes)

if __name__=='__main__':
    xml_glob = glob.glob('*.xml')
    print(xml_glob)
    attr_list = parse_all_xml(xml_glob)
    for attr in attr_list:
        print(attr.get_filename)
        print(attr.get_fileshape)
        print(attr)
        i = 0
        res = []
        # print(len(attr.get_bboxes))
        aaa = []
        for j in range(len(attr.get_bboxes)):
            # if 29 == j:
                # print('@@@@', i, int(attr.get_bboxes[j][0]) - int(attr.get_bboxes[i][0]))
            if int(attr.get_bboxes[j][0]) - int(attr.get_bboxes[i][0]) < 25:
               res.append(attr.get_bboxes[j])
               aaa.append(j)
            else:
                in_side = False
                for bb in res:
                    # if j == 12:
                    #     print(int(attr.get_bboxes[j][0]) > int(bb[0]), int(attr.get_bboxes[j][2]) < int(bb[2]),
                    #           (int(attr.get_bboxes[j][0]) > int(bb[0])) & (int(attr.get_bboxes[j][2]) < int(bb[2])))
                    if (int(attr.get_bboxes[j][0]) > int(bb[0])) & (int(attr.get_bboxes[j][2]) < int(bb[2])):
                        # print(j, int(attr.get_bboxes[j][0]) > int(bb[0]) & int(attr.get_bboxes[j][2]) < int(bb[2]))
                        in_side = True
                if in_side:
                    res.append(attr.get_bboxes[j])
                if len(res) != 0:
                    print(len(res), '---', i + 1, ':', res)
                # print(aaa)
                i = j
                res = []
                aaa = []
                if not in_side:
                    res.append(attr.get_bboxes[j])
                    aaa.append(j)
        if len(res) != 0:
            print(len(res), '---', i + 1, ':', res, '---')

